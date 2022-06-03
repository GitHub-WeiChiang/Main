# 深度優先搜尋路徑
# 路徑、當前index、當前紀錄路徑、總路徑集合
function dfsPathway(arr:: Array, ind:: Int64, curPath:: Array, pathwayArr:: Array)
    # 若已經迭代到最後，儲存路徑並return
    if ind == length(arr) + 1
        push!(pathwayArr, collect(curPath))
        return
    end
    # 否則使用dfs繼續迭代路徑
    for i in split(arr[ind], " ")
        push!(curPath, i)
        dfsPathway(arr, ind + 1, curPath, pathwayArr)
        pop!(curPath)
    end
end