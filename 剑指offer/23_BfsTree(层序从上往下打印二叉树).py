# -*- coding: utf-8 -*-
"""
层序遍历二叉树
"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def append(self, val):
        return self.items.append(val)

    def pop(self):
        return self.items.popleft()

    def empty(self):
        return len(self.items) == 0


class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


class Solution:
    def solve(self, root):
        if not root:
            return []
        curnodes = [root]
        nextnodes = []
        res = [root.val]  # 别忘记第一个元素的值放进去
        while curnodes:
            for node in curnodes:
                if node.left:
                    nextnodes.append(node.left)
                if node.right:
                    nextnodes.append(node.right)
            curnodes = nextnodes
            res.extend([node.val for node in nextnodes])
            nextnodes = []  # 更新nextnodes
        return res

    def solve_use_queue(self, root):
        """use queue bfs"""
        if not root:
            return []
        q = Queue()
        res = [root.val]
        q.append(root)
        while not q.empty():
            curnode = q.pop()
            if curnode.left:
                q.append(curnode.left)
                res.append(curnode.left.val)
            if curnode.right:
                q.append(curnode.right)
                res.append(curnode.right.val)
        return res


def test():
    tree = Node(1, Node(2), Node(3))
    s = Solution()
    assert s.solve(tree) == [1, 2, 3]
    assert s.solve_use_queue(tree) == [1, 2, 3]


if __name__ == '__main__':
    test()
