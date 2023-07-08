4 - 链表 LinkedList
=====
* ### 链表的类型
    * ### 单链表
    * ### 双链表
    * ### 循环链表
    * ### 块状链表
* ### 单向链表的实现
    ```
    from typing import Optional


    class Node:
        def __init__(self, val: int):
            self.val: int = val
            self.next: Optional[Node] = None


    class LinkedList:
        def __init__(self):
            self.head: Optional[Node] = None
            self.tail: Optional[Node] = None
            self.size: int = 0

        def insert(self, pos: int, num: int):
            if pos > self.size:
                return

            node: Node = Node(num)

            if pos == 0:
                node.next = self.head
                self.head = node

                if self.tail is None:
                    self.tail = node

                self.size += 1

                return

            if pos == self.size:
                self.append(num)
                return

            temp: Node = self.head
            for i in range(pos - 1):
                temp = temp.next

            node.next = temp.next
            temp.next = node

            self.size += 1

        def append(self, num: int):
            node: Node = Node(num)

            if self.tail is None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node

            self.size += 1

        def delete(self, num: int):
            if self.head is not None and self.head.val == num:
                self.head = self.head.next
                self.size -= 1

                if self.size == 0:
                    self.tail = self.head

                return

            temp: Optional[Node] = self.head

            while temp.next is not None:
                if temp.next.val == num:
                    temp.next = temp.next.next
                    self.size -= 1
                    return

                temp = temp.next

        def search(self, num: int) -> int:
            temp: Node = self.head

            for i in range(self.size):
                if temp.val == num:
                    return i

                temp = temp.next

            return -1

        def update(self, o_val: int, n_val: int):
            temp: Node = self.head

            for i in range(self.size):
                if temp.val == o_val:
                    temp.val = n_val

                temp = temp.next


    if __name__ == '__main__':
        linked_list: LinkedList = LinkedList()

        linked_list.append(0)
        linked_list.append(1)
        linked_list.append(2)

        linked_list.insert(1, 10)

        f_node: Node = linked_list.head

        c_node: Node = f_node

        while c_node is not None:
            print(c_node.val)
            c_node = c_node.next

        print("-----")

        linked_list.delete(10)

        c_node = f_node

        while c_node is not None:
            print(c_node.val)
            c_node = c_node.next

        print("-----")

        print(linked_list.search(0))
        print(linked_list.search(2))

        print("-----")

        linked_list.update(2, 100)

        c_node = f_node

        while c_node is not None:
            print(c_node.val)
            c_node = c_node.next
    ```
* ### 複雜度分析
    * ### 插入: O(n)
    * ### 刪除: O(n)
    * ### 查找: O(n)
    * ### 更新: O(n)
<br />
