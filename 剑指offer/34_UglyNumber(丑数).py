"""
面试题34：丑数
题目：我们把只包含因子2、3和5的数称作丑数（Ugly Number）。求按从小到大的顺序的第1500个丑数。例如6、8都是丑数，但14不是，
因为它包含因子7。习惯上我们把1当做第一个丑数。


https://leetcode.com/problems/ugly-number/
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].



https://leetcode.com/problems/ugly-number-ii/

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.
"""


class Solution1:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        for p in (2, 3, 5):
            while num % p == 0:
                num /= p
        return num == 1


class Solution:
    def nthUglyNumber(self, n):
        """
        思路1：自增数字并且判断是否是丑数，直到找到第 n 个。效率低

        思路2：创建一个数组保存排好序的丑数。
        根据其定义，丑数应该是另一个丑数乘以2,3,5的结果(1除外)。
        可以创建一个数组，里边的数字是*排好序*的丑数，每一个丑数都是前边的丑数乘以2,3或5得到的。
        关键在于如何保证数组里的丑数是排好序的。

        :type n: int
        :rtype: int
        """
        idx2, idx3, idx5 = 0, 0, 0
        uglys = [1]
        beg = 1
        while beg < n:
            u2, u3, u5 = uglys[idx2] * 2, uglys[idx3]*3, uglys[idx5]*5
            minu = min(u2, u3, u5)
            uglys.append(minu)
            if u2 == minu:
                idx2 += 1
            if u3 == minu:
                idx3 += 1
            if u5 == minu:
                idx5 += 1
            beg += 1
        return uglys[-1]


def test_isugly():
    s = Solution1()
    assert s.isUgly(6)
    assert s.isUgly(8)
    assert s.isUgly(14) is False
    assert s.isUgly(0) is False
    assert s.isUgly(1)


def test_nth_ugly():
    s = Solution()
    assert s.nthUglyNumber(11) == 15
    assert s.nthUglyNumber(1) == 1
    assert s.nthUglyNumber(10) == 12


if __name__ == '__main__':
    test_nth_ugly()
