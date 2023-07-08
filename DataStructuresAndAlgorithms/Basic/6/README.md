6 - 哈希表 Hash Table
=====
* ### 哈希表的实现方式
    * ### 数组: 寻址容易，插删难。
    * ### 链表: 寻址困难，插删易。
    * ### 综合两者: 寻址容易，插删易。
    * ### 哈希表使用 "拉链法" 實現，可理解为 "一堆由链表组成的数组"。
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/DataStructuresAndAlgorithms/Basic/6/Hash.png)
    * ### 哈希表的左侧是数组，数组的每个成员包括一个指针，指向一个链表的头节点，链表可能为空，也可能链接多个节点。
    * ### 存储键值对 (key-value pair) 的方式主要依靠键的特征，通过键的哈希值找到对应的数组下标，然后将其键值对添加到对应的链表中，寻找元素时，也是根据其键的哈希值，找到特定链表其对应的值。
    * ### 哈希表使用哈希函数 (Hash Function) 将键 (key) 转换成一个哈希值 (整形数字)，然后将该数组对数组长度取余，取余得到的数字就当做数组的下标，然后将其键值对添加到对应的链表中。
    * ### 寻找一个键所对应的值时，也是使用哈希函数将键转换为对应的数组下标，并在其链表中定位到该关键字所对应的数值。
* ### 哈希函数 (Hash Function)
    * ### 哈希表能快速添加和查找元素的核心原因就是哈希函数，哈希函数能快速将一个数值转换成哈希值 (整数)。
    * ### 哈希表必须保持哈希值的计算一致，如果两个哈希值是不相同的，那么这两个哈希值的原始输入也是不相同的。
    * ### 如果两个不同的输入得到相同的哈希值，就稱為 "哈希值冲突"，这也是为什么要结合数组和链表来实现哈希表，如果一个关键字对应的数组下标已经有其他元素了，只需要在其对应的链表后创建一个新的节点即可。
* ### 哈希表支持的操作
    * ### 将键值对以链表节点的方式储存，其节点包含自己的键和值。
    * ### 若要将一对键值存入哈希表，需使用哈希函数计算键的哈希值，并与哈希表的长度取模，后找到对应的数组下标，若该位置没有其他键值节点，直接将其位置指向新节点。
    * ### 若对应的位置有其他节点，直接将其新节点加到链表的最后面。
    * ### 若要查找一个键所对应的值，只需计算该键对应的哈希值，找到数组下标所对应的头节点后，从头节点开始寻找所要的键值对。
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/DataStructuresAndAlgorithms/Basic/6/HashTable.png)
    * ### 支持操作
        * ### get(key): 通过特定的关键字拿到其所对应的值。
        * ### add(key, value): 将一对新的键值对加入哈希表。
        * ### remove(key): 通过关键字，删除哈希表中的键值对。
        * ### getSize(): 当前键值对的数量。
        * ### isEmpty(): 查看哈希表是否为空。
* ### 實作
    ```
    from typing import Optional
    from typing import List


    class HashNode:
        def __init__(self, key: str, value: int):
            self.key: str = key
            self.value: int = value
            self.next: Optional[HashNode] = None


    class HashMap:
        def __init__(self):
            self.num_buckets: int = 5
            self.__size: int = 0

            self.bucket_array: List[HashNode | None] = [None] * self.num_buckets

        def get_bucket_index(self, key: str) -> int:
            hash_code: int = hash(key)
            index: int = hash_code % self.num_buckets
            return index

        def add(self, key: str, value: int):
            bucket_index: int = self.get_bucket_index(key)

            head: HashNode = self.bucket_array[bucket_index]

            while head is not None:
                if head.key == key:
                    head.value = value
                    return

                head = head.next

            head = self.bucket_array[bucket_index]
            hash_node: HashNode = HashNode(key, value)
            hash_node.next = head
            self.bucket_array[bucket_index] = hash_node
            self.__size += 1

            if self.__size / self.num_buckets >= 0.5:
                self.generate_bigger_array()

        def generate_bigger_array(self):
            temp: List[HashNode | None] = self.bucket_array

            self.num_buckets *= 2
            self.bucket_array: List[HashNode | None] = [None] * self.num_buckets
            self.__size = 0

            for head_node in temp:
                while head_node is not None:
                    self.add(head_node.key, head_node.value)
                    head_node = head_node.next

        def get(self, key: str) -> int:
            bucket_index: int = self.get_bucket_index(key)
            head: HashNode = self.bucket_array[bucket_index]

            while head is not None:
                if head.key == key:
                    return head.value

                head = head.next

            return -1

        def remove(self, key: str) -> int:
            bucket_index: int = self.get_bucket_index(key)
            head: HashNode = self.bucket_array[bucket_index]
            prev: Optional[HashNode] = None

            while head is not None:
                if head.key == key:
                    break

                prev = head
                head = head.next

            if head is None:
                return -1

            if prev is not None:
                prev.next = head.next
            else:
                self.bucket_array[bucket_index] = head.next

            self.__size -= 1

            return head.value

        def size(self) -> int:
            return self.__size

        def is_empty(self) -> bool:
            return self.__size == 0


    if __name__ == '__main__':
        hash_map: HashMap = HashMap()

        hash_map.add("one", 1)
        hash_map.add("two", 2)
        hash_map.add("three", 3)

        print(hash_map.get("one"))
        print(hash_map.get("two"))
        print(hash_map.get("three"))

        print("-----")

        print(hash_map.remove("three"))

        print("-----")

        print(hash_map.size())
    ```
<br />
