# -*- coding: utf-8 -*-

"""
面试题22：栈的压入、弹出序列
题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1、2、3、4、5是某栈的压栈序列，序列4、5、3、2、1是该压栈序列对应的一个弹出序列，
但4、3、5、1、2就不可能是该压栈序列的弹出序列。

比如：
push 1
push 2
push 3
push 4
pop 4   # 4
push 5
pop 5 # 4,5
pop 3 # 4,5,3
pop 2 # 4,5,3,2
pop 1 # 4,5,3,2,1
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

    def top(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)

    __repr__ = __str__


class Solution:
    def solve(self, nums1, nums2):
        """
        思路：借助一个辅助stack
        如果下一个弹出数字刚好是栈顶数字，直接弹出。
        如果下一个弹出数字不在栈顶，把压栈序列中还没有入栈的数字push 进辅助栈，
        直到把下一个需要弹出的数字压入栈顶为止。
        如果所有数字压入栈了仍然没找到下一个弹出的数字，说明不可能是一个弹出序列。
        """
        idx1, idx2 = 0, 0
        s = Stack()

        while True:
            if s.empty() or s.top() != nums2[idx2]:
                s.push(nums1[idx1])
                idx1 += 1
            if s.top() == nums2[idx2]:
                s.pop()
                idx2 += 1
            print(s, idx1, idx2)
            if idx1 == len(nums1) and s.empty():
                return True
            # 注意最后一个判断条件，这个时候如果已经push 完了，结果栈顶还是找不到 nums2中元素，返回False
            if idx1 == len(nums1) and not s.empty() and s.top() != nums2[idx2]:
                return False


def test():
    s = Solution()
    assert s.solve([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]) is True
    assert s.solve([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) is False
    assert s.solve([1], [1]) is True
    assert s.solve([1], [2]) is False


if __name__ == '__main__':
    test()
