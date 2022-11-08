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

如何在 Git 裡刪除檔案或變更檔名 ?
-----
* ### rm welcome.html, git add welcome.html
* ### git rm welcome.html
* ### SOURCETREE -> WORKSPACE -> File Status -> file(右鍵) -> Remove
* ### mv hello.html world.html, git status, git add --all
* ### git mv welcome.html

修改 Commit 紀錄
-----
* ### git commit --amend -m "Welcome To Facebook"
* ### SOURCETREE -> WORKSPACE -> File Status Bottom (Commit) -> Commit Options -> Amend last commit

追加檔案到最近一次的 Commit
-----
* ### git status, git add newFile.html, git commit --amend --no-edit
* ### SOURCETREE -> WORKSPACE -> File Status Bottom (Commit) -> Commit Options -> Amend last commit

新增目錄 ?
-----
* ### touch images/.keep

有些檔案我不想放在 Git 裡面... (若檔案先前已存在，透過 git rm --cached 強制清除，或透過 SOURCETREE -> File Status Bottom (Commit) -> Stop Tracking，最後 add 並 commit)
-----
* ### touch .gitignore

檢視特定檔案的 Commit 紀錄
-----
* ### git log welcome.html
* ### git log -p welcome.html
* ### SOURCETREE -> WORKSPACE -> File Status -> file(右鍵) -> Log Selected...

等等，這行程式誰寫的 ?
-----
* ### git blame index.html
* ### git blame -L 5,10 index.html
* ### SOURCETREE -> WORKSPACE -> File Status -> file(右鍵) -> Annotate Selected...

啊 ! 不小心把檔案或目錄刪掉了...
-----
* ### git checkout abc.txt
* ### git checkout .
* ### SOURCETREE -> WORKSPACE -> File Status -> file(右鍵) -> Discard
* ### git checkout HEAD~2 welcome.html
* ### git checkout HEAD~2 .

剛才的 Commit 後悔了，想要拆掉重做...
-----
* ### git reset e12d8ef^
* ### git reset e12d8ef^^
* ### git reset e12d8ef^^^^^
* ### git reset e12d8ef~5
* ### git reset master^
* ### git reset HEAD^
* ### git reset 85e7e30
* ### 備註: Commit 拆出來的檔案 -> --mixed 丟回工作目錄、soft 丟回站存區、hard 直接丟掉。
* ### SOURCETREE -> WORKSPACE -> History -> commit -> reset current branch to this commit

不小心使用 hard 模式 Rest 了某個 Commit，救得回來嗎 ?
-----
* ### git reflog, git reset e12d8ef --hard

可以只 Commit 一個檔案的部分內容嗎 ?
-----
* ### git add -p index.html
* ### SOURCETREE -> WORKSPACE -> File Status -> select file -> select line -> Stage lines

為甚麼我的分支都沒有「小耳朵」 ?
-----
* ### git merge cat --no--ff
* ### SOURCETREE -> WORKSPACE -> BRANCHES -> merge -> Create a new commit even if fast-forward is possible

不小心把還沒合併的分支砍掉了，救得回來嗎 ?
-----
* ### git branch newBranceName b174a5a
* ### SOURCETREE -> Branch -> check Specified commit
* ### 備註: git reflog

怎麼取消 rebase ?
-----
* ### git reflog, git rest b174a5a --hard
* ### git rest ORIG_HEAD --hard

我可以從過去的某個 Commit 再長一個新的分支出來嗎 ?
-----
* ### git branch branchName 657fce
* ### git checkout -b branchName 657fce
* ### SOURCETREE -> WORKSPACE -> History -> select commit (Right-click) -> Branch...

修改歷史訊息
-----
* ### git rebase -i bb0c9c2, replace "pick" to "r"
* ### SOURCETREE -> WORKSPACE -> History -> select commit (Right-click) -> Rebase children of bb0c9c2 interactively... -> Description (Right-click) -> Edir message

把多個 Commit 合併成一個 Commit
-----
* ### git log --oneline, git rebase -i bb0c9c2, replace "pick" to "squash"
* ### SOURCETREE -> WORKSPACE -> History -> select commit (Right-click) -> Rebase children of bb0c9c2 interactively... -> Description (Right-click) -> Squash with previous commit

Pull Request 流程
-----
* ### 複製 (Fork) 專案
* ### Clone 回來修改
* ### 執行 Commit
* ### Push 回自己的專案
* ### 發 PR 給原作者ß

怎麼跟上當初 fork 專案的進度
-----
* ### [Syncing a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)

Reference
=====
* ### 為你自己學 Git
