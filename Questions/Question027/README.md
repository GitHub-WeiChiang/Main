Question027 - InnoDB 中的存取方法有哪些 ?
=====
* ### 存取方法
    * ### const: 唯一二級索引 -> 聚簇索引或直接透過聚簇索引 (常數相等比較)。
    * ### ref: 普通二級索引 -> 聚簇索引 (常數相等比較)。
    * ### ref_or_null: 和 ref 相同但多的 null 比較 (常數相等比較)。
    * ### range: 多個單點或範圍掃描區間。
    * ### index: 遍歷二級索引且不用回表。
    * ### all: 全資料表掃描 (聚簇索引)。
    * ### index merge
        * ### Intersection 索引合併。
        * ### Union 索引合併。
        * ### Sort - Union 索引合併。
    * ### 註: MySQL 沒有 Sort - intersection。
* ### 理解更多 -> [click me](https://github.com/GitHub-WeiChiang/main/tree/master/MySQLPrinciples/Chapter10)
<br />
