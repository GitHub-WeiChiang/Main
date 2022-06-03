# 建構OR所給定的路徑
function constructionORpathway(filePath:: String)
    # 開關檔程序(會自動關檔)
    open(filePath) do file
        # 一次讀一行
        for line in eachline(file)
            # 字串分割
            arr = split(line, " ")

            # 迭代每一條路徑並建構至newPathSetDict
            # 例: 999001 249259 401405 999999
            # 製作為以下路徑: 999001 249259 401405 999999、249259 401405 999999、401405 999999
            for i = 1:length(arr) - 1
                path = [arr[i]]
                for j = i + 1:length(arr)
                    push!(path, arr[j])
                end
                # 若無鍵值對，建立
                if !haskey(newPathSetDict, arr[i])
                    newPathSetDict[arr[i]] = Set()
                end
                push!(newPathSetDict[arr[i]], path)
            end
        end
    end
end

# 檔案讀取與資料實體化(分析用的核心數據)
function fileReadAndDataInstantiate(filePath:: String)
    # 開關檔程序(會自動關檔)
    open(filePath) do file
        # 一次讀一行
        for line in eachline(file)
            # 字串分割
            arr = split(line, "\t")

            # 源節點名稱
            sourceNode = arr[1]
            # 靶節點名稱
            targetNode = arr[2]
            # 數量
            amount = parse(Int64, arr[3])

            # 將靶節點放入源節點的NodeEdgeInfo結構中的
            nodeEdgeInfo = get!(graphDict, sourceNode, NodeEdgeInfo([], [], Dict{String, Float64}(), Dict{String, Float64}()))
            push!(nodeEdgeInfo.targetNodes, targetNode)
            nodeEdgeInfo.targetNodesAmounts[targetNode] = amount
            # 將源節點放入靶節點的NodeEdgeInfo結構中
            nodeEdgeInfo = get!(graphDict, targetNode, NodeEdgeInfo([], [], Dict{String, Float64}(), Dict{String, Float64}()))
            push!(nodeEdgeInfo.sourceNodes, sourceNode)
            nodeEdgeInfo.sourceNodesAmounts[sourceNode] = amount
        end
    end
end

# 生成分析結果集合(用於生成關鍵路徑屬性表)
function generateAnalysisSet()
    for i in globalVar["keyPathGroup"]
        for j = 2:length(i)
            str:: String = i[j - 1] * " (interacts with) " * i[j]
            push!(analysisSet, str)
        end
    end
end

# 生成屬性表(用於顯示關鍵路徑以及已患疾病)
# 檔名、屬性
function generateAttributeTable(fileName:: String, attribute:: Any)
    # 開關檔程序(會自動關檔)
    open(fileName, "w") do file
        # 寫入標頭
        write(file, "KEY\tBRIGHT\n")
        # 寫入屬性
        for i in attribute
            str = i * "\tTRUE\n"
            write(file, str)
        end
    end
end