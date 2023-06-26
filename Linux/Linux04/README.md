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
* ### 创建 AWS EC2 Instance
    * ### AWS EC2 ubuntu
    * ### Lauch a instance
    * ### Download the keypair
* ### 連線至執行個體
    * ### 選擇執行個體 -> 連線
    ```
    chmod 400 ssh.pem

    ssh -i "ssh.pem" ubuntu@ec2-35-91-120-232.us-west-2.compute.amazonaws.com
    ```
* ### VNC: VNC 是一款优秀的云服务器远程控制图像化操作工具软件，由著名的 AT&T 的欧洲研究实验室开发。
    ```
    $ sudo apt-get update

    $ sudo apt-get upgrade

    $ sudo apt-get install ubuntu-desktop gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal xfce4

    $ sudo apt install xfce4-goodies

    $ sudo apt install tightvncserver

    # Enter password after
    $ vncserver
    ```
    * ### 將以下內容覆蓋至 ```~/.vnc/xstartup```
        ```
        vim ~/.vnc/xstartup

        # 删除全部内容
        # gg: 光标跳转到该文件的行首。
        # dG: 删除光标行及其以下行的全部内容 (d 为删除，G 为光标跳转到末尾行)。
        ggdG
        ```
        ```
        #!/bin/sh
        # Uncomment the following two lines for normal desktop:
        unset SESSION_MANAGER
        # exec /etc/X11/xinit/xinitrc
        unset DBUS_SESSION_BUS_ADDRESS
        startxfce4 &
        [ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
        [ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
        xsetroot -solid grey
        vncconfig -iconic &
        gnome-panel &
        gnome-settings-daemon &
        metacity &
        nautilus &
        gnome-terminal &
        ```
    ```
    $ exit

    $ ssh -L 5902:localhost:5902 -i ./ssh.pem ubuntu@IP_V_4

    $ vncserver -geometry 1340x750
    ```
    * ### 下載並註冊 VNC Viewer
    * ### 開啟 VNC Viewer 並在 RVNC CONNECT 中輸入 localhost:5902。
* ### 使用 screen share (macOS) 来连接 VNC
    ```
    $ ssh -L 5902:localhost:5902 -i ./ssh.pem ubuntu@IP_V_4
    ```
    * ### Command + Space
    * ### localhost:5902
<br />
