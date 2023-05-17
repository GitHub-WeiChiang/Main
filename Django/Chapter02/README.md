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

    conda deactivate
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
    | manage.py | BASE DIR | 網站管理程式，執行命令操作 |
    | db.sqlite3 | BASE DIR | 預設資料庫檔案 |
    | settings.py | PROJECT DIR | 組態檔 |
    | urls.py | PROJECT DIR | 路由映射 |
    | wsgi.py | PROJECT DIR | 伺服器對接檔 |
    | views.py | APP DIR | 控制流程 |
    | models.py | APP DIR | 資料表映射模型 |
    | admin.py | APP DIR | 後台管理程式設定 |
    | forms.py | APP DIR | 表單內容 |
* ### settings.py 的初始化編輯
    ```
    ALLOWED_HOSTS = ['*']

    INSTALLED_APPS = [
        ...,
        'APP_NAME',
    ]

    LANGUAGE_CODE = 'zh-hant'

    TIME_ZONE = 'Asia/Taipei'
    ```
    | LANGUAGE_CODE | VALUE |
    | - | - |
    | Hira | 平假名 |
    | Kana | 片假名 |
    | Hrkt | 日文假名 (平假名 + 片假名) |
    | Jpan | 日文 (漢字 + 平假名 + 片假名) |
    | Hani | 漢字 |
    | Hans | 簡體漢字 |
    | Hant | 繁體漢字 |
* ### 生成 db.sqlite3
    ```
    # 建立 Migration (資料遷移) 中介檔案
    python manage.py makemigrations

    # 依照 Migration (資料遷移) 中介檔案進行同步更新
    python manage.py migrate
    ```
* ### What is a slug?
    * ### A slug is the part of a URL which identifies a particular page on a website in an easy to read form.
    * ### In other words, it’s the part of the URL that explains the page’s content.
    * ### For this article, for example, the URL is https://yoast.com/slug, and the slug simply is 'slug'.
* ### 啟用 admin 管理介面
    ```
    python manage.py createsuperuser

    # Username: admin
    # Password: admin
    # 需在 admin.py 中進行資料表納管
    # http://127.0.0.1:8000/admin/
    ```
* ### render(): 此函式會將 template 進行渲染。
* ### locals(): 此函式會將所在區域之變數使用字典打包以供使用。
* ### Pasteboard — Easy Image Uploads -> [click me](https://pasteboard.co/)
* ### 生成 requirements.txt
    ```
    pip list --format=freeze > requirements.txt
    ```
<br />
