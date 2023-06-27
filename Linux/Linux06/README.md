Linux06 Linux 实践练习
=====
* ### 文本操作
    * ### 创建一个新的文件夹 folder1。
    * ### 在 folder1 中创建新的文件 file1.txt。
    * ### 使用 nano 編輯 file1.txt。
    * ### 创建一个 folder2 並将 folder1 完全复制到 folder2 中。
    * ### 删除 folder1 文件夹。
    ```
    $ mkdir folder1
    $ touch folder1/file1.txt
    $ nano folder1/file1.txt
    $ mkdir folder2
    $ cp -r folder1 folder2
    $ rm -r folder1
    ```
* ### 文本权限、通配符、环境变量
    * ### 将当前文件夹中所有以 .txt 为后缀的文件，设置以下的权限:
    * ### 用户可读可写可执行、同组的人可读可写、其他人可读。
    ```
    $ chmod u=rwx *.txt
    $ chmod g=rw *.txt
    $ chmod o=r *.txt
    ```
    * ### 也可以通过设置数字来修改权限:
    * ### 4 代表可读、2 代表可写、1 代表可读，故 7 = 4 + 2 + 1 就是可读可写可执行，6 = 4 + 2 就是可读可写，1 就是可读。
    ```
    $ chmod 764 *.txt
    ```
* ### Linux 远程控制和脚本编辑
    * ### 在 Linux 桌面创建 3 个文件: file1.txt、file2.txt 和 file3.txt。
    * ### 编辑一个 Python 脚本，将这三个文件放到一个叫 new_folder 的新文件夹中。
    ```
    # script.py
    import os
    os.system('mv file1.txt file2.txt file3.txt new_folder')
    ```
<br />
