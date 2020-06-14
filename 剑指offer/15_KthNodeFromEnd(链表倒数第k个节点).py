"""
面试题15：链表中倒数第k个结点
题目：输入一个链表，输出该链表中倒数第k个结点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾结点是倒数第1个结点。
例如一个链表有6个结点，从头结点开始它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个结点是值为4的结点。

https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

# Definition for singly-linked list.


class Node:
    def __init__(self, x=None, next=None):
        self.val = x
        self.next = next

    def __str__(self):
        return '{}'.format(self.val)
    __repr__ = __str__


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        思路：这一题的约束是只需要遍历一次。可以两个指针，相差 k 步


        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 做麻烦了，具体看 leetcode 这一题题解。加上root指向head 更容易做
        curnode = head
        prenode = behind_node = head
        for i in range(n-1):
            curnode = curnode.next
        while curnode.next:
            curnode = curnode.next
            prenode = behind_node
            behind_node = behind_node.next
        if prenode == behind_node == head:
            newhead = head.next
            del head
            return newhead
        elif prenode != behind_node:
            prenode.next = behind_node.next
            del behind_node
            return head

    def to_list(self, head):
        res = []
        cur_node = head
        while cur_node:
            res.append(cur_node.val)
            cur_node = cur_node.next
        return res


def test():
    s = Solution()
    linklist = Node(1)
    head = s.removeNthFromEnd(linklist, 1)
    assert s.to_list(head) == []

    linklist = Node(1, Node(2))
    head = s.removeNthFromEnd(linklist, 1)
    assert s.to_list(head) == [1]

    linklist = Node(1, Node(2))
    head = s.removeNthFromEnd(linklist, 2)
    assert s.to_list(head) == [2]

    linklist = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    head = s.removeNthFromEnd(linklist, 2)
    assert s.to_list(head) == [1, 2, 3, 5]

    linklist = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    head = s.removeNthFromEnd(linklist, 1)
    assert s.to_list(head) == [1, 2, 3, 4]

    linklist = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    head = s.removeNthFromEnd(linklist, 5)
    assert s.to_list(head) == [2, 3, 4, 5]


if __name__ == '__main__':
    test()
