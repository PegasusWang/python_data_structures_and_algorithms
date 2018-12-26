# -*- coding: utf-8 -*-


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def print_num(n):
    for i in range(1, n + 1):    # 注意很多编程语言使用的都是 从 0 开始的左闭右开区间, python 也不例外
        print(i)


def print_num_recursive(n):
    if n > 0:
        print_num_recursive(n - 1)
        print(n)


def print_num_recursive_revserve(n):
    if n > 0:
        print(n)
        print_num_recursive_revserve(n - 1)


from collections import deque


class Stack(object):
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def is_empty(self):
        return len(self._deque) == 0


def print_num_use_stack(n):
    s = Stack()
    while n > 0:    # 不断将参数入栈
        s.push(n)
        n -= 1

    while not s.is_empty():    # 参数弹出
        print(s.pop())


def hanoi_move(n, source, dest, intermediate):
    if n >= 1:  # 递归出口，只剩一个盘子
        hanoi_move(n - 1, source, intermediate, dest)
        print("Move %s -> %s" % (source, dest))
        hanoi_move(n - 1, intermediate, dest, source)


def flatten(rec_list):
    for i in rec_list:
        if isinstance(i, list):
            for i in flatten(i):
                yield i
        else:
            yield i


def test_flatten():
    assert list(flatten([[[1], 2, 3], [1, 2, 3]])) == [1, 2, 3, 1, 2, 3]
