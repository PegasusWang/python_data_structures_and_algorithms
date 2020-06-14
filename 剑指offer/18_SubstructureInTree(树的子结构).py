"""
面试题18：树的子结构
题目：输入两棵二叉树A和B，判断B是不是A的子结构。

https://leetcode.com/problems/subtree-of-another-tree/   这一题和 leetcode 还不太一样。剑指offer 上要求是子树，
leetcode 这一题要求是严格的子树
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


class Solution:
    def isSubtree(self, s, t):
        """ TODO 思路
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        res = False
        if s and t:
            if s.val == t.val:
                res = self.is_sametree(s, t)
            if not res:
                res = self.isSubtree(s.left, t)
            if not res:
                res = self.isSubtree(s.right, t)
        return res

    def is_sametree(self, t1, t2):
        """递归判断两个树是否相同"""
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        if t1.val != t2.val:
            return False
        return self.is_sametree(t1.left, t2.left) and self.is_sametree(t1.right, t2.right)


def test():
    s = Node(3, Node(4, Node(1), Node(2)), Node(5))
    t = Node(4, Node(1), Node(2))
    so = Solution()
    assert so.isSubtree(s, t) is True

    s = Node(3, Node(4, Node(1), Node(2, Node(0))), Node(5))
    t = Node(4, Node(1), Node(2))
    so = Solution()
    assert so.isSubtree(s, t) is False


test()
