"""
面试题21：包含min函数的栈
题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min函数。在该栈中，调用min、push及pop的时间复杂度都是O（1）。

https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
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


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = Stack()
        self.mins = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.s.push(x)
        if self.mins.empty():
            self.mins.push(x)
        else:
            min_val = self.mins.top()
            if x < min_val:
                self.mins.push(x)
            else:
                self.mins.push(min_val)

    def pop(self):
        """
        :rtype: void
        """
        self.mins.pop()
        return self.s.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.s.top()

    def getMin(self):
        """Retrieve the minimum element in the stack.
        :rtype: int
        """
        return self.mins.top()


def test():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3  # --> Returns -3.
    minStack.pop()
    assert minStack.top() == 0     # --> Returns 0.
    assert minStack.getMin() == -2  # --> Returns -2.


if __name__ == '__main__':
    test()
