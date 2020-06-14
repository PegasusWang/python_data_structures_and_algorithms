"""
面试题37：两个链表的第一个公共结点
题目：输入两个链表，找出它们的第一个公共结点。链表结点定义如下：


https://leetcode.com/problems/intersection-of-two-linked-lists/

思路：
两个链表连接以后，之后的节点都是一样的了。

1. 使用两个栈push 所有节点，然后比较栈顶元素，如果一样就 都 pop继续比较。如果栈顶不一样，结果就是上一次 pop 的值。

2. 先分别遍历两个链表，找到各自长度，然后让一个链表先走 diff(len1-len2)步骤，之后一起往前走，找到的第一个就是。

"""

# Definition for singly-linked list.


class Node(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class _Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None or (headA is None and headB is None):
            return None
        len1 = 0
        cura = headA
        while cura:
            len1 += 1
            cura = cura.next

        len2 = 0
        curb = headB
        while curb:
            len2 += 1
            curb = curb.next

        difflen = abs(len1 - len2)
        if len1 > len2:
            for i in range(difflen):
                headA = headA.next
        else:
            for i in range(difflen):
                headB = headB.next

        while headA and headB:
            if headA == headB:    # headA.val == headB.val and headA.next == headB.next
                return headA
            headA = headA.next
            headB = headB.next

        return None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        len1 = 0
        cura = headA
        while cura:
            len1 += 1
            cura = cura.next

        len2 = 0
        curb = headB
        while curb:
            len2 += 1
            curb = curb.next

        difflen = abs(len1 - len2)
        if len1 > len2:
            for i in range(difflen):
                headA = headA.next
        else:
            for i in range(difflen):
                headB = headB.next

        while headA and headB:
            if headA == headB:    # headA.val == headB.val and headA.next == headB.next
                return headA
            headA = headA.next
            headB = headB.next

        return None
