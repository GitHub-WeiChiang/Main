# --------------------------------------------------

# 全局變數
# Key: 變數名
# value: 變數值

# globalGraphEntropy = 全局圖熵
# startPoint = 起始節點
# endPoint = 最後節點
# shortestPathTime = 最短時程
# shortestPath = 最短路徑
# timestamp = 時間戳

globalVar = Dict{String, Any}()

# --------------------------------------------------

# 邊資訊
mutable struct EdgeInfo
    # 靶節點
    to:: String
    # 時程
    time:: Float64
end

# 圖結構
# Key: String = 節點疾病名稱
# Value: EdgeInfo[] = 該疾病的所有可能演變疾病
graphStruct = Dict{String, Array}()

# --------------------------------------------------

# 節點資訊
mutable struct NodeInfo
    # 生成概率
    generateProbability:: Float64
    # 歸一化生成概率
    nGenerateProbability:: Float64
    # 節點熵值
    nodeEntropy:: Float64
    # 是否忽略
    isIgnore:: Bool
end

# 節點資訊字典
# Key: String = 節點疾病名稱
# Value: NodeInfo = 節點資訊結構
nodeInfoDict = Dict{String, Any}()

# --------------------------------------------------

# 源節點路徑資訊
mutable struct SourceNodePathInfo
    # 源節點
    sourceNode:: String
    # 比例
    proportion:: Float64
    # 是否忽略
    isIgnore:: Bool
end

# 源節點字典
# Key: String = 靶節點疾病名稱
# Value: SourceNodePathInfo[] = 該靶節點的所有源節點路徑資訊
sourceDict = Dict{String, Array}()

# --------------------------------------------------