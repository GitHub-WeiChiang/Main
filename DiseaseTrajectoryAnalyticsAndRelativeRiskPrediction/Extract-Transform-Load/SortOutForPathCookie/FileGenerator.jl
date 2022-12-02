# 產生路徑檔(分析會用到)
function generatePathwayFile(pathwayArr:: Array, fileName:: String)
    # 開關檔程序(會自動關檔)
    open(fileName, "w") do file
        # 寫入
        for i in pathwayArr
            pathway = ""
            for j in i
                pathway *= j * " "
            end
            write(file, pathway[1:end-1] * "\n")
        end
    end
end

# 產生圖檔(分析用)
# 圖字典、檔名
function generateAnalysisFile(graphDict:: Dict{String, Int64}, fileName:: String)
    # 開關檔程序(會自動關檔)
    open(fileName, "w") do file
        # 寫入
        for (i, j) in graphDict
            edgeStr = i * "\t" * string(j) * "\n"
            edgeStr = replace(edgeStr, " (interacts with) " => "\t")
            write(file, edgeStr)
        end
    end
end

# 產生Cytoscape匯入檔(顯示人數用)
# 圖字典、檔名
function generateCytoscapeAttributeFile(graphDict:: Dict{String, Int64}, fileName:: String)
    # 開關檔程序(會自動關檔)
    open(fileName, "w") do file
        # 寫入標頭
        write(file, "Key\tAmount\n")
        # 寫入
        for (i, j) in graphDict
            edgeStr = i * "\t" * string(j) * "\n"
            write(file, edgeStr)
        end
    end
end

# 產生Cytoscape匯入檔(繪圖用)
# 圖字典、檔名
function generateCytoscapeGraphFile(graphDict:: Dict{String, Int64}, fileName:: String)
    # 開關檔程序(會自動關檔)
    open(fileName, "w") do file
        # 寫入標頭
        write(file, "SourceNode\tTargetNode\n")
        # 寫入
        for i in keys(graphDict)
            edgeStr = replace(i, " (interacts with) " => "\t")
            edgeStr *= "\n"
            write(file, edgeStr)
        end
    end
end

# 產生圖Json(網頁Cytoscape.js用)
# 圖字典、檔名
function generateCytoscapeJsJsonFile(graphDict:: Dict{String, Int64}, fileName:: String)
    data = Dict("Info" => [])
    
    for (i, j) in graphDict
        sourceNode = split(i," (interacts with) ")[1]
        targetNode = split(i," (interacts with) ")[2]
        numOfPeople = j

        push!(data["Info"], Dict("sourceNode"=>sourceNode, "targetNode"=>targetNode, "numOfPeople"=>numOfPeople))
    end

    open(fileName, "w") do file
        JSON.print(file, data)
    end
end