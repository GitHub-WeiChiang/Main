Linux02 文件系统和文本操作
=====
* ### 改变当前目录位置
    ```
    # 输出当前所在文件夹
    pwd

    # 切换到不同的文件夹
    cd Desktop/

    # 输出当前所在文件夹
    pwd

    # 返回上一级目录
    cd ..

    # 进入子文件夹
    cd Desktop/Folder01/

    # 返回上级目录两次
    cd ../../

    # 返回刚才所在的目录
    cd -

    # 前往 Home
    cd ~

    # 切换到绝对路径指定文件夹
    cd /home/ubuntu/Desktop/Folder01/
    ```
* ### 查看文件夹内容
    ```
    # 查看文件夹中的内容
    ls

    # 查看文件的详细信 (-l 是 long 的縮寫: 打印權限、用戶名、大小、修改日、名稱)
    ls -l

    # 显示出所有文件 (-a 是 all 的縮寫)
    ls -a

    # 多参数结合
    ls -al

    # 查看指令的具体内容 (man 是 manual 的縮寫)
    man COMMAND
    ```
* ### 创建和删除
    ```
    # 创建文件夹 (mkdir, make directory)
    mkdir FOLDER_NAME

    # 创建子文件夹
    mkdir SUPER_FOLDER_NAME/SUB_FOLDER_NAME

    # 删除文件夹 (rmdir, remove directory): 前提条件為被删除文件夹是空的
    rmdir SUPER_FOLDER_NAME/SUB_FOLDER_NAME

    # 删除文件夹中的全部内容 (-r 或 -R 是 recursively 的縮寫)
    rm -r FOLDER_NAME

    # 创建文件
    touch FILE_NAME

    # 删除文件
    rm FILE_NAME

    # 删除多个文件
    rm FILE_NAME_1 FILE_NAME_2 FILE_NAME_3
    ```
* ### 移动和复制
    ```
    # 移动文件或文件夹: 将 FILE_NAME 移动到文件夹 FOLDER_NAME 中 (mv, move)
    mv FILE_NAME FOLDER_NAME

    # 重命名: 将 FILE_NAME_1 重命名为 FILE_NAME_2
    mv FILE_NAME_1 FILE_NAME_2

    # 复制文件和文件夹: 若文件夹不为空需加上 -r 或 -R 参数 (cp, copy)
    # 将 FILE_NAME 复制到 FOLDER_NAME 中
    cp FILE_NAME FOLDER_NAME
    # 将 FOLDER_NAME_1 全部复制到 FOLDER_NAME_2 中
    cp -R FOLDER_NAME_1 FOLDER_NAME_2
    ```
* ### 编辑文件
    ```
    # 编辑文件: 透過 Ctrl + s 保存並以 Ctrl + x 退出
    nano FILE_NAME

    # 查看文件内容 (cat, catenate)
    cat FILE_NAME

    # 文件內容覆蓋: FILE_NAME_2 的内容会被 FILE_NAME_1 完全覆盖
    cat FILE_NAME_1 > FILE_NAME_2

    # 文件内容添加: FILE_NAME_1 的內容會被添加到 FILE_NAME_2 尾端
    cat FILE_NAME_1 >> FILE_NAME_2
    ```
* ### 重点命令总结
    ```
    # 显示指令 ls 的具体信息
    $ man ls

    # 显示当前路径
    $ pwd

    # 进入 Desktop 文件夹中
    $ cd Desktop

    # 显示当前目录中含有的文件和文件夹
    $ ls

    # 创建文件夹 new_folder
    $ mkdir new_folder

    # 删除文件夹 new_folder
    $ rmdir new_folder

    # 创建 new_file 文件
    $ touch new_file

    # 删除 new_file
    $ rm new_file

    # 將 new_file 移到 new_folder 中
    $ mv new_file new_folder

    # 将 new_file 复制到 new_folder 中
    $ cp new_file new_folder

    # 用 nano 文本编辑器编辑文件
    $ nano file1

    # 在终端查看 file1 内容
    $ cat file1

    # 用 file1 的内容覆盖掉 file2 的内容
    $ cat file1 > file2

    # 在 file2 文件的末尾加上 file1 的内容
    $ cat file1 >> file2
    ```
<br />
