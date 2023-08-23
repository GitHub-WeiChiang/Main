class OurQueue:
    def __init__(self):
        self.in_stack: list = []
        self.out_stack: list = []

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)

    def push(self, obj):
        self.in_stack.append(obj)

    def pop(self):
        if not self.out_stack:
            self.out_stack = self.in_stack[::-1]
            self.in_stack = []

        return self.out_stack.pop()


if __name__ == '__main__':
    our_queue: OurQueue = OurQueue()
    our_queue.push(1)
    our_queue.push(2)
    print(our_queue.pop())
    print(our_queue.pop())
    our_queue.push(3)
    print(our_queue.pop())
