8 - 优先队列 PriorityQueue 與堆 Heap
=====
* ### 优先队列 PriorityQueue
    ```
    from typing import Optional


    class Node:
        def __init__(self, value: int, priority: int):
            self.value: int = value
            self.priority: int = priority
            self.next: Optional[Node] = None


    class PriorityQueue:
        def __init__(self):
            self.head: Optional[Node] = None

        def push(self, value: int, priority: int):
            new: Node = Node(value, priority)

            if self.head is None:
                self.head = new
                return

            cur: Node = self.head

            if self.head.priority < priority:
                new.next = self.head
                self.head = new
            else:
                while cur.next is not None and cur.next.priority > priority:
                    cur = cur.next

                new.next = cur.next
                cur.next = new

        def peek(self) -> Node:
            return self.head

        def pop(self) -> Node | None:
            if self.head is None:
                return None

            temp: Node = self.head
            self.head = self.head.next

            return temp

        def is_empty(self) -> bool:
            return self.head is None


    if __name__ == '__main__':
        priority_queue: PriorityQueue = PriorityQueue()

        priority_queue.push(0, 0)
        priority_queue.push(1, 1)

        print(priority_queue.pop().value)
        print(priority_queue.peek().value)
        print(priority_queue.pop().value)

        print(priority_queue.is_empty())
    ```
    * ### 复杂度分析
        * ### push: O(n)
        * ### pop: O(1)
        * ### peek: O(1)
* ### 堆 Heap: 一种特殊的平衡二叉树，堆中的节点满足以下的条件: 一个节点的父节点优先级比自己高，而自己的子节点优先级比自己低; 优先级可以根据数值的大小来决定。常见的堆有以下两种类型：
    * ### 最大堆 (Max Heap): 最大堆中根节点数值最大，所有父节点的数值比各自的子节点数值大。
    * ### 最小堆 (Min Heap): 根节点数值最小，父节点数值比其子节点数值小。
* ### 最大堆 (Max Heap) 支持操作
    * ### add: 将新元素插入堆。
    * ### poll: 将根节点 (数值最大的元素) 删除。
    * ### peek: 获取根节点的数值。
* ### 任何时间点，最大堆都应该保持其特性: 父节点的数值比所有子节点大。
* ### 在插入新元素的时候，需遵循以下步骤:
    * ### 在堆的最后新建一个节点。
    * ### 将数值赋予新节点。
    * ### 将其节点和父节点比较。
    * ### 如果新节点的数值比父节点大，调换父子节点的位置。
    * ### 重复步骤 3 和 4 直到最大堆的特性被满足。
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/DataStructuresAndAlgorithms/Basic/8/max_heap_animation.gif)
* ### 删除根节点的步骤:
    * ### 移除根节点。
    * ### 将最后的元素移到根节点处。
    * ### 将子节点和父节点比较。
    * ### 如果父节点的数值比子节点小，替换父子节点。
    * ### 重复步骤 3 和 4 直到最大堆的特性被满足。
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/DataStructuresAndAlgorithms/Basic/8/max_heap_deletion_animation.gif)
* ### 实现方式: Array
    ```
    class MaxHeap:
        def __init__(self, capacity: int):
            self.capacity: int = capacity
            self.size: int = 0
            self.array: list = [-1] * self.capacity

        @staticmethod
        def get_left_child_index(parent_index: int) -> int:
            return 2 * parent_index + 1

        def get_right_child_index(self, parent_index: int) -> int:
            return self.get_left_child_index(parent_index) + 1

        @staticmethod
        def get_parent_index(child_index: int) -> int:
            return (child_index - 1) // 2

        def has_left_child(self, index: int) -> bool:
            return self.get_left_child_index(index) < self.size

        def has_right_child(self, index: int) -> bool:
            return self.get_right_child_index(index) < self.size

        def has_parent(self, index: int) -> bool:
            return self.get_parent_index(index) >= 0

        def left_child(self, parent_index: int) -> int:
            return self.array[self.get_left_child_index(parent_index)]

        def right_child(self, parent_index: int) -> int:
            return self.array[self.get_right_child_index(parent_index)]

        def parent(self, child_index: int) -> int:
            return self.array[self.get_parent_index(child_index)]

        def insert(self, item: int):
            if self.size == self.capacity:
                self.array = self.array + [-1] * self.capacity
                self.capacity *= 2

            self.array[self.size] = item
            self.size += 1

            self.heapify_up()

        def heapify_up(self):
            index: int = self.size - 1

            while self.has_parent(index) and self.parent(index) < self.array[index]:
                parent_index: int = self.get_parent_index(index)
                self.array[parent_index], self.array[index] = self.array[index], self.array[parent_index]
                index = parent_index

        def poll(self) -> int:
            if self.size == 0:
                raise Exception

            element: int = self.array[0]
            self.array[0] = self.array[self.size - 1]
            self.size -= 1
            self.heapify_down()

            return element

        def heapify_down(self):
            index: int = 0

            while self.has_left_child(index):
                larger_child_index: int = self.get_left_child_index(index)

                if self.has_right_child(index) and self.right_child(index) > self.left_child(index):
                    larger_child_index = self.get_right_child_index(index)

                if self.array[index] < self.array[larger_child_index]:
                    self.array[index], self.array[larger_child_index] = self.array[larger_child_index], self.array[index]
                else:
                    break

                index = larger_child_index

        def peek(self) -> int:
            if self.size == 0:
                raise Exception

            return self.array[0]


    if __name__ == '__main__':
        max_heap: MaxHeap = MaxHeap(5)

        max_heap.insert(0)
        max_heap.insert(2)
        max_heap.insert(1)
        max_heap.insert(4)
        max_heap.insert(3)

        print(max_heap.peek())
        print(max_heap.poll())
        print(max_heap.peek())
    ```
<br />
