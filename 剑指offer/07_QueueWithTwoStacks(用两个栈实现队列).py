"""
面试题7：用两个栈实现队列
题目：用两个栈实现一个队列。队列的声明如下，请实现它的两个函数appendTail和deleteHead，分别完成在队列尾部插入结点和在队列头部删除结点的功能。
"""

from collections import deque


class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, val):
        return self.items.append(val)

    def pop(self):
        return self.items.pop()

    def empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def append(self, val):
        self.s1.push(val)

    def pop(self):
        if len(self.s2):
            return self.s2.pop()
        while len(self.s1):
            val = self.s1.pop()
            self.s2.push(val)
        return self.s2.pop()


def test():
    q = Queue()
    q.append(1)
    q.append(2)
    q.append(3)
    assert q.pop() == 1
    q.append(4)
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4


if __name__ == '__main__':
    test()
