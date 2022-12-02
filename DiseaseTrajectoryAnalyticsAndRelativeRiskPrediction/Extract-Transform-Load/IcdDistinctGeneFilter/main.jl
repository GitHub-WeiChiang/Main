icdSet = Set{Int64}()
open("./input/ICD_distinct_Gene.txt") do file
    for line in eachline(file)
        result = findfirst(".html", line)
        if result != nothing
            icd = SubString(line, result[1] - 3, result[1] - 1)
            push!(icdSet, parse(Int64, icd))
        end
    end
end

for order in 4:6
    icdSetForCytoscape = Set{String}()
    open("./input/PathwayForOR_" * string(order) * ".txt") do file
        for line in eachline(file)
            arr = split(line, " ")
            for icdRange in arr
                if(icdRange == "999001" || icdRange == "999999")
                    continue
                end
                icdString = icdRange
                if(length(icdString) == 5)
                    icdString = "0" * icdString
                end
                minIcd::Int64 = parse(Int64, icdString[1:3])
                maxIcd::Int64 = parse(Int64, icdString[4:6])
                for icd in minIcd:maxIcd
                    if icd in icdSet
                        push!(icdSetForCytoscape, icdRange)
                    end
                end
            end
        end
    end
    open("./output/ICD_distinct_Gene_Attribute_OR" * string(order) * ".txt", "w") do file
        write(file, "KEY\tDISTINCT\n")
        for i in icdSetForCytoscape
            write(file, i * "\tTRUE\n")
        end
    end
end