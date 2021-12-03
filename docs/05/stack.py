# -*- coding: utf-8 -*-

# NOTE: 这里拷贝的 double_link_list.py 里的代码

from collections import deque


class Node(object):

    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class CircularDoubleLinkedList(object):
    """循环双端链表 ADT
    多了个循环其实就是把 root 的 prev 指向 tail 节点，串起来
    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):    # O(1), 你发现一般不用 for 循环的就是 O(1)，有限个步骤
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value=value)
        tailnode = self.tailnode() or self.root

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value=value)
        if self.root.next is self.root:   # empty
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            node.prev = self.root
            headnode = self.root.next
            node.next = headnode
            headnode.prev = node
            self.root.next = node
        self.length += 1

    def remove(self, node):      # O(1)，传入node 而不是 value 我们就能实现 O(1) 删除
        """remove
        :param node  # 在 lru_cache 里实际上根据key 保存了整个node:
        """
        if node is self.root:
            return
        else:    #
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        """相比单链表独有的反序遍历"""
        if self.root.prev is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode


############################################################
# 分割线，下边是本章 内容实现
############################################################


class Deque(CircularDoubleLinkedList):   # 注意这里我们用到了继承，嗯，貌似我说过不会用啥 OOP 特性的，抱歉

    def pop(self):
        """删除尾节点"""
        if len(self) == 0:
            raise Exception('empty')
        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(tailnode)
        return value

    def popleft(self):
        if len(self) == 0:
            raise Exception('empty')
        headnode = self.headnode()
        value = headnode.value
        self.remove(headnode)
        return value


def test_deque():
    dq = Deque()
    dq.append(1)

    dq.append(2)
    assert list(dq) == [1, 2]

    dq.appendleft(0)
    assert list(dq) == [0, 1, 2]

    dq.pop()
    assert list(dq) == [0, 1]

    dq.popleft()
    assert list(dq) == [1]

    dq.pop()
    assert len(dq) == 0


class Stack(object):
    def __init__(self):
        self.deque = Deque()   # 你可以很容易替换为 python 内置的 collections.deque

    def push(self, value):
        self.deque.append(value)

    def pop(self):
        return self.deque.pop()


class Stack2(object):

    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def empty(self):
        return len(self._deque) == 0


def test_stack():
    s = Stack()
    s.push(0)
    s.push(1)
    s.push(2)

    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0

    import pytest    # pip install pytest
    with pytest.raises(Exception) as excinfo:   # 我们来测试是否真的抛出了异常
        s.pop()
    assert 'empty' in str(excinfo.value)


if __name__ == '__main__':
    test_stack()
