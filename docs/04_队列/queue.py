# -*- coding: utf-8 -*-

from collections import deque

# NOTE：注意这里是第三章 linked_list.py 里的内容，为了使文件自包含，我直接拷贝过来的


class Node(object):
    def __init__(self, value=None, next=None):   # 这里我们 root 节点默认都是 None，所以都给了默认值
        self.value = value
        self.next = next

    def __str__(self):
        """方便你打出来调试，复杂的代码可能需要断点调试"""
        return '<Node: value: {}, next={}>'.format(self.value, self.next)

    __repr__ = __str__


class LinkedList(object):
    """ 链接表 ADT
    [root] -> [node0] -> [node1] -> [node2]
    """

    def __init__(self, maxsize=None):
        """
        :param maxsize: int or None, 如果是 None，无限扩充
        """
        self.maxsize = maxsize
        self.root = Node()     # 默认 root 节点指向 None
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):    # O(1)
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)    # 构造节点
        tailnode = self.tailnode
        if tailnode is None:    # 还没有 append 过，length = 0， 追加到 root 后
            self.root.next = node
        else:     # 否则追加到最后一个节点的后边，并更新最后一个节点是 append 的节点
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        """遍历 从 head 节点到 tail 节点"""
        curnode = self.root.next
        while curnode is not self.tailnode:    # 从第一个节点开始遍历
            yield curnode
            curnode = curnode.next    # 移动到下一个节点
        yield curnode

    def remove(self, value):    # O(n)
        """ 删除包含值的一个节点，将其前一个节点的 next 指向被查询节点的下一个即可

        :param value:
        """
        prevnode = self.root    #
        curnode = self.root.next
        for curnode in self.iter_node():
            if curnode.value == value:
                prevnode.next = curnode.next
                del curnode
                self.length -= 1
                return 1  # 表明删除成功
            else:
                prevnode = curnode
        return -1  # 表明删除失败

    def find(self, value):    # O(n)
        """ 查找一个节点，返回序号，从 0 开始

        :param value:
        """
        index = 0
        for node in self.iter_node():   # 我们定义了 __iter__，这里就可以用 for 遍历它了
            if node.value == value:
                return index
            index += 1
        return -1    # 没找到

    def popleft(self):    # O(1)
        """ 删除第一个链表节点
        """
        if self.root.next is None:
            raise Exception('pop from empty LinkedList')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0

######################################################
# 下边是 Queue 实现
######################################################


class EmptyError(Exception):
    """自定义异常"""
    pass


class Queue(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_link_list = LinkedList()

    def __len__(self):
        return len(self._item_link_list)

    def push(self, value):    # O(1)
        """ 队尾添加元素 """
        return self._item_link_list.append(value)

    def pop(self):
        """队列头部删除元素"""
        if len(self) <= 0:
            raise EmptyError('empty queue')
        return self._item_link_list.popleft()


def test_queue():
    q = Queue()
    q.push(0)
    q.push(1)
    q.push(2)

    assert len(q) == 3

    assert q.pop() == 0
    assert q.pop() == 1
    assert q.pop() == 2

    import pytest    # pip install pytest
    with pytest.raises(EmptyError) as excinfo:   # 我们来测试是否真的抛出了异常
        q.pop()   # 继续调用会抛出异常
    assert 'empty queue' == str(excinfo.value)


class MyQueue:
    """
    使用 collections.deque 可以迅速实现一个队列
    """
    def __init__(self):
        self.items = deque()

    def append(self, val):
        return self.items.append(val)

    def pop(self):
        return self.items.popleft()

    def __len__(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0

    def front(self):
        return self.items[0]
