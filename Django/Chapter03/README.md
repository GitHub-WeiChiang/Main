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
* ### settings.py: 負責 Django 網站相關設定。
* ### wsgi.py: 負責建立與 Apache 轉交程式碼以及回傳執行結果。
* ### FileZilla -> [click me](https://filezilla-project.org/)
* ### 安装 tree 软件包的命令，用于以树形结构显示目录和文件的层次关系。
    ```
    apt install tree -y
    ```
* ### 啟用 Apache 前工作 (settings.py 配置修改)
    ```
    # SECRET_KEY 主要用于加密和保护敏感信息，以及确保应用程序的安全性。
    with open("/etc/secret_key.txt") as f:
        SECRET_KEY = f.read().strip()

    DEBUG = False

    # For testing.
    ALLOWED_HOSTS = ["*"]

    STATIC_URL = 'static/'
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]
    STATIC_ROOT = '/var/www/mblog/staticfiles'

    """
    此時需要執行以下命令

    python manage.py collectstatic

    用于将静态文件收集到一个指定的目录中，以便在生产环境中提供静态文件的访问
    """
    ```
* ### 啟用 Apache 前工作 (000-default.conf 配置修改)
    ```
    <VirtualHost *:80>
        ServerAdmin albert0425369@gmail.com

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        Alias /static /var/www/mblog/staticfiles/
        <Directory /var/www/mblog/staticfiles>
            Require all granted
        </Directory>

        WSGIApplicationGroup %{GLOBAL}
        WSGIDaemonProcess mblog python-path=/var/www/mblog python-home=/var/www/venv_mblog
        WSGIProcessGroup mblog
        WSGIScriptAlias / /var/www/mblog/mblog/wsgi.py
    </VirtualHost>
    ```
* ### 重啟 Apache
    ```
    service apache2 restart
    ```
* ### 問題記錄
    * ### WSGI: Truncated or oversized response headers received from daemon process (Pending)
        ```
        # Add the below line to your httpd.conf.
        # In my case the file was /etc/apache2/sites-available/default-ssl.conf

        WSGIApplicationGroup %{GLOBAL}
        ```
    * ### Other
        ```
        # 确保 Web 服务器可以访问和管理特定目录下的文件和资源。

        """
        chown: 是一个缩写，表示 "change owner"，即更改所有者。
        -R: 是一个选项，表示递归地更改指定目录下的所有文件和子目录的所有者。
        www-data:www-data: 是新的所有者和所属组的标识。
        在这个例子中，www-data 是一个常见的 Apache Web 服务器使用的用户和组。
        """

        chown -R www-data:www-data /var/www/mblog
        ```
* ### 000-default.conf 域名配置修改
    ```
    <VirtualHost domain.name:80>
        ...
    </VirtualHost>
    ```
* ### 啟用 HTTPS (SSL)
    ```
    # 安裝 Snapd 軟體管理工具並啟用，方便安裝、管理和更新自包含的應用程式。
    apt install snapd

    # 使用 Snap 安裝 Certbot 軟體，
    # Certbot 是一個由 Electronic Frontier Foundation (EFF) 開發的工具，
    # 用於自動化在網站上設置和更新 SSL/TLS 加密證書。
    snap install --classic certbot

    # 建立一個符號連結，將 /snap/bin/certbot 連結到 /usr/bin/certbot，
    # 以方便在系統中使用 /usr/bin/certbot 路徑來執行 Certbot 工具。
    ln -s /snap/bin/certbot /usr/bin/certbot

    * ### 000-default.conf HTTPS (SSL) 配置修改
    <VirtualHost domain.name:443>
        ...
    </VirtualHost>

    # 使用 Certbot 工具與 Apache 網頁伺服器進行互動，
    # 以自動獲取和安裝 SSL/TLS 加密證書。
    certbot --apache

    # Redirect HTTP to HTTPS
    <VirtualHost mblog.hopto.org:80>
        Redirect permanent / https://mblog.hopto.org/
    </VirtualHost>

    # 測試憑證的自動更新
    certbot renew --dry-run

    # 檢查憑證到期日
    sudo openssl x509 -dates -noout -in /etc/letsencrypt/live/<your_domain_name>/cert.pem
    ```
* ### Heroku 部署
    ```
    brew tap heroku/brew && brew install heroku

    heroku --version

    heroku login

    heroku --help

    # 安裝 Gunicorn (Green Unicorn) 套件。
    # Gunicorn 是一個 WSGI (Web Server Gateway Interface) HTTP 伺服器，
    # 用於在生產環境中運行 Python Web 應用程序。
    pip install gunicorn

    # 安裝 Django On Heroku 套件。
    # Django On Heroku 是一個 Django 應用程序的插件，
    # 用於簡化在 Heroku 平台上部署 Django 應用程序的過程。
    pip install django-on-heroku

    # 手動建立檔案 Procfile 並寫入以下內容 (與 manage.py 同階層)
    web: gunicorn mblog.wsgi

    # 修改 settings.py 配置
    import django_on_heroku

    DEBUG = False

    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATIC_URL = 'static/' / django_on_heroku.settings(locals())
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]

    # 建立網站
    heroku create app_name

    # 上傳專案至 Heroku 主機
    git add .
    git commit -m "for heroku upload"
    git push heroku main

    # 建立 Migration (資料遷移) 中介檔案
    heroku run python manage.py makemigrations
    # 依照 Migration (資料遷移) 中介檔案進行同步更新
    heroku run python manage.py migrate

    # 瀏覽
    heroku open
    ```
<br />
