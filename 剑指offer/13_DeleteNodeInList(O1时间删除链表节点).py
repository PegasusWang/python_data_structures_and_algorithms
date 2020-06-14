"""
面试题13：在O（1）时间删除链表结点
题目：给定单向链表的头指针和一个结点指针，定义一个函数在O（1）时间删除该结点。链表结点与函数的定义如下：

https://leetcode.com/problems/delete-node-in-a-linked-list/
"""


class Node:
    def __init__(self, val, next=None):
        self.val, self.next = val, next


class Solution:
    def solve(self, headnode, target_node):
        """
        传统方法是从头遍历到要删除的节点，然后让前一个节点指向下一个节点。
        思路：把下一个节点节点复制到当前节点就好了。但是要注意只有一个节点的情况
        - 链表只有一个节点
        - 链表有多个节点并且不是尾节点
        - 链表有多个节点并且是尾节点（此时不存在下一个节点了，需要从头遍历）
        """
        if not headnode or not target_node:
            return

        if target_node.next:
            next_node = target_node.next
            target_node.next = next_node.next
            target_node.val = next_node.val
            del next_node

        elif target_node == headnode:
            headnode.next = None
            del target_node

        else:  # O(n) 删除
            cur_node = headnode
            while cur_node:
                if cur_node.next == target_node:
                    cur_node.next = target_node.next
                    del target_node
                    break
                cur_node = cur_node.next
