6 - MySQL 简介和安装
=====
* ### macOS 快速安裝與啟動 (預設密碼為空白)
    ```
    brew install mysql

    brew install --cask mysqlworkbench
    ```
    ```
    brew services start mysql
    brew services stop mysql
    ```
    ```
    mysql -u root -p
    ```
    ```
    mysqladmin -u root -p --ssl-mode=required password
    ```
* ### 在系统路径中加入 mysql 的执行代码 (非 Homebrew 安裝)
    ```
    export PATH=${PATH}:/usr/local/mysql/bin
    ```
* ### 簡單實踐示例
    ```
    CREATE DATABASE testDB;

    USE testDB;

    CREATE TABLE Students (
        StudentID int PRIMARY KEY, 
        Name varchar(255),
        City varchar(255)
    );

    INSERT INTO Students VALUES(1, 'David', 'Beijing');

    SELECT * FROM Students;
    ```
<br />
