"""
面试题39：二叉树的深度
题目一：输入一棵二叉树的根结点，求该树的深度。从根结点到叶结点依次经过的
结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。



https://leetcode.com/problems/maximum-depth-of-binary-tree/



Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if left > right:
            return left + 1
        else:
            return right + 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    if left > right:
        return left + 1
    else:
        return right + 1


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        leftd = maxDepth(root.left)
        rightd = maxDepth(root.right)
        if abs(leftd-rightd) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
