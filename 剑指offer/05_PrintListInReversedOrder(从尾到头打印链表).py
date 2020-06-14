"""
面试题5：从尾到头打印链表
题目：输入一个链表的头结点，从尾到头反过来打印出每个结点的值。链表结点定义如下：
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


class Node:
    def __init__(self, val, next=None):
        self.val, self.next = val, next


class Solution:
    def solve(self, headnode):
        """
        思路：用一个栈保存所有节点，之后一个一个 pop
        """
        val_s = Stack()
        cur_node = headnode
        while cur_node:
            val_s.push(cur_node.val)
            cur_node = cur_node.next
        while not val_s.empty():
            print(val_s.pop())

    def solve2(self, headnode):
        """
        能用栈就可以使用递归。这一点需要能联想到
        """
        curnode = headnode
        if curnode:
            self.solve2(curnode.next)
            print(curnode.val)   # 注意 print 放到 递归之后才是倒序


def test():
    s = Solution()
    linklist = Node(0, Node(1))
    s.solve2(linklist)

    # linklist = Node(0)
    # s.solve2(linklist)

if __name__ == '__main__':
    test()
