# 全局圖熵計算
function globalGraphEntropyCalc()
    # 全局圖熵
    globalVar["globalGraphEntropy"] = Float64(0)

    # 加總當前節點生成概率進行歸一化
    currentTotalP = Float64(0)
    for i in values(nodeInfoDict)
        # 若疾病為忽略狀態則忽略
        if i.isIgnore
            continue
        end
        currentTotalP = currentTotalP + i.generateProbability
    end
    
    # 跌代所有疾病
    for i in values(nodeInfoDict)
        # 若疾病為忽略狀態則忽略
        if i.isIgnore
            continue
        end
        # 紀錄歸一化生成概率
        i.nGenerateProbability = i.generateProbability / currentTotalP
        # 傳入生成概率計算熵值
        i.nodeEntropy = nodeEntropyCalc(i.nGenerateProbability)
        # 加總
        globalVar["globalGraphEntropy"] += i.nodeEntropy
    end
end

# 節點熵值計算
function nodeEntropyCalc(gp:: Float64):: Float64
    return gp * log10(1 / gp)
end

# 尋找起始點
function seekStartPoint()
    # 將起始點的生成概率設為1
    for (k, v) in sourceDict
        # 找到起始點
        if length(v) == 0
            # 設定生成概率
            nodeInfoDict[k].generateProbability = 1
            # 儲存起始點
            globalVar["startPoint"] = k
            break;
        end
    end
end

# 生成概率計算
function generateProbabilityCalc()
    # 生成概率計算
    for targetNode in keys(sourceDict)
        # 如果該節點 未忽略 且 尚未有生成概率，進入深度優先
        if !nodeInfoDict[targetNode].isIgnore && isequal(nodeInfoDict[targetNode].generateProbability, NaN)
            dfsForGpc(targetNode)
        end
    end
end

# 深度優先搜尋for生成概率計算
function dfsForGpc(targetNode)
    generateProbability:: Float64 = 0

    # 計算該點的生成概率
    # 跌代該點的所有源節點
    for sourceNodePathInfo in sourceDict[targetNode]
        # 若 該源節點資訊路徑為忽略狀態 或 該源節點為忽略狀態，則continue
        if sourceNodePathInfo.isIgnore || nodeInfoDict[sourceNodePathInfo.sourceNode].isIgnore
            continue
        end
        # 如果該源節點沒有生成概率，進入深度優先遞迴
        if isequal(nodeInfoDict[sourceNodePathInfo.sourceNode].generateProbability, NaN)
            dfsForGpc(sourceNodePathInfo.sourceNode)
        end
        # 加總生成概率
        generateProbability += nodeInfoDict[sourceNodePathInfo.sourceNode].generateProbability * sourceNodePathInfo.proportion
    end

    nodeInfoDict[targetNode].generateProbability = generateProbability
end