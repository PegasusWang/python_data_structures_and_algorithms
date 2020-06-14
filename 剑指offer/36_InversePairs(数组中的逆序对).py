"""
面试题36：数组中的逆序对
题目：在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。
“例如在数组{7,5,6,4}中，一共存在5个逆序对，分别是（7,6）、（7,5）、（7,4）、（6,4）和（5,4）。”

https://www.lintcode.com/problem/reverse-pairs/

思路1：扫描整个数组，寻找每个数字后边小于它的。O(n^2)
思路2：类似归并排序的思路。
"""


class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """

    def reversePairs(self, A):
        """做归并排序的同时计数
        """
        count = 0

        def merge(A, beg, end):
            nonlocal count
            if beg == end - 1:
                return [A[beg]]
            mid = (beg + end) // 2
            left = merge(A, beg, mid)
            right = merge(A, mid, end)
            copy = [None] * (len(left) + len(right))
            i = len(left) - 1
            j = len(right) - 1
            k = len(left) + len(right) - 1
            while i >= 0 and j >= 0:
                if left[i] > right[j]:
                    count += j + 1
                    copy[k] = left[i]
                    i -= 1
                    k -= 1
                else:
                    copy[k] = right[j]
                    k -= 1
                    j -= 1
            if i >= 0:
                copy[0:i + 1] = left[0:i + 1]
            if j >= 0:
                copy[0:j + 1] = right[0:j + 1]
            return copy

        res = merge(A, 0, len(A))
        print(res, '|||||')
        return count


def test():
    s = Solution()
    assert s.reversePairs([2]) == 0
    assert s.reversePairs([2, 4, 1, 3, 5]) == 3
    assert s.reversePairs([2, 1]) == 1
    assert s.reversePairs([2]) == 0


test()
