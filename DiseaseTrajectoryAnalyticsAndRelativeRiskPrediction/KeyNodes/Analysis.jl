# 迭代分析
# 1.計算該節點熵值
# 2.刪除該節點
# 3.計算子圖圖滴
# 4.計算節點效率值
function iterativeAnalysis()
    # 迭代每一個節點並分析
    for (k, v) in nodeInfoDict
        # 初始化
        initializeDict()
        # 若刪除節點是起始節點，將其生成概率設為0
        if k == globalVar["startPoint"]
            nodeInfoDict[globalVar["startPoint"]].generateProbability = 0
        end

        # ---------- 1.計算該節點熵值 ----------
        sql = "SELECT ENTROPY FROM " * globalVar["timestamp"] * "OriginalInfoTable WHERE DISEASE = '" * k * "'"
        # 該節點熵值
        E_I:: Float64 = collect(skipmissing(select(sql).ENTROPY))[1]

        # ---------- 2.刪除該節點 ----------
        # 被刪除的節點
        DELETE_DISEASE:: String = k
        # 刪除節點
        deleteNode(DELETE_DISEASE)

        # ---------- 3.計算子圖圖熵 ----------
        # 生成概率計算
        generateProbabilityCalc()
        # 全局圖熵計算
        globalGraphEntropyCalc()
        # 子圖熵
        EN_I:: Float64 = globalVar["globalGraphEntropy"]

        # ---------- 4.計算節點效率值 ----------
        # 該節點效率值
        EFFECT_I:: Float64 = EN_I / log10(EN_I / E_I)

        # println("DELETE_DISEASE ", DELETE_DISEASE)
        # println("E_I ", E_I)
        # println("EN_I ", EN_I)
        # println("EFFECT_I ", EFFECT_I)
        # println("")

        # INSERT INTO AnalysisResultTable
        # 若值為NaN，改為-1以寫入資料庫
        E_I = isequal(E_I, NaN) ? -1 : E_I
        EN_I = isequal(EN_I, NaN) ? -1 : EN_I
        EFFECT_I = isequal(EFFECT_I, NaN) ? -1 : EFFECT_I
        sql = "INSERT INTO " * globalVar["timestamp"] * "AnalysisResultTable (DELETE_DISEASE, E_I, EN_I, EFFECT_I) VALUES('" * DELETE_DISEASE * "', " * string(E_I) * ", " * string(EN_I) * ", " * string(EFFECT_I) * ");"
        insertInto(sql)

        # 子圖詳細資訊
        # println("刪除疾病為: ", k)
        # for (i, j) in nodeInfoDict
        #     println("疾病: ", i)
        #     println("PV_I: ", j.generateProbability)
        #     println("ENTROPY: ", j.nodeEntropy)
        # end
        # println()

        # INSERT INTO 子圖詳細資訊
        for (i, j) in nodeInfoDict
            # INSERT INTO OriginalInfoTable
            PV_I = isequal(j.generateProbability, NaN) ? 0 : j.generateProbability
            ENTROPY = isequal(j.nodeEntropy, NaN) ? -1 : j.nodeEntropy
            sql = "INSERT INTO " * globalVar["timestamp"] * k * "IsDelete (DISEASE, PV_I, ENTROPY) VALUES ('" * i * "', " * string(PV_I) * ", " * string(ENTROPY) * ");"
            insertInto(sql)
        end
    end
end

# 刪除節點
function deleteNode(dn:: String)
    # 將節點設為忽略
    nodeInfoDict[dn].isIgnore = true
    # 刪除路徑
    deletePath(dn)
end

# 刪除路徑
function deletePath(dn:: String)
    # 刪除dn的所有源節點路徑
    for i in sourceDict[dn]
        i.isIgnore = true;
    end
    # 刪除源節點為dn的所有源節點路徑
    for i in values(sourceDict)
        for j in i
            if j.sourceNode == dn
                j.isIgnore = true;
            end
        end
    end

    # 檢查有沒有節點現在不存在來源
    # 不存在來源: 進入深度優先遞迴
    for (k, v) in sourceDict
        # 若 為起始點 或 為狀態為忽略之節點
        if k == globalVar["startPoint"] || nodeInfoDict[k].isIgnore
            continue
        end
        # 有沒有來源
        hasSource:: Bool = false
        for i in v
            if !i.isIgnore
                hasSource = true
                break
            end
        end
        # 若該節點沒有來源，進入深度優先遞迴
        if !hasSource
            deleteNode(k)
        end
    end
end

# 初始化
function initializeDict()
    # 初始化節點資訊字典中的value
    for i in values(nodeInfoDict)
        i.generateProbability = NaN
        i.nodeEntropy = NaN
        i.isIgnore = false
    end
    # 初始化源節點字典中value陣列內的所有SourceNodePathInfo
    for i in values(sourceDict)
        for j in i
            j.isIgnore = false
        end
    end
    # 設定起始點生成概率
    nodeInfoDict[globalVar["startPoint"]].generateProbability = 1
end

# 最短路徑分析
function shortestPathAnalysis()
    # 設定最短路徑時程
    globalVar["shortestPathTime"] = Inf
    # 設定目標節點
    globalVar["endPoint"] = "999999"

    # 路徑紀錄
    sp = Dict{String, Int64}()
    sp[globalVar["startPoint"]] = 1
    # 最短路徑深度優先
    shortestDfs(globalVar["startPoint"], 0.0, sp)
end

# 最短路徑深度優先
# 當前疾病、時間加總、路徑紀錄
function shortestDfs(disease:: String, sum:: Float64, sp:: Dict)
    # 如果已經找到目標節點且sum小於shortestPathTime
    if disease == globalVar["endPoint"] && globalVar["shortestPathTime"] > sum
        globalVar["shortestPathTime"] = sum
        globalVar["shortestPath"] = collect(sp)
        return
    end
    # 如果sum大於globalVar["shortestPathTime"]則不繼續計算
    if sum > globalVar["shortestPathTime"]
        return
    end
    # 跌代
    for i in graphStruct[disease]
        sp[i.to] = length(sp) + 1
        shortestDfs(i.to, sum + i.time, sp)
        delete!(sp, i.to)
    end
end