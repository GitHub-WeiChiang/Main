# ---------- INCLUDE ----------
# 資訊管理
include("InfoMgr.jl")
# 檔案處理
include("DataProcess.jl")
# 計算器
include("Calculator.jl")
# 數據打印
include("DataPrinter.jl")
# 資料庫
include("DAOForSQLite.jl")
# 分析
include("Analysis.jl")

# ---------- 初始圖形分析 ----------
# 數據處理與生成
dataProcessAndGenerate()
# 建立本次作業結果資料表
createCurrentProcessResultTable()
# 尋找起始點
seekStartPoint()
# 生成概率計算
generateProbabilityCalc()
# 全局圖熵計算
globalGraphEntropyCalc()
# 打印分析結果
printAnalysisResult()
# 打印全局圖熵
printGlobalGraphEntropy()

# ---------- 逐一刪除節點分析 ----------
# 迭代分析
iterativeAnalysis()

# ---------- 最短時程路徑 ----------
# 最短路徑分析
# shortestPathAnalysis()
# 打印最短時程路徑
# printShortestTimePath()