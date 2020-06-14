"""
面试题27：二叉搜索树与双向链表
题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
比如输入图4.12中左边的二叉搜索树，则输出转换之后的排序双向链表。

https://www.lintcode.com/problem/convert-binary-search-tree-to-doubly-linked-list/description

Description
Convert a binary search tree to doubly linked list with in-order traversal.

Have you met this question in a real interview?
Example
Given a binary search tree:

    4
   / \
  2   5
 / \
1   3
return 1<->2<->3<->4<->5

"""


# Definition of Doubly-ListNode
class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = None  # nextDefinition of TreeNode:


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """ 用了一种有点 tricky 的方式，中序遍历输出所有节点以后拼成链表
    @param root: The root of tree
    @return: the head of doubly list node
    """

    def bstToDoublyList(self, root):
        if not root:
            return None
        vals = []
        self.inorder(root, vals)
        prevnode = head = DoublyListNode(vals[0])
        for idx in range(1, len(vals)):
            node = DoublyListNode(vals[idx])
            node.prev = prevnode
            prevnode.next = node
            prevnode = node
        return head

    def inorder(self, subtree, vals):
        if subtree:
            self.inorder(subtree.left, vals)
            vals.append(subtree.val)
            self.inorder(subtree.right, vals)


def test():
    pass
