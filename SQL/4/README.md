4 - SQL 基本查询语法
=====
* ### Students
    | StudentID | Name | Gender | Age | City |
    | - | - | - | - | - |
    | 1 | David | M | 21 | Shanghai |
    | 2 | Kevin | M | 19 | Beijing |
    | 3 | Emily | F | 22 | Shanghai |
    | 4 | William | M | 20 | New York City |
    | 5 | Alice | F | 19 | Los Angeles |
* ### Courses
    | CourseID | CourseName |
    | - | - |
    | 1 | CS101 |
    | 2 | CS202 |
    | 3 | EE101 |
* ### 创建表並插入資料
    ```
    CREATE TABLE Students (
        StudentID int PRIMARY KEY,
        Name varchar(255),
        Gender varchar(1),
        Age int,
        City varchar(255)
    );

    INSERT INTO Students VALUES(1, 'David', 'M', 21, 'Shanghai');
    INSERT INTO Students VALUES(2, 'Kevin', 'M', 19, 'Beijing');
    INSERT INTO Students VALUES(3, 'Emily', 'F', 22, 'Shanghai');
    INSERT INTO Students VALUES(4, 'William', 'M', 20, 'New York City');
    INSERT INTO Students VALUES(5, 'Alice', 'F', 19, 'Los Angeles');
    ```
    ```
    CREATE TABLE Courses (
        CourseID int PRIMARY KEY,
        CourseName varchar(255)
    );

    INSERT INTO Courses VALUES(1, 'CS101');
    INSERT INTO Courses VALUES(2, 'CS202');
    INSERT INTO Courses VALUES(3, 'EE101');
    ```
* ### 基本查询
    ```
    -- 查询表的据
    SELECT * FROM table_name;

    -- 查询 Students 表中所有记录
    SELECT * FROM Students;
    ```
* ### 条件查询
    ```
    -- 限定查询记录的条件
    SELECT * FROM table_name WHERE condition;

    -- 只抓取年纪大于 20 的学生记录
    SELECT * FROM Students WHERE Age > 20;
    ```
* ### 条件表达式
    ```
    -- 性别为 Male 且年纪大于 20
    SELECT * FROM Students WHERE Gender = 'M' AND Age > 20;

    -- Gender 为 F 或者 Age 小于 20
    SELECT * FROM Students WHERE Gender = 'F' OR Age < 20;

    -- Gender 不为 F
    SELECT * FROM Students WHERE NOT Gender = 'F';

    -- Age 在 20 以下或 22 以上且是男生的学生
    SELECT * FROM Students WHERE (Age < 20 OR Age > 22) AND Gender = 'M';
    ```
* ### 常见条件表达式
    | 条件 | 说明 | Example 1 | Example 2 |
    | - | - | - | - |
    | = | 相等 | age = 20 | name = 'xyz' |
    | > | 大于 | age > 20 | name > 'xyz' |
    | >= | 大于等于 | age >= 20 | name >= 'xyz' |
    | < | 小于 | age < 20 | name < 'xyz' |
    | <= | 小于等于 | age <= 20 | name <= 'xyz' |
    | <> | 不等于 | age <> 20 | name <> 'xyz' |
    | LIKE | 相似 |  | name LIKE 'xy%' (% 表示任意字符，xy% 表示以 xy 为开头的字符) |
* ### 投影查询 (特定字段查询)
    ```
    -- 年纪大于 20 的学生的 StudentID 和 Name 字段
    SELECT StudentID, Name FROM Students WHERE Age > 20;

    -- 去重
    SELECT DISTINCT column1, column2, ... FROM table_name;

    -- 学生来自哪些不同的城市
    SELECT DISTINCT City FROM Students;
    ```
* ### 排序 ORDER BY
    ```
    -- 語法
    SELECT col1, col2, ... 
    FROM table_name
    ORDER BY col1, col2, ... ASC|DESC;

    -- 学生按照年龄从小到大排序 (默认為 ASC)
    SELECT * FROM Students ORDER BY Age;

    -- 学生按照年龄从大到小排序
    SELECT * FROM Students ORDER BY Age DESC;

    -- 按照年纪从小到大排序后再根据性别排序
    SELECT * FROM Students ORDER BY Age ASC, Gender;

    -- WHERE + ORDER BY
    SELECT * FROM Students 
    WHERE City = 'Shanghai'
    ORDER BY Age;
    ```
* ### 选取年纪大于 20 且来自上海的学生，将结果按照年纪从小到大排序且结果只顯示 StudentID 字段。
    ```
    SELECT StudentID 
    FROM Students
    WHERE Age > 20 AND City = 'Shanghai'
    ORDER BY Age ASC;
    ```
<br />
