# -*- coding: utf-8 -*-

# 从数组和列表章复制的代码


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


class Slot(object):
    """定义一个 hash 表 数组的槽
    注意，一个槽有三种状态，看你能否想明白。相比链接法解决冲突，二次探查法删除一个 key 的操作稍微复杂。
    1.从未使用 HashMap.UNUSED。此槽没有被使用和冲突过，查找时只要找到 UNUSED 就不用再继续探查了
    2.使用过但是 remove 了，此时是 HashMap.EMPTY，该探查点后边的元素扔可能是有key
    3.槽正在使用 Slot 节点
    """

    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable(object):

    UNUSED = None    # 没被使用过的槽，作为该类变量的一个单例，下边都是is 判断
    EMPTY = Slot(None, None)     # 使用过但是被删除的槽

    def __init__(self):
        self._table = Array(7)
        self.length = 0

    @property
    def _load_factor(self):
        # load factor 超过 2/3 就重新分配空间
        return self.length / float(len(self._table))

    def __len__(self):
        return self.length

    def _hash1(self, key):
        """ 计算key的hash值"""
        return abs(hash(key)) % len(self._table)

    def _find_slot(self, key, for_insert=False):
        """_find_slot

        :param key:
        :param for_insert: 是否插入，还是仅仅查询
        :return:  slot index or None
        """
        index = self._hash1(key)
        base_index = index
        hash_times = 1
        _len = len(self._table)

        if not for_insert:  # 查找是否存在 key
            while self._table[index] is not HashTable.UNUSED:
                if self._table[index] is HashTable.EMPTY:
                    index = (base_index + hash_times * hash_times) % _len    # 一个简单的二次方探查
                    continue
                elif self._table[index].key == key:
                    return index
                index = (base_index + hash_times * hash_times) % _len
                hash_times += 1
            return None
        else:
            while not self._slot_can_insert(index):  # 循环直到找到一个可以插入的槽
                index = (base_index + hash_times * hash_times) % _len
                hash_times += 1
            return index

    def _slot_can_insert(self, index):
        return (self._table[index] is HashTable.EMPTY or self._table[index] is HashTable.UNUSED)

    def __contains__(self, key):   # in operator
        index = self._find_slot(key, for_insert=False)
        return index is not None

    def add(self, key, value):
        if key in self:    # key 相同值不一样的时候，用新的值
            index = self._find_slot(key, for_insert=False)
            self._table[index].value = value
            return False
        else:
            index = self._find_slot(key, for_insert=True)
            self._table[index] = Slot(key, value)
            self.length += 1
            if self._load_factor >= 0.8:    # 注意超过了 阈值 rehashing
                self._rehash()
            return True

    def _rehash(self):
        old_table = self._table
        newsize = len(self._table) * 2 + 1   # 扩大 2*n + 1
        self._table = Array(newsize)

        self.length = 0

        for slot in old_table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                index = self._find_slot(slot.key, for_insert=True)
                self._table[index] = slot
                self.length += 1

    def get(self, key, default=None):
        index = self._find_slot(key, for_insert=False)
        if index is None:
            return default
        else:
            return self._table[index].value

    def remove(self, key):
        assert key in self, 'keyerror'
        index = self._find_slot(key, for_insert=False)
        value = self._table[index].value
        self.length -= 1
        self._table[index] = HashTable.EMPTY
        return value

    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot.key   # 和 python dict 一样，默认遍历 key，需要value 的话写个 items() 方法


#########################################
# 上边是从 哈希表章 拷贝过来的代码，我们会直接继承 HashTable 实现 dict
#########################################

class DictADT(HashTable):

    def _iter_slot(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot

    def items(self):
        for slot in self._iter_slot():
            yield (slot.key, slot.value)

    def keys(self):
        for slot in self._iter_slot():
            yield slot.key

    def values(self):
        for slot in self._iter_slot():
            yield slot.value


def test_dict_adt():
    import random
    d = DictADT()
    l = list(range(30))
    random.shuffle(l)
    for i in l:
        d.add(i, i)

    for i in range(30):
        assert d.get(i) == i

    assert sorted(list(d.keys())) == sorted(l)
