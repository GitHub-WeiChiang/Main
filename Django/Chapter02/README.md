Chapter02 Django 網站快速入門
=====
* ### item2 文件路徑過長
    ```
    vim ~/.oh-my-zsh/themes/agnoster.zsh-theme

    i

    # Dir: current working directory
    prompt_dir() {
      # prompt_segment blue $CURRENT_FG '%~'
      prompt_segment blue $CURRENT_FG '%1d'
    }

    [ESC]

    :wq
    ```
* ### 建立虛擬環境
    ```
    conda create --name Chapter02 python=3.10

    conda activate Chapter02
    ```
* ### 建立網站框架
    ```
    pip install django

    # 建立 Django 專案
    django-admin startproject mblog

    cd mblog

    # 建立 Django App
    python manage.py startapp mysite

    # 啟動 Django 伺服器
    python manage.py runserver
    ```
* ### Django 網站框架主要檔案用途
    | 檔案名稱 | 資料夾位置 | 用途 |
    | - | - | - |
    | manage.py | BASE DIR | 網站管理程式，執行命令操作。 |
    | db.sqlite3 | BASE DIR | 預設資料庫檔案。 |
    |  |  |  |
    |  |  |  |
    |  |  |  |
    |  |  |  |
    |  |  |  |
    |  |  |  |
    |  |  |  |
<br />
