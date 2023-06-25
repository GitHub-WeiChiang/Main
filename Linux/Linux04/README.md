Linux04 Linux 远程控制、AWS 创建和脚本编辑
=====
* ### SSH 安全登入
    ```
    # 安装 openssh-server 软件
    $ sudo apt-get install openssh-server

    # 安装 net-tools 软件
    $ sudo apt-get install net-tools

    # 查詢 IP (可能需要調整虛擬機網路設定)
    $ ifconfig

    # 查看當前用戶
    $ whoami

    # 設定密碼
    $ passwd
    ```
    ```
    # 連入 Ubuntu
    ssh ubuntu@IP

    # 離開 Ubuntu
    exit
    ```
* ### TeamViewer 图像化远程操作
    * ### 至官網下載 TeamViewer 後執行下方指令進行安裝。
    ```
    sudo dpkg -i PKG_NAME

    sodu apt-get install -f
    ```
    * ### How to uninstall teamviewer ?
        * ### First, use the command:
            ```
            dpkg -l | grep team
            ```
        * ### The full package name should show up in the output on the list of installed applications.
        * ### Find it and use the name listed.
        * ### I believe it should look like this:
            ```
            sudo apt purge teamviewer
            ```
        * ### or, if you want to use a wild card, you can use something like this instead:
            ```
            sudo apt remove "teamview*"
            ```
        * ### However, be careful when using a wildcard so you don't unintentionally uninstall something you want to keep.
        * ### Always review the list of packages to be removed before selecting Y.
* ### scp 文件传输
    * ### 将本地文件 file1.txt 传到 Linux 系统的桌面上
        ```
        scp ./file1.txt ACCOUNT_NAME@IP:~/Desktop
        ```
    * ### 在本地的 Terminal 中将 Linux 系统中的文件 file2.txt 复制到本地
        ```
        $ scp ACCOUNT_NAME@IP:~/Desktop/file2.txt ./
        ```
* ### Python 脚本编辑
    ```
    # copy.py
    
    import os
    os.system('cp file1.txt file2.txt')
    ```
    ```
    $ python3 copy.py
    ```
<br />
