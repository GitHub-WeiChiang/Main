# import XLSX 套件
import XLSX

# 檔案位置
filePath = "D:/風險係數分析/correct/PretermBirth/Input/path_cookie_remove_cycle.xlsx"
# 讀取檔案
xf = XLSX.readxlsx(filePath)
# 讀取sheet
sh = xf[XLSX.sheetnames(xf)[1]]

# 起始列
strRowArr = 2
# 最終列
endRowArr = 47
# 總正常生產人數
totalNormal = 111163
# 總早產人數
totalPreterm = 5755
# 總人數
total = totalNormal + totalPreterm

# 疾病紀錄表
diseaseList = []

# 迭代
for line = strRowArr:endRowArr
    # 路徑
    path:: String = sh[line, 1]
    # 去頭去尾
    path = path[11:findfirst(" -1 999999 ", path)[1] - 1]
    # 分割
    diseaseArr = split(path, " -1 ")
    # 迭代
    for i in diseaseArr
        # 分割
        diseaseCodeArr = split(i, " ")
        # 迭代
        for j in diseaseCodeArr
            if j ∉ diseaseList
                push!(diseaseList, string(j))
            end
        end
    end
end

push!(diseaseList, "path absolute risk")
push!(diseaseList, "non-path absolute risk")
push!(diseaseList, "path relative risk")

XLSX.openxlsx("./Output/PretermBirth_RapidMiner.xlsx", mode = "w") do xf
    sheet = xf[1]
    XLSX.rename!(sheet, "new_sheet")
    col:: String = "A"
    row:: Int64 = 1
    sheet[string(col, row)] = diseaseList

    # 迭代
    for line = strRowArr:endRowArr
        row = row + 1

        # 紀錄
        list = []

        # 路徑
        path:: String = sh[line, 1]
        # 去頭去尾
        path = path[11:findfirst(" -1 999999 ", path)[1] - 1]
        # 分割
        diseaseArr = split(path, " -1 ")
        # 迭代
        for i in diseaseArr
            # 分割
            diseaseCodeArr = split(i, " ")
            # 迭代
            for j in diseaseCodeArr
                push!(list, j)
            end
        end

        # 結果
        ans = []
        #
        reverse = []

        for i = 1:length(diseaseList) - 3
            #
            push!(reverse, false)

            if diseaseList[i] ∈ list
                push!(ans, true)
            else
                push!(ans, false)
            end
        end
        
        n:: Float64 = sh[line, 2]
        p:: Float64 = sh[line, 3]

        pasp:: Float64 = p / (n + p)
        npasp:: Float64 = (totalPreterm - p) / (total - (n + p))
        rsr:: Float64 = pasp / npasp

        push!(ans, string(pasp))
        push!(ans, string(npasp))
        push!(ans, string(rsr))

        sheet[string(col, row)] = ans

        #
        r_pasp:: Float64 = (totalPreterm - p) / (total - (n + p))
        r_npasp:: Float64 = p / (n + p)
        r_rsr:: Float64 = r_pasp / r_npasp
        #
        push!(reverse, string(r_pasp))
        push!(reverse, string(r_npasp))
        push!(reverse, string(r_rsr))
        #
        row = row + 1
        sheet[string(col, row)] = reverse
    end
end