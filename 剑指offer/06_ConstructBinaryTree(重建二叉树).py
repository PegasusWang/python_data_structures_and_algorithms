"""
面试题6：重建二叉树
题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建出图2.6所示的二叉树并输出它的头结点。二叉树结点的定义如下：<Paste>
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


class Solution:
    def __init__(self):
        self.pres = []
        self.inorders = []

    def solve(self, prevals, invals):
        """
        思路：先序找到根，然后可以找到中序遍历根的位置确定左子树和右子树，递归处理
        """
        if not prevals or not invals:
            return None
        root_val = prevals[0]
        root = Node(root_val)
        inorder_root_idx = invals.index(root_val)
        left_length = inorder_root_idx
        right_length = len(invals) - inorder_root_idx - 1

        if left_length:
            root.left = self.solve(prevals[1:1 + left_length], invals[:inorder_root_idx])

        if right_length:
            root.right = self.solve(prevals[left_length + 1:], invals[inorder_root_idx + 1:])
        return root

    def inorder(self, subtree):
        if subtree:
            self.inorder(subtree.left)
            self.inorders.append(subtree.val)
            self.inorder(subtree.right)

    def preorder(self, subtree):
        if subtree:
            self.pres.append(subtree.val)
            self.preorder(subtree.left)
            self.preorder(subtree.right)


def test():
    s = Solution()
    prevals = [1, 2, 4, 7, 3, 5, 6, 8]
    invals = [4, 7, 2, 1, 5, 3, 8, 6]
    root = s.solve(prevals, invals)
    s.inorder(root)
    assert s.inorders == invals

    s.preorder(root)
    assert s.pres == prevals


if __name__ == '__main__':
    test()
