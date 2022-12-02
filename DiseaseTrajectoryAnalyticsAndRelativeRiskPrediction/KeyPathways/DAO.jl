using SQLite
using DataFrames

import Dates

# 連接資料庫
db = SQLite.DB("AnalysisResult.db")

# 時間戳
timestamp = SubString(string(Dates.now()), 11, 19)
timestamp = replace(string(timestamp), "-" => "")
timestamp = replace(timestamp, ":" => "")
timestamp *= "_"

# 生成關鍵路徑資訊表
function generateKeyPathwayTable(disList)
    # table name
    keyPathwayInfo:: String = timestamp * "KeyPathwayInfo"

    # CREATE TABLE
    sql_1:: String = "CREATE TABLE " * keyPathwayInfo * " (DISEASE char(20) PRIMARY KEY, PIV double, POV double, ENTROPY double);"
    SQLite.execute!(db, sql_1)

    # INSERT INTO
    for (k, v) in disList
        sql_2:: String = "INSERT INTO " * keyPathwayInfo * " (DISEASE, PIV, POV, ENTROPY) VALUES ('" * k * "', " * string(v.piv) * ", " * string(v.pov) * ", " * string(v.entropy) * ");"
        SQLite.execute!(db, sql_2)
    end
end

# INSERT All Path Analysis Result
function insertIntoEachPathwayAnalysisResult(pathway:: String, graphEntropy:: Float64)
    # table name
    allAnalysis:: String = timestamp * "AllAnalysis"

    # INSERT INTO
    sql:: String = "INSERT INTO " * allAnalysis * " (PATHWAY, GRAPHENTROPY) VALUES ('" * pathway * "', " * string(graphEntropy) * ");"
    SQLite.execute!(db, sql)
end

# 生成所分析的所有關鍵路徑表
function generateAllAnalysisPathTable()
    # table name
    allAnalysis:: String = timestamp * "AllAnalysis"

    # CREATE TABLE
    sql:: String = "CREATE TABLE " * allAnalysis * " (PATHWAY char(100) PRIMARY KEY, GRAPHENTROPY double);"
    SQLite.execute!(db, sql)
end
generateAllAnalysisPathTable()