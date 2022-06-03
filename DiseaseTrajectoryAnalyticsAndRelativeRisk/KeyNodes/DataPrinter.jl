# 打印分析結果
function printAnalysisResult()
    # println("# ---------- 各疾病生成概率與熵值 ---------- #")

    for (k, v) in nodeInfoDict
        # println("疾病: ", k)
        # println("生成概率: ", v.generateProbability)
        # println("熵值: ", v.nodeEntropy, "\n")

        # INSERT INTO OriginalInfoTable
        sql = "INSERT INTO " * globalVar["timestamp"] * "OriginalInfoTable (DISEASE, PV_I, N_PV_I, ENTROPY) VALUES ('" * k * "', " * string(v.generateProbability) * ", " * string(v.nGenerateProbability) * ", " * string(v.nodeEntropy) * ");"
        insertInto(sql)
    end
end

# 打印全局圖熵
function printGlobalGraphEntropy()
    # println("# ---------- 全局圖熵 ---------- #")
    # println("全局圖熵: ", globalVar["globalGraphEntropy"], "\n")
end

# 打印最短時程路徑
function printShortestTimePath()
    # println("# ---------- 最短時程/路徑 ---------- #")
    # println("最短時程: ", globalVar["shortestPathTime"])
    # println("最短路徑: ", globalVar["shortestPath"])

    # INSERT INTO ShortestPath
    for (k, v) in globalVar["shortestPath"]
        sql = "INSERT INTO " * globalVar["timestamp"] * "ShortestPath (DISEASE, NUMBER) VALUES ('" * k * "', " * string(v) * ");"
        insertInto(sql)
    end
end