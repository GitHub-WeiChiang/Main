狀況題
=====

可以每個專案設定不同的作者嗎 ?
-----
* ### git config --local user.name "ChiangWei"
* ### git config --local user.email "albert0425369@gmail.com"

如果在 git add 之後又修改了那個檔案的內容 ?
-----
* ### 再次使用 git add abc.txt

我想要找某個人或某些人的 Commit...
-----
* ### git log --oneline --author="ChiangWei"
* ### git log --oneline --author="ChiangWei\|Albert"

我想要找 Commit 訊息裡面有在罵髒話的...
-----
* ### git log --oneline --grep="wtf"

我要怎麼找到哪些 Commit 的檔案內容有提到 "Ruby" 這個字 ?
-----
* ### git log -S "Ruby"

主管: 「你再混嘛!我看看你今天早上 Commit 了甚麼!」(及從 2017 年 1 月之後，每天早上 9 點到 12 點的 Commit)
-----
* ### git log --oneline --since="9am" --until="12am"
* ### git log --oneline --since="9am" --until="12am" --after="2017-01"
* ### SOURCETREE -> WORKSPACE -> Search



Reference
=====
### * 為你自己學 Git
