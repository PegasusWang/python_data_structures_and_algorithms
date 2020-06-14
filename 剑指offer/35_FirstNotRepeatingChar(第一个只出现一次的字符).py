"""
面试题35：第一个只出现一次的字符
题目：在字符串中找出第一个只出现一次的字符。如输入"abaccdeff"，则输出'b'。


https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


class Solution:
    def firstUniqChar(self, s):
        """
        思路：哈希表。
        对于范围大小确定的有限集合，字母可以看成是数字0-25。可以直接用数组来保存也可以

        变形题目：
        1. 定义一个函数，输入俩字符串，从第一个字符串中删除第二个字符串中出现过的所有字符
        2. 写一个函数删除字符串中所有重复出现的字符。
        3. 判断是否是变位词。两个单词字母和每个字母出现次数均相同
        :type s: str
        :rtype: int
        """
        chars = [0] * 26
        for char in s:
            chars[ord(char) - ord('a')] += 1
        for idx, char in enumerate(s):
            _idx = ord(char) - ord('a')
            if chars[_idx] == 1:
                return idx
        return -1


def test():
    s = Solution()
    assert s.firstUniqChar('ll') == -1
    assert s.firstUniqChar('l') == 0
    assert s.firstUniqChar('leetcode') == 0
    assert s.firstUniqChar('loveleetcode') == 2


test()
