Question002 - 什麼是 Bloom Filter ?
=====
* ### 什麼是 Bloom Filter: 是一個可以儲存「某一個元素是否存在」的集合。
    * ### 不存在漏報 (False Negative): 有一定會說。
    * ### 但卻可能誤報 (False Positive): 但說了不一定會對。
    * ### 確定某元素是否在集合的代價和元素數目無關: 不管對不對，反正很快。
    * ### 不果只要它說不在就一定不在。
* ### Difference between Bloom filters and Hashtable
    * ### In hash table the object gets stored to the bucket (index position in the hashtable) the hash function maps to.
    * ### Bloom filters doesn't store the associated object. It just tells whether it is there in the bloom filter or not.
    * ### Hash tables are less space efficient.
<br />
