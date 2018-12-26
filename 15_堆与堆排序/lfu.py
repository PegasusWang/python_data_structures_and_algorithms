"""
https://medium.com/@epicshane/a-python-implementation-of-lfu-least-frequently-used-cache-with-o-1-time-complexity-e16b34a3c49b
https://leetcode.com/problems/lfu-cache/

这里学习下 LRU(least frequently used)，就是当缓存满了之后剔除一个最少使用的 key。
"""
from collections import defaultdict, OrderedDict


class Node:
    __slots__ = 'key', 'val', 'cnt'

    def __init__(self, key, val, cnt=0):
        self.key, self.val, self.cnt = key, val, cnt


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # type {key: node}
        self.cnt2node = defaultdict(OrderedDict)
        self.mincnt = 0

    def get(self, key, default=-1):
        if key not in self.cache:
            return default

        node = self.cache[key]
        del self.cnt2node[node.cnt][key]

        if not self.cnt2node[node.cnt]:
            del self.cnt2node[node.cnt]

        node.cnt += 1
        self.cnt2node[node.cnt][key] = node

        if not self.cnt2node[self.mincnt]:
            self.mincnt += 1
        return node.val

    def put(self, key, value):
        if key in self.cache:
            self.cache[key].val = value
            self.get(key)
            return
        if len(self.cache) >= self.capacity:
            pop_key, _pop_node = self.cnt2node[self.mincnt].popitem(last=False)
            del self.cache[pop_key]

        self.cache[key] = self.cnt2node[1][key] = Node(key, value, 1)
        self.mincnt = 1


def test():
    c = LFUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    assert c.get(2) == -1
    assert c.get(3) == 3
    c.put(4, 4)
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4


if __name__ == '__main__':
    test()
