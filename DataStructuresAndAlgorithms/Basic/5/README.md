5 - 堆栈和队列
=====
* ### 堆栈 (Stack)
    ```
    class Stack:
        CAPACITY: int = 1000

        def __init__(self):
            self.sta: list = [0] * Stack.CAPACITY
            self.top: int = -1

        def push(self, val: int) -> bool:
            if self.top >= Stack.CAPACITY - 1:
                return False

            self.top += 1
            self.sta[self.top] = val

        def pop(self) -> int:
            if self.top < 0:
                return -1

            ele: int = self.sta[self.top]

            self.top -= 1

            return ele

        def peek(self) -> int:
            if self.top < 0:
                return -1

            return self.sta[self.top]

        def is_empty(self) -> bool:
            return self.top < 0


    if __name__ == '__main__':
        stack: Stack = Stack()

        stack.push(0)
        stack.push(1)
        stack.push(2)

        print(stack.pop())
        print(stack.peek())
        print(stack.is_empty())
    ```
    ```
    from typing import Optional


    class StackNode:
        def __init__(self, val: int):
            self.val: int = val
            self.next: Optional[StackNode] = None


    class ListStack:
        def __init__(self):
            self.top: Optional[StackNode] = None

        def push(self, val: int):
            node: StackNode = StackNode(val)

            if self.top is None:
                self.top = node
                return

            node.next = self.top
            self.top = node

        def pop(self) -> int:
            if self.top is None:
                return -1

            val: int = self.top.val
            self.top = self.top.next

            return val

        def peek(self) -> int:
            if self.top is None:
                return -1

            return self.top.val

        def is_empty(self) -> bool:
            return self.top is None


    if __name__ == '__main__':
        stack: ListStack = ListStack()

        stack.push(0)
        stack.push(1)
        stack.push(2)

        print(stack.pop())
        print(stack.peek())
        print(stack.is_empty())
    ```
* ### 队列 (Queue)
    ```
    class ArrayQueue:
        def __init__(self, capacity: int):
            self.front: int = 0
            self.rear: int = 0
            self.size: int = 0
            self.capacity: int = capacity
            self.array: list = [-1] * self.capacity

        def enqueue(self, item: int):
            if self.is_full():
                return

            self.array[self.rear] = item
            self.rear = (self.rear + 1) % self.capacity

            self.size += 1

        def dequeue(self) -> int:
            if self.is_empty():
                return -1

            item: int = self.array[self.front]
            self.front = (self.front + 1) % self.capacity

            self.size -= 1

            return item

        def peek(self) -> int:
            if self.is_empty():
                return -1

            return self.array[self.front]

        def is_full(self) -> bool:
            return self.size == self.capacity

        def is_empty(self) -> bool:
            return self.size == 0


    if __name__ == '__main__':
        array_queue: ArrayQueue = ArrayQueue(2)

        array_queue.enqueue(0)
        array_queue.enqueue(1)

        print(array_queue.is_full())
        print(array_queue.peek())
        print(array_queue.dequeue())
        print(array_queue.dequeue())
        print(array_queue.is_empty())
    ```
    ```
    from typing import Optional


    class QueueNode:
        def __init__(self, val: int):
            self.val: int = val
            self.next: Optional[QueueNode] = None


    class ListQueue:
        def __init__(self):
            self.front: Optional[QueueNode] = None
            self.rear: Optional[QueueNode] = None

        def enqueue(self, val: int):
            node: QueueNode = QueueNode(val)

            if self.rear is None:
                self.front = self.rear = node
                return

            self.rear.next = node
            self.rear = node

        def dequeue(self) -> int:
            if self.front is None:
                return -1

            node: QueueNode = self.front
            self.front = self.front.next

            if self.front is None:
                self.rear = None

            return node.val

        def peek(self) -> int:
            if self.front is None:
                return -1

            return self.front.val

        def is_empty(self) -> bool:
            return self.front is None


    if __name__ == '__main__':
        list_queue: ListQueue = ListQueue()

        list_queue.enqueue(0)
        list_queue.enqueue(1)

        print(list_queue.peek())
        print(list_queue.dequeue())
        print(list_queue.dequeue())
        print(list_queue.is_empty())
    ```
<br />
