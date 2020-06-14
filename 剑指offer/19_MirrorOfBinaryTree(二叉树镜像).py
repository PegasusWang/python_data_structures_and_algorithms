"""
请完成一个函数，输入一个二叉树，该函数输出它的镜像。
https://leetcode.com/problems/invert-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class _Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root


# Definition for a binary tree node.
class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return '{}'.format(self.val)

    __repr__ = __str__


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


class Solution:  # https://leetcode.com/problems/symmetric-tree/

    def isSymmetric(self, root):
        """ use stack """
        if not root:
            return True
        s = Stack()
        s.push((root.left, root.right))  # push a tuple
        while not s.empty():
            top_vals = s.pop()
            left_node, right_node = top_vals[0], top_vals[1]
            if left_node and right_node:
                if left_node.val == right_node.val:
                    s.push((left_node.left, right_node.right))
                    s.push((left_node.right, right_node.left))
                else:
                    return False
            else:
                if left_node != right_node:
                    return False
        return True

    def isSymmetric_recursive(self, root):
        """ 判断是否是镜像，使用递归的方式
        :type root: TreeNode
        :rtype: bool
        """
        def _check(left, right):
            if left and right:
                if left.val == right.val:
                    flag1 = _check(left.left, right.right)
                    flag2 = _check(left.right, right.left)
                    return flag1 and flag2
                else:
                    return False
            else:
                return left == right  # 这种情况下 left 和 right 要么一个为 None，或者都是 None

        if root:
            return _check(root.left, root.right)
        return True

    def isSymmetric_layer(self, root):
        """ 判断是否是镜像，使用层序遍历
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        curnodes = [root]
        next_nodes = []
        while curnodes or next_nodes:
            lefts = []
            rights = []
            for node in curnodes:
                lefts.append(node.left.val if node.left else None)  # NOTE: append val not node
                rights.append(node.right.val if node.right else None)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            if lefts != rights[::-1]:
                return False

            curnodes = next_nodes
            next_nodes = []
        return True


def test():
    t = Node(1, Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))
    s = Solution()
    assert s.isSymmetric(t) is True


test()
