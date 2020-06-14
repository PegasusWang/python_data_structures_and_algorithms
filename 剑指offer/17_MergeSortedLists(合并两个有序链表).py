"""
面试题17：合并两个排序的链表
题目：输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然是按照递增排序的

https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __str__(self):
        return '{}'.format(self.val)
    __repr__ = __str__


Node = ListNode


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        root = cur = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            cur.next = node
            cur = node
        cur.next = l1 or l2  # 链接剩余元素
        return root.next


class Solution2:

    def mergeTwoLists(self, l1, l2):
        """
        思路：使用递归简化问题，一开始想用循环来写的，比较麻烦

        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        node1, node2 = l1, l2
        head = None
        if node1.val < node2.val:
            head = node1
            head.next = self.mergeTwoLists(node1.next, node2)
        else:
            head = node2
            head.next = self.mergeTwoLists(node1, node2.next)
        return head

    def to_list(self, head):
        res = []
        curnode = head
        while curnode:
            res.append(curnode.val)
            curnode = curnode.next
        return res


def test():
    ll1 = Node(1, Node(2, Node(4)))
    ll2 = Node(1, Node(3, Node(4)))
    s = Solution()
    head = s.mergeTwoLists(ll1, ll2)
    assert s.to_list(head) == [1, 1, 2, 3, 4, 4]


if __name__ == '__main__':
    test()
