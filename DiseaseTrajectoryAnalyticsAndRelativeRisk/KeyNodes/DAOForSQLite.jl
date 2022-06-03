using SQLite
using DataFrames

import Dates

# 連接資料庫
db = SQLite.DB("AnalysisResultData.db")

# CREATE TABLE
function createTable(sql:: String)
    SQLite.execute!(db, sql)
end

# INSERT INTO
function insertInto(sql:: String)
    SQLite.execute!(db, sql)
end

# SELECT
function select(sql:: String):: DataFrame
    SQLite.Query(db, sql) |> DataFrame
end

# 建立本次作業結果資料表
function createCurrentProcessResultTable()
    # 抓取現在時間
    globalVar["timestamp"] = SubString(string(Dates.now()), 11, 19)
    globalVar["timestamp"] = replace(globalVar["timestamp"], "-" => "")
    globalVar["timestamp"] = replace(globalVar["timestamp"], ":" => "")
    globalVar["timestamp"] *= "_"
    # 建立原始圖資料表
    createTable("CREATE TABLE " * globalVar["timestamp"] * "OriginalInfoTable (DISEASE char(20) PRIMARY KEY, PV_I double, N_PV_I double, ENTROPY double);")
    # 建立分析結果資料表
    createTable("CREATE TABLE " * globalVar["timestamp"] * "AnalysisResultTable (DELETE_DISEASE char(20) PRIMARY KEY, E_I double, EN_I double, EFFECT_I)")
    # 建立刪除節點後子圖資訊資料表
    for i in keys(nodeInfoDict)
        sql = "CREATE TABLE " * globalVar["timestamp"] * i * "IsDelete (DISEASE char(20) PRIMARY KEY, PV_I double, ENTROPY double);"
        createTable(sql)
    end
    # 建立最短路徑資料表
    createTable("CREATE TABLE " * globalVar["timestamp"] * "ShortestPath (DISEASE char(20) PRIMARY KEY, NUMBER int);")
end