Linux01 Linux 操作系统简介和 Ubuntu 安装
=====
* ### 計算機
    ```
    bc

    quit
    ```
* ### 日曆
    ```
    cal

    cal 2019
    ```
* ### ```Solved``` "E: Unable to locate package" Error on Ubuntu
    ```
    # Solution 1: Check the Package Spelling
    $ sudo apt install package

    # Solution 2: Update and Upgrade All Packages
    $ sudo apt update && sudo apt upgrade -y

    # Solution 3: Add Missing Repositories
    $ sudo add-apt-repository main
    $ sudo add-apt-repository universe
    $ sudo add-apt-repository restricted
    $ sudo add-apt-repository multiverse

    # Install
    $ sudo apt install PACKAGE_NAME
    ```
<br />
