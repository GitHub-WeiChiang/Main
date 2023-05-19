Chapter03 讓網站上線
=====
* ### DigitalOcean -> [click me](https://www.digitalocean.com/)
* ### macOS connect via SSH
    ```
    ssh root@IP

    exit
    ```
* ### 安裝 Apache 網頁伺服器及設置 Django 執行環境
    ```
    """
    此處流程僅進行至使用 Django 內建開發伺服器執行
    """

    # 已安装的软件包是否有可用的更新: 提供汇总报告 (只检查不更新)
    apt update

    # 通过 APT (Advanced Package Tool) 进行软件包升级，
    # 使用 -y 选项可以使命令自动确认所有的升级操作，而无需用户进行手动确认。
    apt upgrade -y

    # 安装 Apache HTTP 服务器
    apt install apache2 -y

    # 安装 Apache HTTP Server 的 mod_wsgi 模块，
    # 以支持使用 Python 3 运行在 Apache 服务器上的 Web 应用程序。
    apt install libapache2-mod-wsgi-py3 -y

    # 安裝 Git 版本控制工具
    apt install git -y
    # 設置 Git Config
    git config --global user.name "GitHub-WeiChiang"
    git config --global user.email "albert0425369@gmail.com"

    # Install python pip and virtualenv.
    apt install python3-pip -y
    pip install virtualenv

    # 進入 /var/www (Linux 中 Apache 會將網頁放置於此)
    cd /var/www

    # 建立虛擬環境
    virtualenv venv_name

    # Git clone.
    git clone https://github.com/...

    # 啟動虛擬環境
    source venv_name/bin/activate

    # 進入專案並執行第三方軟體包安裝
    cd project_name
    pip install -r requirements.txt

    # 建立 Migration (資料遷移) 中介檔案
    python manage.py makemigrations
    # 依照 Migration (資料遷移) 中介檔案進行同步更新
    python manage.py migrate
    # 啟用 admin 管理介面
    python manage.py createsuperuser

    # 執行
    python manage.py runserver IP:Port
    ```
* ### setting.py: 負責 Django 網站相關設定。
* ### wsgi.py: 負責建立與 Apache 轉交程式碼以及回傳執行結果。
* ### FileZilla -> [click me](https://filezilla-project.org/)
<br />
