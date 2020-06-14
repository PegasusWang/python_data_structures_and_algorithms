# -*- coding: utf-8 -*-
"""
面试题32：从1到n整数中1出现的次数
题目：输入一个整数n，求从1到n这n个整数的十进制表示中1出现的次数。
例如输入12，从1到12这些整数中包含1 的数字有1，10，11和12，1一共出现了5次。

思路：比较容易想出来的一种方法是从1到 n 统计每个数字包含的1。时间复杂度n*logn
"""


def numberof1(n):
    strn = str(n)
    length = len(strn)
    first = int(strn[0])
    if len(strn) == 1 and first == 0:
        return 0
    if len(strn) == 1 and first > 0:
        return 1
    # 假设 strn = "21345"
    # num_first_digit是数字 10000-19999 第一个位中的数目
    num_first_digit = 0
    if first > 1:  # 第一位不是1
        num_first_digit = power_base10(length - 1)
    elif first == 1:  # 如果第一位置是1，是后边数字+1, 12345有 2346个
        num_first_digit = int(strn[1:]) + 1

    # num_other_digits 是 1346-21345 除了第一位之外的数位中的数目
    num_other_digits = first * (length - 1) * power_base10(length - 2)

    # num_recursive 是 1-1345中的数目
    num_recursive = numberof1(strn[1:])
    return num_first_digit + num_other_digits + num_recursive


def power_base10(n):
    res = 1
    i = 0
    while i < n:
        res *= 10
        i += 1
    return res


def test():
    assert numberof1(10) == 1
    print(numberof1(21345))


test()
