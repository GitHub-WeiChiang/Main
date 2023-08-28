3 - 数据操作: 表格, 记录, 约束
=====
* ### 表格 (创建、修改、删除)
    * ### 创建表
        ```
        -- 基本语法

        CREATE TABLE table_name (
            column1 datatype1,
            column2 datatype2,
            column3 datatype3,
            ....
        );
        ```
        ```
        -- 範例

        CREATE TABLE Students (
            StudentID int, 
            Name varchar(255),
            City varchar(255),
            PRIMARY KEY(StudentID)
        );
        ```
    * ### 修改表
        ```
        ALTER TABLE table_name 
        ADD column_name datatype;
        ```
        ```
        -- 添加一个类型为 int 的 Age 字段

        ALTER TABLE Students
        ADD age int;
        ```
        ```
        -- 删除字段

        ALTER TABLE Students 
        DROP COLUMN Age;
        ```
        ```
        -- 修改字段设定
        
        ALTER TABLE Students 
        MODIFY COLUMN Name varchar(200);
        ```
    * ### 删除表
        ```
        DROP TABLE Students;
        ```
* ### 常用的 SQL 数据类型
    | 数据类型 | 描述 |
    | - | - |
    | VARCHAR(n) 或 CHARACTER VARYING(n) | 可变长度的字符/字符串，最大长度为 n |
    | BINARY(n) | 固定长度为 n 的二进制串 |
    | BOOLEAN | 存储 TRUE 或 FALSE 值 |
    | INTEGER(p) | 整数值 (没有小数点)，精度为 p |
    | INTEGER | 整数值 (没有小数点)，精度为 10 |
    | DECIMAL(p, s) | 精确数值，精度为 p，小数点后位数为 s，例如: DICIMAL(5, 2) 小数点前有 3 位数，小数点后有 2 位数 |
    | FLOAT(p) | 近似数值，尾数精度为 p |
    | FLOAT | 近似数值，尾数精度为 16 |
    | DATE | 存储年、月、日的值 |
    | TIMESTAMP | 存储年、月、日、小时、分、秒的值 |
* ### 操作记录 (增加、删除、修改、替换)
    * ### 插入记录
        ```
        -- 基本语法 1

        INSERT INTO table_name(column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
        ```
        ```
        -- 基本语法 2

        INSERT INTO table_name VALUES (value1, value2, value3, ...);
        ```
        ```
        -- 插入一个新学生的记录

        INSERT INTO Students(StudentID, Name, City) VALUES (1, 'Enoch', 'Los Angeles');
        ```
    * ### 修改记录
        ```
        -- 基本语法

        UPDATE table_name
        SET column1 = value1, column2 = value2, ...
        WHERE condition;
        ```
        ```
        -- 将 StudentID 为 1 的学生改名为 'Daniel'

        UPDATE Students
        SET Name = 'Daniel' 
        WHERE StudentID = 1;
        ```
    * ### 删除记录
        ```
        -- 基本语法

        DELETE FROM table WHERE condition;
        ```
        ```
        -- 将所有住在 'Los Angeles' 的学生记录删除

        DELETE FROM Students WHERE City = 'Los Angeles';
        ```
    * ### 替换
        ```
        -- 希望插入一条新纪录，但是如果此记录已经存在，就先删除原记录，再插入新纪录。

        REPLACE INTO Students(StudentID, name, city) VALUES (1, 'Enoch', 'New York City');
        ```
* ### 约束 (Constraints)
    ```
    -- 基本语法

    CREATE TABLE table_name (
        column1 data_type1(size) constraint1,
        column2 data_type2(size) constraint2,
        column3 data_type3(size) constraint3,
        ...
    );
    ```
    ```
    -- 範例

    CREATE TABLE Employees (
        EmployeeID int Primary Key,
        Name varchar(255) NOT NULL,
        Dpartment varchar(255) DEFAULT 'A',
        Age int CHECK (Age > 18)
    );
    ```
    * ### 常見的約束
        * ### NOT NULL: 字段不能存储空值。
        * ### UNIQUE: 保证字段的每行都是唯一的值。
        * ### PRIMARY KEY: 主键，NOT NULL 和 UNIQUE 的结合，确保某列 (或多列) 有唯一标识，用于找到特定记录。
        * ### FOREIGN KEY: 保证表中的数据匹配到 (指向) 另一个表中的主键。
        * ### CHECK: 保证字段的值符合指定条件。
        * ### DEFAULT: 规定没赋值时的默认值。
    * ### 创建约束 ALTER TABLE
        ```
        -- 基本语法

        ALTER TABLE Students 
        MODIFY Age int NOT NULL;
        ```
        ```
        -- 添加一个外键约束

        ALTER TABLE Students
        ADD CONSTRAINT fk_class_id
        FOREIGN KEY (classID)
        REFERENCES Classes (id);
        ```
        ```
        -- 删除 Students 中 classID 的外键约束

        ALTER TABLE Students
        DROP FOREIGN KEY fk_class_id;
        ```
<br />
