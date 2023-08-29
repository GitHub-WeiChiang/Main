5 - SQL 高级查询语法
=====
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
    INSERT INTO Students VALUES(6, 'Frank', 'F', 22, 'Los Angeles');
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
* ### 聚合查询 (聚合函数)
    ```
    -- 查询有多少学生
    SELECT COUNT(*) FROM Students;

    -- 對 COUNT(*) 设置别名
    SELECT COUNT(*) AS StudentsNum FROM Students;

    -- 查找年龄大于 20 岁的学生数量
    SELECT COUNT(*) FROM Students WHERE Age > 20;

    -- 查询学生的平均年龄
    SELECT AVG(Age) FROM Students;
    ```
* ### 常用的聚合函数
    | 函数 | 说明 |
    | - | - |
    | SUM | 计算某一列的总和，该列必须为数值类型 |
    | AVG | 计算某一列的平均数，该列必须为数值类型 |
    | MAX | 计算某一列的最大值 |
    | MIN | 计算某一列的最小值 |
* ### 分组
    ```
    -- 查询每个城市有多少学生
    SELECT City, COUNT(*) FROM Students GROUP BY City;

    -- 先将学生根据 City 分组再根据性别分组
    SELECT City, Gender, COUNT(*) FROM Students GROUP BY City, Gender;
    ```
* ### 多表查询
    ```
    -- 基礎語法
    SELECT * FROM table1, table2;

    -- 查询 Students 表和 Courses 表的 "笛卡爾乘積"
    SELECT * FROM Students, Courses;

    -- 使用 AS 取别名来区别字段與表
    SELECT Students.StudentID AS StudentId, Courses.CourseID AS CourseId FROM Students, Courses;

    SELECT Students.ID AS StudentId, Courses.ID AS CourseId FROM Students, Courses;

    SELECT S.ID AS StudentId, C.ID AS CourseId FROM Students AS S, Courses AS C;

    -- 抓取 StudentID 和其对应的所選课程名字
    SELECT S.StudentID, C.CourseName FROM Students AS S, Courses AS C WHERE S.CourseID = C.CourseID;
    ```
* ### 连接 (JOIN) 查询
    ```
    -- 抓取 StudentID 和其对应的所選课程名字
    SELECT S.StudentID, C.CourseName 
    FROM Students AS S 
    INNER JOIN Courses AS C ON S.CourseID = C.CourseID;
    ```
* ### RIGHT [OUT] JOIN & LEFT [OUT] JOIN
    ```
    SELECT S.StudentID, C.CourseName
    FROM Students AS S 
    RIGHT JOIN Courses AS C ON S.CourseID = C.CourseID;
    ```
    * ### 如果有一节课没有任何学生加入，会有一行多余的记录，记录中仅有 CourseName，但是 StudentID 为 NULL。
    * ### INNER JOIN 会返回同时存在两张表的数据，如果 Students 有 1、2、3 與 5 课号，Courses 有 1、2、3 與 4 课号，那么结果就是其相交集 1、2、3。
    * ### 而 RIGHT JOIN 返回的则是右表存在的记录，如果左表不存在右表中的某几行，那结果中的那几行就会是 NULL。
    * ### LEFT JOIN 会返回左表中都存在的数，如果给 Students 加上 CourseID = 10，即使 Courses 表中没有 ID 为 10 的课程记录，那么 LEFT JOIN 的结果还是会多一行记录，其对应的 CourseName 是 NULL。
* ### 找出加入 CourseID 为 1 的学生之数量和课程名字，且年纪需為大于 20 岁的女学生。
    ```
    SELECT Courses.CourseName, COUNT(*)
    FROM Students
    INNER JOIN Courses ON Students.CourseID = Courses.CourseID
    WHERE Students.Age > 20 AND Students.CourseID = 1 AND Students.Gender = 'F'
    GROUP BY Students.CourseID;
    ```
* ### 理解更多 -> [click me](https://github.com/GitHub-WeiChiang/main/tree/master/MySQLPrinciples/Chapter11)
<br />
