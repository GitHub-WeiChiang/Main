# import XLSX 套件
import XLSX

# --------------------------------------------------

# ----------------------------------
# ----- 現在要分析的 OR 記得要改 -----
# ----------------------------------

# OR
oddsRatio = "4"

# --------------------------------------------------

# 靶節點資訊
mutable struct TargetInfo
    # 靶節點
    targetNode:: String
    # 次數
    count:: Float64
    # 機率
    probability:: Float64
end

# 靶節點資訊字典
# key = 節點名稱
# value = 該節點的靶節點資訊陣列
targetInfoDict = Dict{String, Array{TargetInfo}}()

# --------------------------------------------------

# 源節點資訊字典
# key = 節點名稱
# value = 該節點的源節點陣列
sourceInfoDict = Dict{String, Array{String}}()

# --------------------------------------------------

# 節點總次數字典
# key = 節點名稱
# value = 該節點的患病計數
nodeCountDict = Dict{String, Float64}()

# --------------------------------------------------

# 次數與時程
mutable struct CountAndTime
    count:: Float64
    time:: Float64
end

# 時程紀錄字典
# key = 路徑
# value:: Array{CountAndTime} = 所有的次數與時程
timeRecordDict = Dict{String, Array{CountAndTime}}()

# --------------------------------------------------

# 紀錄屬於當前OR的路徑
currentOrPath = Set{String}()

# --------------------------------------------------

# 最短時程路徑
mutable struct ShortestPath
    path:: String
    time:: Float64
    sup:: Int64
end

shortestPath = ShortestPath("", Inf, 0)

# --------------------------------------------------

open("./Input/AnalysisOddsRatio_" * oddsRatio * ".txt") do file
    # 一次讀一行
    for line in eachline(file)
        # 字串分割
        arr = split(line, "\t")

        # 源節點名稱
        sourceNode = arr[1]
        # 靶節點名稱
        targetNode = arr[2]
        # 次數
        count = arr[3]

        # 實體化靶節點資訊
        targetInfo = TargetInfo(targetNode, parse(Float64, count), 0)
        # 放入靶節點資訊字典
        push!(get!(targetInfoDict, sourceNode, []), targetInfo)

        # 建立源節點資訊字典
        push!(get!(sourceInfoDict, targetNode, []), sourceNode)

        # 建立節點總次數字典
        if !haskey(nodeCountDict, sourceNode)
            nodeCountDict[sourceNode] = 0
        end
        if !haskey(nodeCountDict, targetNode)
            nodeCountDict[targetNode] = 0
        end
    end
end

for node in keys(nodeCountDict)
    # 如果不是起始點，該點的總次數為所有從源節點來的數量總和
    if node != "999001"
        for sourceNode in sourceInfoDict[node]
            for targetInfo in targetInfoDict[sourceNode]
                if targetInfo.targetNode == node
                    nodeCountDict[node] += targetInfo.count
                end
            end
        end
    # 如果是起始點，該點的總次數為所有前往靶節點的數量總和
    else
        for targetInfo in targetInfoDict[node]
            nodeCountDict[node] += targetInfo.count
        end
    end
end

# --------------------------------------------------

# 檔案位置
filePath = "D:/NtutMasterResearch/ntutmasterresearch/研究用程式/數據整理用/TransformCountToProbabilityAndCalculateTheSchedule/Input/path_cookie_remove_cycle.xlsx"
# 讀取檔案
xf = XLSX.readxlsx(filePath)
# 讀取sheet
sh = xf[XLSX.sheetnames(xf)[1]]
# 起始列
strRowArr = [2, 2, 2]
# 最終列
endRowArr = [5, 12, 47]
# 早產代碼
prematureCode = "999999"

# 迭代需要的資料
for row = strRowArr[7 - parse(Int64, oddsRatio)]:endRowArr[7 - parse(Int64, oddsRatio)]
    # 路徑
    path:: String = sh[row, 1]
    # 紀錄
    push!(currentOrPath, path) 
end

open("./Input/P_time_data_list.txt") do file
    # 一次讀一行
    for line in eachline(file)
        hashtagInd:: Int64 = findfirst("#", line)[1]
        path:: String = SubString(line, 1, hashtagInd - 1)

        # 判斷路徑OR值是否屬於本次指定值
        if !in(path, currentOrPath)
            continue
        end

        # 次數
        sup:: Float64 = 0
        commaInd:: Int64 = findfirst(",", line)[1]
        supStr:: String = SubString(line, hashtagInd, commaInd - 2)
        sup = parse(Int64, split(supStr, " ")[2])
        
        # 移除路徑最後的空白
        path = SubString(path, 1, length(path) - 1)
        # 拆解
        pathArr = split(path, "-1")
        
        # 抓取演變時程陣列
        scheduleStr:: String = SubString(line, findfirst("[", line)[1] + 1, length(line) - 2)
        # 拆解
        scheduleArr = split(scheduleStr, " ")

        # 匹配演變時程
        for i in 1 : length(pathArr) - 1
            # 再分割，因為會有同時罹患多種疾病的可能
            sourceNodes = split(pathArr[i], " ")
            targetNodes = split(pathArr[i + 1], " ")
            # 匹配
            for sourceNode in sourceNodes
                for targetNode in targetNodes
                    edge:: String = sourceNode * " " * targetNode
                    countAndTime:: CountAndTime = CountAndTime(sup, parse(Float64, scheduleArr[i]))

                    push!(get!(timeRecordDict, edge, []), countAndTime)
                end
            end
        end

        # 搜尋最短時程路徑
        evolutionTime = 0
        for i in scheduleArr
            evolutionTime = evolutionTime + parse(Float64, i)
        end
        if evolutionTime < shortestPath.time
            shortestPath.time = evolutionTime
            shortestPath.path = path
            shortestPath.sup = sup
        end
    end
end

# --------------------------------------------------

open("./Output/ForImportantNodeAnalysis_OR" * oddsRatio * ".txt", "w") do file
    for (sourceNode, targetInfoArray) in targetInfoDict
        for targetInfo in targetInfoArray
            targetInfo.probability = targetInfo.count / nodeCountDict[sourceNode]

            edge:: String = sourceNode * " " * targetInfo.targetNode
            totalCount:: Float64 = 0
            totalTime:: Float64 = 0
            for countAndTime in timeRecordDict[edge]
                totalCount = totalCount + countAndTime.count
                totalTime = totalTime + countAndTime.count * countAndTime.time
            end

            averageTime:: Float64 = totalTime / totalCount

            str = sourceNode * " " * targetInfo.targetNode * " " * string(targetInfo.probability) * " " * string(averageTime) * "\n"
            write(file, str)
        end
    end
end

open("./Output/ShortestPath_OR" * oddsRatio * ".txt", "w") do file
    write(file, string(shortestPath.path) * "\n")
    write(file, string(shortestPath.time) * "\n")
    write(file, string(shortestPath.sup) * "\n")
end

open("./Output/NodeSizeNumFromSupOnNode_OR" * oddsRatio * ".txt", "w") do file
    for (disease, sup) in nodeCountDict
        write(file, string(disease) * "\t" * string(sup) * "\n")
    end
end