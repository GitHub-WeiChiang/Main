# import XLSX 套件
import XLSX
# import JSON 套件
import JSON

# include 檔案生成器
include("./FileGenerator.jl")
# include 演算法
include("./Algorithm.jl")

# 主題
topic = "hf_20%_"
# 檔案位置
filePath = "D:/NtutMasterResearch/ntutmasterresearch/研究用程式/數據整理用/SortOutForPathCookie/Input/p_greater_or_equal_to_20%_hf_patient.xlsx"
# 讀取檔案
xf = XLSX.readxlsx(filePath)
# 讀取sheet
sh = xf[XLSX.sheetnames(xf)[1]]

# 起始列
# strRowArr = [2, 6, 18]
# 早產
# strRowArr = [2, 2, 2]
# 心衰
strRowArr = [2, 2]

# 最終列
# 早產
# endRowArr = [5, 17, 58]
# 心衰
# endRowArr = [26, 56]
# endRowArr = [9, 23]
endRowArr = [6, 17]

# 勝算比
oddsRatioArr = [5, 4]
# 目標代碼
prematureCode = "999999"

# 迭代所有勝算比
for index = 1:length(oddsRatioArr)
    # 圖字典
    # Key:: String = 源節點 (interacts with) 靶節點
    # Value:: Int64 = 人數
    graphDict = Dict{String, Int64}()

    # 路徑陣列
    pathwayArr = []

    # 迭代需要的資料
    for row = strRowArr[index]:endRowArr[index]
        # 路徑
        path:: String = sh[row, 1]
        # 未早產人數
        normal:: Int64 = sh[row, 2]
        # 早產人數
        premature:: Int64 = sh[row, 3]
        # 總人數
        total:: Int64 = normal + premature

        # 字串分割
        arr = split(path, " -1 ")
        # 移除陣列最後一個元素其多餘的空白
        arr[end] = replace(arr[end], " " => "")

        # 深度優先搜尋OR指定的路徑
        # 例:
        #   疾病軌跡為: ["1", "2", "3 4", "5"]
        #   需遞迴出:
        #       指定路徑1: ["1", "2", "3", "5"]
        #       指定路徑2: ["1", "2", "4", "5"]
        dfsPathway(arr, 1, [], pathwayArr)

        # 迭代該路徑
        for i in 1 : length(arr) - 1
            # 再分割，因為會有同時罹患多種疾病的可能
            sourceNodes = split(arr[i], " ")
            targetNodes = split(arr[i + 1], " ")
            # 匹配
            for sourceNode in sourceNodes
                for targetNode in targetNodes
                    key = sourceNode * " (interacts with) " * targetNode
                    # 若尚未到早產節點則累加總人數、若以到早產節點則累加早產人數
                    graphDict[key] = targetNode == prematureCode ? get!(graphDict, key, 0) + premature : get!(graphDict, key, 0) + total
                end
            end
        end
    end

    # 產生Cytoscape匯入檔(繪圖用) for cytoscape
    generateCytoscapeGraphFile(graphDict, "./Output/" * topic * "OddsRatio_" * string(oddsRatioArr[index]) * ".txt")
    # 產生Cytoscape匯入檔(顯示人數用) for cytoscape
    generateCytoscapeAttributeFile(graphDict, "./Output/" * topic * "OddsRatioAttributeTable_" * string(oddsRatioArr[index]) * ".txt")

    # 產生圖檔(分析用) for analysis
    generateAnalysisFile(graphDict, "./Output/" * topic * "AnalysisOddsRatio_" * string(oddsRatioArr[index]) * ".txt")
    # 產生路徑檔(分析會用到) for analysis
    generatePathwayFile(pathwayArr, "./Output/" * topic * "PathwayForOR_" * string(oddsRatioArr[index]) * ".txt")

    # 產生Json檔(網頁顯示用Cytoscape.js) for web
    generateCytoscapeJsJsonFile(graphDict, "./Output/" * topic * "OddsRatioJson_" * string(oddsRatioArr[index]) * ".json")
end