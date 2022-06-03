# 數據處理與生成
function dataProcessAndGenerate()
    # 開關檔程序(會自動關檔)
    open("./Input/ForImportantNodeAnalysis_OR6.txt") do file
        # 一次讀一行
        for line in eachline(file)
            # 字串分割
            arr = split(line, " ")

            # 源節點名稱
            sourceNode = arr[1]
            # 靶節點名稱
            targetNode = arr[2]
            # 比例
            proportion = arr[3]
            # 演進期程
            time = arr[4]

            # 生成節點資訊字典
            generateNodeInfoDict(sourceNode, targetNode)
            # 生成源節點字典
            generateSourceDict(sourceNode, targetNode, parse(Float64, proportion))
            # 生成圖
            generateGraphStruct(sourceNode, targetNode, time)
        end
    end
end

# 生成圖
function generateGraphStruct(sourceNode, targetNode, time)
    # 建立邊資訊結構
    edgeInfo = EdgeInfo(targetNode, parse(Float64, time))
    # 尋找圖結構中是否有sourceNode鍵值對
    # 有: 回傳其值(陣列)並push入新edgeInfo
    # 無: 新增sourceNode鍵值對並push入新edgeInfo
    push!(get!(graphStruct, sourceNode, []), edgeInfo)
end

# 生成源節點字典
function generateSourceDict(sourceNode, targetNode, proportion)
    # 建立源節點路徑資訊
    sourceNodePathInfo = SourceNodePathInfo(sourceNode, proportion, false)
    # 尋找源節點字典中是否有targetNode鍵值對
    # 有: 回傳其值並push入新sourceNodePathInfo
    # 無: 新增targetNode鍵值對並push入新sourceNodePathInfo
    push!(get!(sourceDict, targetNode, []), sourceNodePathInfo)
    # 確保生成概率為1的疾病也有被加入(糖尿病)
    if !haskey(sourceDict, sourceNode)
        sourceDict[sourceNode] = []
    end
end

# 生成節點資訊字典
function generateNodeInfoDict(nodeArr...)
    # 跌代
    for i in nodeArr
        # 不存在就新增
        if !haskey(nodeInfoDict, i)
            nodeInfoDict[i] = NodeInfo(NaN, NaN, NaN, false)
        end
    end
end