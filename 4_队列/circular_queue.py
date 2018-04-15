# -*- coding: utf-8 -*-


# NOTE: 从 array_and_list 第一章拷贝的代码
class Array(object):

    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(self._items):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class ArrayQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0

    def push(self, value):
        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value


def test_queue():
    size = 5
    q = ArrayQueue(size)
    for i in range(size):
        q.push(i)

    assert q.pop() == 0
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4
