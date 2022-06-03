# ---------- INCLUDE ----------
include("FileProcess.jl")
include("InfoMgr.jl")
include("Analysis.jl")
include("DAO.jl")

# ---------- INITIALIZE ----------
function init()
    # ---------- CONFIG ----------
    # 目標疾病
    globalConfig["aimDesease"] = "999999"
    # 已患疾病，不包含999001，因其為起始點(生產前某一段時間開始)，並非疾病
    globalConfig["sufferFromDisease"] = ["617629"]
    # 分析的OR檔 (源節點 靶節點 總人數)
    # globalConfig["analysisDataFilePath"] = "./Input/AnalysisOddsRatio_4.txt"
    globalConfig["analysisDataFilePath"] = "./Input_hasNormalChildbirthNode/AnalysisOddsRatio_6.txt"
    # 分析的OR檔的所有路徑 (路徑)
    globalConfig["analysisDataPathwayFilePath"] = "./Input/PathwayForOR_6.txt"
    # ---------- VAR ----------
    # 當前關鍵路徑組
    globalVar["keyPathGroup"] = []
    # 當前關鍵路徑熵值
    globalVar["pathEntropy"] = Inf
    # 當前關鍵路徑上的人次數
    globalVar["numberOfTimes"] = 0
end
init()

# ---------- Main ----------
# 檔案讀取與資料實體化(建構分析用的核心數據)
fileReadAndDataInstantiate(globalConfig["analysisDataFilePath"])
# 建構OR所給定的路徑
constructionORpathway(globalConfig["analysisDataPathwayFilePath"])
# --------------------------
# 迭代分析所有已患疾病
iterationAnalysis()
# --------------------------
# 生成關鍵路徑資訊表
generateKeyPathwayTable(globalVar["disList"])
# 生成分析結果集合
generateAnalysisSet()
# 生成關鍵路徑屬性表
generateAttributeTable("./Output/EdgeAttributeTable.txt", analysisSet)
# 生成已患疾病屬性表
generateAttributeTable("./Output/NodeAttributeTable.txt", globalConfig["sufferFromDisease"])