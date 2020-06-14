# -*- coding: utf-8 -*-
"""
面试题25：二叉树中和为某一值的路径
题目：输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

https://leetcode.com/problems/path-sum/
"""


# Definition for a binary tree node.
class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


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


class Solution:
    """
    https://leetcode.com/problems/path-sum/
    """

    def hasPathSum(self, root, sum):
        if not root:
            return False
        s = Stack()
        s.push((root, root.val))
        while not s.empty():
            topnode, val = s.pop()
            if topnode.left is None and topnode.right is None:
                if val == sum:
                    return True
            if topnode.left:
                s.push((topnode.left, val+topnode.left.val))
            if topnode.right:
                s.push((topnode.right, val+topnode.right.val))
        return False

    def _hasPathSum(self, root, sum, cursum=0):
        """思路：递归判断，如果到了叶节点（left=right=None）当前 cursum 等于sum，返回 True
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        cursum += root.val
        if root.left is None and root.right is None:
            if cursum == sum:
                return True
            else:
                cursum -= root.val
        return self._hasPathSum(root.left, sum, cursum) or self._hasPathSum(root.right, sum, cursum)


def test():
    tree = Node(1, Node(2), Node(3))
    s = Solution()
    # assert s.hasPathSum(tree, 4)

    N = Node
    tree = N(5, N(4, N(11, N(7), N(2))), N(8, N(13), N(4, None, N(1))))
    assert s.hasPathSum(tree, 22)


test()
