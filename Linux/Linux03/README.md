Linux03 文本限制、通配符、环境变量
=====
* ### 查看权限
    ```
    $ ls -l
    ```
    * ### 文件信息的前 10 个字符 (例如: drwxr-xr-x) 分别代表了不同的意义。
    * ### 第一位代表文件类型，2 ~ 4 位代表文件的所有者 (owener) 对文件的权限，第 5 ~ 7 位代表所有者的同组用户 (group) 拥有该文件的权限，第 8 ~ 10 位代表其他用户 (others) 拥有该文件的权限。
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/Linux/Linux03/FilePermissions.png)
    * ### 第一个字符代表文件类型:
        * ### [d]: 目录。
        * ### [-]: 文件。
        * ### [l]: 链接文件。
        * ### [b]: 串行端口设备。
    * ### 接下来的字符以三个为一组，用 r、w、x 三个参数的组合表示，位置不会变: 
        * ### [r]: 可读 (read)。
        * ### [w]: 可写 (write)。
        * ### [x]: 可执行 (execute)。
        * ### [-]: 没有权限。
    * ### 字符後的第一个名稱代表这个文件所属的用户，第二个名稱表达这个文件属于的组群。
    * ### 用户一般就是指使用电脑的人、Group 组群是用户的集合。
* ### 修改权限: chmod <who><what> <file>
    ```
    # 给予同组的人写的权利: group + write
    chmod g+w FILE_NAME
    ```
    * ### chmod 的具体参数:
        * ### who: u 对于 User 权限的修改，g 对于 Group 权限的修改，o 為其它权限的修改，a 為所有人权限的修改。
        * ### what: +、–、= 表达加上、减掉、等于接續所指定的权限，r、w、x 表示被修改的权限，也可以将多个权限加起来，比如 rwx。
        * ### file: 被操作的文件，可以为多个。
* ### Linux 通配符 (Wildcard): 用於一次性操作多个文件，為一种短文本模式，也稱通配符 (wildcards)，简洁地代表一组路径。
    * ### ```?```: 单个字符。
        ```
        $ ls ?.txt
        a.txt b.txt

        $ ls ???.txt
        abc.txt

        $ ls file?.txt
        file1.txt file2.txt
        ```
    * ### ```*```: 任意数量字符 (以複製副檔名為 .txt 檔案至指定資料夾為例)。
        ```
        cp *.txt FOLDER_NAME/
        ```
        ```
        $ ls *.txt
        a.txt b.txt abc.txt file1.txt file2.txt

        $ ls a*.txt
        a.txt
        ```
    * ### ```[…]```: 匹配括号中任意一个字符。
        ```
        $ ls [ab].txt
        a.txt b.txt
        ```
    * ### ```[start-end]```: 表示一个连续的范围。
        ```
        $ ls file[1-3].txt
        file1.txt file2.txt file3.txt
        ```
    * ### ```{...}```: 表示匹配大括号中的所有模式 (模式之间用逗号分隔)。
        ```
        $ ls {file,file1}.txt
        file.txt file1.txt
        ```
* ### 环境变量设置方式
    ```
    # 查看具体环境变量
    $ echo $PATH

    # 设定环境变量
    $ ENV_VAR_NAME=PATH

    # 清除环境变量
    $ unset ENV_VAR_NAME

    # 加入其它变量到 PATH 变量中
    $ PATH=$PATH:<PATH1>:<PATH2>:<PATH3>
    ```
* ### 以上的环境变量生存周期只在当前 shell 中，如果要添加一些永久性生效的环境变量，则需要将变量添加在 ```/etc/profile``` 文件中 (以 Java 為例):
    ```
    $ nano ~/.bash.profile

    export CLASSPAHT=./JAVA_HOME/lib;$JAVA_HOME/jre/lib
    ```
    * ### 运行 ```$ source ~/.bach_profile``` 使其立即生效 (否則在用户重新登入时才能生效)。
* ### 命令总结
    ```
    # 查看具体文件信息
    $ ls -l

    $ chmod <who><what> <file_name>

    # 给予同组的人写 script1.py 的权限
    $ chmod g+w script1.py

    # 给予所以人读写和执行 script1.py 的全部权限
    $ chmod 777 script1.py
    ```
    ```
    # 单字符匹配
    $ ls ?.txt

    # 任意字符匹配
    $ ls *.txt

    # 可选匹配通配符
    $ ls [ab].txt

    # 可选匹配通配符
    $ ls {a,b,c}.txt
    ```
    ```
    # 显示某个环境变量值
    $ echo $PATH

    # 设置一个新的环境变量
    $ export NEW_VAL="test"

    # 显示所有环境变量
    $ env

    # 显示本地定义的 shell 变量
    $ set

    # 清楚环境变量
    $ unset <Variable_Name>

    # 设置只读环境变量
    $ readonly NEW_VAL
    ```
<br />
