"""
面试题33：把数组排成最小的数
题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3,32,321}，则打印出这3个数字能排成的最小数字321323。

类似的 leetcode 题目如下，不过是排成的最大的数字：

https://leetcode.com/problems/largest-number/

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
"""

from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums):
        """思路：直接定义比较规则就好"""
        def str_cmp(a, b):
            return int(a+b) - int(b+a)
        strs = [str(i) for i in nums]
        strs.sort(key=cmp_to_key(str_cmp), reverse=True)
        return str(int(''.join(strs)))

    def largestNumber_2(self, nums):
        """ 思路：一开始的解法，比较 ugly，把所有的数字扩充成一样长度，之后再比较
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])
        num_strs = [str(i) for i in nums]
        maxlen = len(max(num_strs, key=lambda _s: len(_s)))
        pairs = []
        for num_str in num_strs:
            if len(num_str) < maxlen:
                difflen = maxlen - len(num_str)
                max_char = max(num_str[0], num_str[-1])
                append_num_str = num_str + ''.join([max_char] * difflen)
                pairs.append((append_num_str, num_str))
            else:
                pairs.append((num_str, num_str))
        res = []
        for pair in sorted(pairs, reverse=True):
            res.append(pair[1])
        idx, size = 0, len(res)
        while res[idx] == '0' and idx != size-1:
            idx += 1
        return ''.join(res[idx:])


def test():
    s = Solution()
    assert s.largestNumber([824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247]) == '9609938824824769735703560743981399'
    assert s.largestNumber([824, 8247]) == '8248247'
    assert s.largestNumber([0, 0]) == '0'
    assert s.largestNumber([1, 1, 1]) == '111'
    assert s.largestNumber([3, 30, 34, 5, 9]) == "9534330"
    assert s.largestNumber([10, 2]) == '210'
    assert s.largestNumber([0, 2]) == '20'
    assert s.largestNumber([1]) == '1'
    assert s.largestNumber([0]) == '0'


test()
