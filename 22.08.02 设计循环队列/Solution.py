from Cython.Compiler.ExprNodes import ListNode


class MyCircularQueue:

    def __init__(self, k: int):
        self.head= self.tail = None
        self.capacity = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        node = ListNode(value) # 链表
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.size -= 1
        return True

    def Front(self) -> int:
        return  -1 if self.isEmpty() else self.head.val

    def Rear(self) -> int:
        return  -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()