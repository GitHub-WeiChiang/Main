# --------------------------------------------------
# 新路徑集合字典 (所有可能成為關鍵路徑之路徑) ***使用OR指定路徑建構
# Key:: String = 疾病名稱
# Value:: Set = 路徑集合
# Value Array e.g. = [[路徑1], [路徑2], ...]
newPathSetDict = Dict{String, Set{Array{String}}}()
# --------------------------------------------------
# 路徑集合字典 (所有可能成為關鍵路徑之路徑) ***使用深度優先搜尋產生
# Key:: String = 疾病名稱
# Value:: Array = 所有路徑
# Value Array e.g. = [[路徑1], [路徑2], ...]
# pathSetDict = Dict{String, Array{Array{String}}}()
# --------------------------------------------------
# 節點資訊
mutable struct NodeInfo
    piv:: Float64
    pov:: Float64
    entropy:: Float64
end
# --------------------------------------------------
# 分析結果集合
# Value = 路徑
# e.g. = DiseaseA  (interacts with) DiseaseB
analysisSet = Set{String}()
# --------------------------------------------------
#=
全局組態
aimDesease = 目標疾病:: Stirng
sufferFromDisease = 已患疾病:: Array
=#
globalConfig = Dict{String, Any}()
# --------------------------------------------------
#=
全局變數
keyPathGroup = 當前關鍵路徑組
pathEntropy = 當前關鍵路徑熵值
numberOfTimes = 當前關鍵路徑上的人次數
=#
globalVar = Dict{String, Any}()
# --------------------------------------------------
# 節點邊資訊
mutable struct NodeEdgeInfo
    # 該節點的所有源節點
    sourceNodes:: Array{String}
    # 該節點的所有靶節點
    targetNodes:: Array{String}
    # 該節點連接到各個源節點的邊權重(次數)
    sourceNodesAmounts:: Dict{String, Int64}
    # 該節點連接到各個靶節點的邊權重(次數)
    targetNodesAmounts:: Dict{String, Int64}
end
# 圖字典
# key = 節點名稱
# Value = NodeEdgeInfo
graphDict = Dict{String, NodeEdgeInfo}()
# --------------------------------------------------