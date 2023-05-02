Question032 - 如何在特定業務邏輯下同時新增數據到兩張相關的資料表中 ?
=====
* ### 如果該資料表的 Primary Key 是數據插入前程式可掌握的:
    * ### 在程式邏輯中實作，簡單又具有暴力美。
* ### 如果該資料表的 Primary Key 是 AUTO INCREMENT 的:
    * ### 透過 MySQL Triggers 實作，這是一個較為通用易懂的方法。
    * ### 透過 Common Table Expression 結合 ```RETURNING``` 敘述實作。
    * ### 註: RETURNING is supported by Oracle and PostgreSQL but not by MySQL。
    * ### 註: 但是 MySQL 中有 last_insert_id() 與 NEW 可以使用。
* ### 理解更多 (主鍵生成策略) -> [click me](https://github.com/GitHub-WeiChiang/main/tree/master/Questions/Question022)
* ### 理解更多 (觸發篇) -> [click me](https://github.com/GitHub-WeiChiang/main/tree/master/MySQLPrinciples)
* ### 理解更多 (公共篇) -> [click me](https://github.com/GitHub-WeiChiang/main/tree/master/MySQLPrinciples)
* ### 理解更多 (回傳篇) -> [click me](https://github.com/GitHub-WeiChiang/main/tree/master/MySQLPrinciples)
<br />
