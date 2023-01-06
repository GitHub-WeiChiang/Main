Question013 - 聯合主鍵和複合主鍵的差異 ?
=====
* ### 聯合主鍵: 透過兩張表格各自的 Primary Key 所組合而成。
* ### 複合主鍵
    * ### 型態一 (Composite Key): 由多個欄位所組成的 Primary Key。
    * ### 型態二 (Compound Key): 組成的 Primary Key 中包含了 Foreign Key。
* ### 簡而言之，聯合主鍵是 Compound Key 的一種，Compound Key 又是 Composite Key 的一種。
* ### 嚴格意義上來說，這是一個玄學...
```
--- 学生表
CREATE TABLE `student` (
    `student_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `name` varchar(20) NOT NULL,
    PRIMARY KEY (`student_id`) USING BTREE
);

--- 科目表
CREATE TABLE `subject` (
    `subject_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `name` varchar(20) NOT NULL,
    PRIMARY KEY (`subject_id`) USING BTREE
);

--- 分数表，用所谓的 “复合主键”
CREATE TABLE `score` (
    `student_id` int(10) unsigned NOT NULL,
    `subject_id` int(10) unsigned NOT NULL,
    `value` int(10) unsigned NOT NULL,
    PRIMARY KEY (`student_id`, `subject_id`) USING BTREE
);

--- 分数表，用所谓的 “联合主键”
CREATE TABLE `score` (
    `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `student_id` int(10) unsigned NOT NULL,
    `subject_id` int(10) unsigned NOT NULL,
    `value` int(10) unsigned NOT NULL,
    PRIMARY KEY (`id`) USING BTREE,
    UNIQUE INDEX `un`(`student_id`, `subject_id`) USING BTREE
);
```
* ### 在英文语境中只有 Composite Primary Key（也有叫 Compound Primary Key 的），就是一个表中如果是多个字段组成一个主键，那么这个主键就被称为这玩意儿。
* ### 上述概念是中文编程界人为造出的，所以恭喜白學，看看就好。
<br />
