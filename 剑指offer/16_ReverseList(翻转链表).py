"""
定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的头结点。链表结点定义如下：
leetcode:
https://leetcode.com/problems/reverse-linked-list/
"""

# Definition for singly-linked list.


class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        newhead = self.reverseList(head.next)
        nextnode = head.next  # head -> nextnode
        nextnode.next = head  # head <- nextnode
        head.next = None  # None -< head <= nextnode
        return newhead

    def reverseList_iter(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prenode = None
        curnode = head
        while curnode:
            nextnode = curnode.next
            curnode.next = prenode
            prenode = curnode
            curnode = nextnode
        return prenode   # 注意返回的是 prenode

    def to_list(self, head):
        res = []
        curnode = head
        while curnode:
            res.append(curnode.val)
            curnode = curnode.next
        return res


def test():
    s = Solution()
    ll = Node(1, Node(2, Node(3, Node(4))))
    head = s.reverseList(ll)
    assert s.to_list(head) == [4, 3, 2, 1]

    ll = Node(1)
    head = s.reverseList(ll)
    assert s.to_list(head) == [1]


def test_rec():
    s = Solution()
    ll = Node(1, Node(2, Node(3, Node(4))))
    head = s.reverseList(ll)
    assert s.to_list(head) == [4, 3, 2, 1]


if __name__ == '__main__':
    test()
