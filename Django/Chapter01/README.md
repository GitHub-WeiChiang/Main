Chapter01 網站開發環境建置
=====
* ### 內容管理系統 (Content Management System, CMS)
    * ### 在一個合作模式下，用於管理工作流程的一套制度。該系統可應用於手工操作中，也可以應用到電腦或網路裡。作為一種中央儲存器 (Central Repository)，內容管理系統可將相關內容集中儲存並具有群組管理、版本控制等功能。版本控制是內容管理系統的一個主要優勢。
    * ### 內容管理系統在物品或文案或資料的儲存、掌管、修訂 (盤存)、語用充實、文件發布等方面有著廣泛的應用。現在流行的開源 CMS 系統有 WordPress、Joomla!、Drupal、Xoops 和 CmsTop 等。
* ### mac 安装 Anconda 后 Terminal 出现 (base)
    * ### 每次在命令行通过 ```conda deactivate``` 退出 base 环境回到系统自动的环境。
    * ### 設置 auto_activate_base 值
        ```
        # 設置 auto_activate_base 為 false
        conda config --set auto_activate_base false

        # 進入 base
        conda activate base

        # 設置 auto_activate_base 為 true
        conda config --set auto_activate_base true
        ```
* ### 利用 virtualenv 建立虛擬環境
    ```
    # 建立
    virtualenv venv_name
    ```
    ```
    # 進入

    # Windows
    venv_name\Scripts\activate

    # macOS
    source venv_name/bin/activate
    ```
    ```
    # 離開
    deactivate
    ```
* ### 利用 conda 建立虛擬環境
    ```
    # 查看
    conda env list

    # 建立
    conda create --name venv_name python=3.10

    # 進入
    conda activate venv_name

    # 離開
    conda deactivate

    # 刪除
    conda env remove --name venv_name
    ```
* ### 新網站專案開發基本步驟
    ```
    # 建立
    conda create --name venv_name python=3.10

    # 進入
    conda activate venv_name

    # 安裝 Django
    pip install django

    # 初始化
    django-admin startproject project_name

    # 匯出第三方模組
    pip freeze > requirements.txt

    # 安裝第三方模組
    pip install -r requirements.txt
    ```
<br />
