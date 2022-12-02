# 迭代分析所有已患疾病
function iterationAnalysis()
    # # 產出pathSetDict
    # # 迭代已患疾病
    # for disease in globalConfig["sufferFromDisease"]
    #     # 深度優先搜尋找出該疾病所有可能成為關鍵路徑之路徑
    #     dfsAllPath(disease, disease, push!([], disease))
    # end

    # 遞迴路徑匹配
    recursivePathMach(1, [])
end

# 遞迴路徑匹配
# 已患疾病陣列索引、關鍵路徑紀錄
function recursivePathMach(ind:: Int64, pathRecord:: Array)
    # 舊的
    # for i in pathSetDict[globalConfig["sufferFromDisease"][ind]]
    # 新的
    for i in newPathSetDict[globalConfig["sufferFromDisease"][ind]]
        push!(pathRecord, i)

        # 若已經是最後一個疾病
        if ind == length(globalConfig["sufferFromDisease"])
            # 製作疾病列(路徑上的所有疾病)
            pathWayDisease = Set{String}()
            for i in pathRecord
                for j in i
                    push!(pathWayDisease, j)
                end
            end
            # 製作圖疾病資訊列(全圖的疾病節點)
            disList = Dict{String, NodeInfo}()
            for i in keys(graphDict)
                # 因999001為一起始點而非疾病，故不可將其熵值加總至全圖熵，也無須計算期熵值
                if i == "999001"
                    continue
                end

                get!(disList, i, NodeInfo(NaN, NaN, NaN))
            end

            # println("路徑上的疾病: ", pathWayDisease)
            # println("路徑紀錄", pathRecord)

            pathEntropyAnalysis(pathRecord, disList, pathWayDisease)
        else
            # 進入遞迴
            recursivePathMach(ind + 1, pathRecord)
        end

        pop!(pathRecord)
    end
end

# 路徑熵分析
# 關鍵路徑紀錄、圖疾病資訊列(全圖)、路徑上的所有疾病
function pathEntropyAnalysis(pathRecord:: Array, disList:: Dict{String, NodeInfo}, pathWayDisease:: Set{String})
    # 圖熵
    graphEntropy:: Float64 = 0

    # 迭代圖上所有節點
    for i in keys(disList)
        # 分析節點
        disList[i].piv, disList[i].pov, disList[i].entropy = nodeAnalysis(i, pathWayDisease, pathRecord)
        disList[i].entropy = isequal(disList[i].entropy, NaN) ? 0 : disList[i].entropy
        # 加總熵值
        graphEntropy += disList[i].entropy
        # 若熵值大於目前記錄，跳出函數，不用再計算
        # if graphEntropy > globalVar["pathEntropy"]
        #     return
        # end
    end

    # println("當前熵值: ", graphEntropy)
    # println("當前路徑: ", pathRecord)
    # println("疾病資訊: ", disList)

    # record each analysis result
    insertIntoEachPathwayAnalysisResult(string(pathRecord), graphEntropy)

    # 若熵值小於目前記錄，表示出現新的關鍵路徑
    if graphEntropy < globalVar["pathEntropy"]
        # 更新關鍵路徑紀錄
        globalVar["keyPathGroup"] = collect(pathRecord)
        # 更新圖熵值
        globalVar["pathEntropy"] = graphEntropy
        # 更新關鍵路徑上所有疾病資訊列
        globalVar["disList"] = collect(disList)
        # 更新關鍵路徑上的人次數
        globalVar["numberOfTimes"] = numberOfTimesCalculate(pathRecord)

        # println("當前熵值: ", graphEntropy)
        # println("當前路徑: ", pathRecord)
        # println("疾病資訊: ", disList)
    # 若熵值相同
    elseif graphEntropy == globalVar["pathEntropy"]
        # 當前關鍵路徑的人次數
        numberOfTimes:: Int64 = numberOfTimesCalculate(pathRecord)
        # 選擇路徑上人次數最多的那條
        if numberOfTimes > globalVar["numberOfTimes"]
            # 更新關鍵路徑紀錄
            globalVar["keyPathGroup"] = collect(pathRecord)
            # 更新圖熵值
            globalVar["pathEntropy"] = graphEntropy
            # 更新關鍵路徑上所有疾病資訊列
            globalVar["disList"] = collect(disList)
            # 更新關鍵路徑上的人次數
            globalVar["numberOfTimes"] = numberOfTimes
        end

        # println("當前熵值: ", graphEntropy)
        # println("當前路徑: ", pathRecord)
        # println("疾病資訊: ", disList)
    end
end

# 計算路徑上人次數
# 關鍵路徑
function numberOfTimesCalculate(keyPathGroup:: Array):: Int64
    count:: Int64 = 0

    # 避免重覆計算相同路徑
    recordSet = Set{String}()

    # 迭代關路徑組
    for i in keyPathGroup
        for j = 1 : length(i) - 1
            record:: String = join([i[j], i[j + 1]])
            # 若已加總過此次數，continue
            if record in recordSet
                continue
            # 若尚未加總此次數，紀錄並加總
            else
                push!(recordSet, record)
                count += graphDict[i[j]].targetNodesAmounts[i[j + 1]]
            end
        end
    end
    
    return count
end

# 分析節點
# 分析節點、路徑上的所有疾病、關鍵路徑紀錄
function nodeAnalysis(dis:: String, pathWayDisease:: Set{String}, pathRecord:: Array)
    # 節點總連結數
    totalLinks:: Int64 = 0
    for amount in values(graphDict[dis].sourceNodesAmounts)
        totalLinks += amount
    end
    for amount in values(graphDict[dis].targetNodesAmounts)
        totalLinks += amount
    end
    # 內連結數
    innerLinks:: Int64 = 0
    # 外連結數
    outerLinks:: Int64 = 0

    # 若當前疾病在圈圈內
    if in(dis, pathWayDisease)
        # 迭代此節點所有源節點連結
        for sourceNode in graphDict[dis].sourceNodes
            # 此路徑是否為內鏈路徑
            isInner:: Bool = false
            # 比對是否在路徑中
            for i in pathRecord
                # 尋找關鍵路徑中是否有此節點
                sourceNodeIndex = findfirst(isequal(sourceNode), i)
                # 沒有則continue
                if sourceNodeIndex === nothing
                    continue
                end
                # 比對下一個節點是否為dis，防止圈圈範圍誤判
                # 因為圖可能為有像有循環圖
                # 例: A <=> B -> c，關鍵路徑為A->B->C，判斷A節點時，B為A的源節點，B也在路徑上，但B->A為outerLinks，A->B才是innerLinks
                if sourceNodeIndex + 1 <= length(i) && i[sourceNodeIndex + 1] == dis
                    isInner = true
                    break
                end
            end
            isInner ? innerLinks += graphDict[dis].sourceNodesAmounts[sourceNode] : outerLinks += graphDict[dis].sourceNodesAmounts[sourceNode]
        end
        # 迭代此節點所有靶節點連結
        for targetNode in graphDict[dis].targetNodes
            # 此路徑是否為內鏈路徑
            isInner:: Bool = false
            # 比對是否在路徑中
            for i in pathRecord
                # 尋找關鍵路徑中是否有此節點
                targetNodeIndex = findfirst(isequal(targetNode), i)
                # 沒有則continue
                if targetNodeIndex === nothing
                    continue
                end
                # 比對上一個節點是否為dis，防止圈圈範圍誤判
                # 因為圖可能為有像有循環圖
                # 例: A <=> B -> c，關鍵路徑為A->B->C，判斷A節點時，B為A的源節點，B也在路徑上，但B->A為outerLinks，A->B才是innerLinks
                if targetNodeIndex - 1 > 0 && i[targetNodeIndex - 1] == dis
                    isInner = true
                    break
                end
            end
            isInner ? innerLinks += graphDict[dis].targetNodesAmounts[targetNode] : outerLinks += graphDict[dis].targetNodesAmounts[targetNode]
        end
    # 若當前疾病在圈圈外
    else
        # 迭代此節點所有源節點連結
        for i in graphDict[dis].sourceNodes
            in(i, pathWayDisease) ? innerLinks += graphDict[dis].sourceNodesAmounts[i] : outerLinks += graphDict[dis].sourceNodesAmounts[i]
        end
        # 迭代此節點所有靶節點連結
        for i in graphDict[dis].targetNodes
            in(i, pathWayDisease) ? innerLinks += graphDict[dis].targetNodesAmounts[i] : outerLinks += graphDict[dis].targetNodesAmounts[i]
        end
    end

    # 內連機率
    piv:: Float64 = innerLinks / totalLinks
    # 外連機率
    pov:: Float64 = outerLinks / totalLinks
    # 節點熵值
    entropy:: Float64 = entropyCalculator(piv, pov)

    return piv, pov, entropy
end

# 熵值計算
function entropyCalculator(piv:: Float64, pov:: Float64):: Float64
    return -piv * log2(piv) - pov * log2(pov)
end

# 深度優先搜尋找出該疾病所有可能成為關鍵路徑之路徑
# 起始疾病、當前疾病、路徑紀錄
# function dfsAllPath(startDis:: String, currentDis:: String, pathRecord:: Array)
#     # 若到達目標節點
#     if currentDis == globalConfig["aimDesease"]
#         # 若無鍵值對，建立
#         if !haskey(pathSetDict, startDis)
#             pathSetDict[startDis] = []
#         end
#         # 放入路徑
#         push!(pathSetDict[startDis], collect(pathRecord))
#     end
#     # 跌代該疾病所有目標節點
#     for i in graphDict[currentDis].targetNodes
#         # 將疾病放入路徑中
#         push!(pathRecord, i)
#         # DFS
#         dfsAllPath(startDis, i, pathRecord)
#         # 將疾病移除
#         pop!(pathRecord)
#     end
# end