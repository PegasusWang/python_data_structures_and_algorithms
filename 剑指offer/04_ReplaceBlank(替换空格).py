"""
替换字符串中的空格
题目：请实现一个函数，把字符串中的每个空格替换成"%20"。例如输入“We are happy.”，则输出“We%20are%20happy.”
"""


class Solution:
    def solve(self, string):
        """因为 python string 不可变对象，和其他的语言用字符串数组能直接修改有点区别"""
        res = []
        for char in string:
            if char == ' ':
                res.append('%20')
            else:
                res.append(char)
        return ''.join(res)

    def solve2(self, string):
        """
        思路：
        先遍历一次计算替换后的总长度
        从后往前替换，防止从前往后需要
        """
        pass


def test():
    s = Solution()
    ss = 'We are happy.'
    assert s.solve(ss) == 'We%20are%20happy.'

    assert s.solve('') == ''


if __name__ == '__main__':
    test()
