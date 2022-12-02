# 清空輸出檔
open("./Output/有環處.txt", "w") do file
end

# 早產
# 讀 OR4~6 檔案
for i = 4:6
# 心衰
# 讀 OR4~5 檔案
# for i = 4:5
    # 紀錄出現次數
    # key = 疾病演變順序
    # value = 記錄到的次數
    recordDict = Dict{String, Int64}()

    # 讀檔
    open("./Input/AnalysisOddsRatio_" * string(i) * ".txt") do file
        # 一次讀一行
        for line in eachline(file)
            # 字串分割
            arr = split(line, "\t")

            # 源節點名稱
            sourceNode = arr[1]
            # 靶節點名稱
            targetNode = arr[2]

            key1:: String = sourceNode * "_" * targetNode
            key2:: String = targetNode * "_" * sourceNode
            if haskey(recordDict, key1)
                recordDict[key1] = recordDict[key1] + 1
            elseif haskey(recordDict, key2)
                recordDict[key2] = recordDict[key2] + 1
            else
                recordDict[key1] = 1
            end
        end
    end

    open("./Output/有環處.txt", "a") do file
        println("------------------------------")
        write(file, "------------------------------\n")

        println("OR [" * string(i) * "] 的有環處:")
        write(file, "OR [" * string(i) * "] 的有環處:\n")

        for (key, value) in recordDict
            if value > 1
                println(key, " - ", value)
                str:: String = key * " - " * string(value) * "\n"
                write(file, str)
            end
        end

        println("------------------------------")
        write(file, "------------------------------\n")
    end
end