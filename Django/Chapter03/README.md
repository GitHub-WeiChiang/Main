Chapter03 讓網站上線
=====
* ### DigitalOcean -> [click me](https://www.digitalocean.com/)
* ### macOS connect via SSH
    ```
    ssh root@IP

    exit
    ```
* ### 安裝 Apache 網頁伺服器及 Django 執行環境
    ```
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
    ```
<br />
