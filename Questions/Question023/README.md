Question023 - MySQL 中的 delimiter 關鍵字有什麼用 ?
=====
* ### delimiter 是 mysql 分隔符，在 mysql 客户端中分隔符默认是分号 ";"，如果一次输入的语句较多，并且语句中间有分号，这时需要新指定一个特殊的分隔符。
* ### 其实就是告诉 mysql 解释器，该段命令是否已经结束了，mysql 是否可以执行了，在命令行客户端中，如果有一行命令以分号结束，那么回车后，mysql 将会执行该命令。
```
mysql> select * from test_table;
```
* ### 上述場景若按下回车，那么 MySQL 将立即执行该语句。
* ### 有时候，不希望 MySQL 这么做，在输入较多的语句且语句中包含有分号時，这种情况就需要事先把 delimiter 换成其它符号。
* ### 创建一个存储过程，在创建该存储过程之前，将 delimiter 分隔符转换成符号 "//"，最后在转换回符号 ";"。
```
-- 将结束标志符更改为 //
delimiter //
 
-- 创建存储过程
create procedure proce_user_count(OUT count_num INT)
reads sql data
begin
	select count(*) into count_num from tb_user;
end
//
 
-- 将结束标志符更改回分号
delimiter ;
```
* ### 先将分隔符设置为 "//"，直到遇到下一个 "//" 才整体执行语句。
* ### 执行完后最后一行 "delimiter ;" 将 mysql 的分隔符重新设置为分号 "；"。
<br />
