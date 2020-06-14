"""
面试题10：二进制中1的个数
题目：请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如把9表示成二进制是1001，有2位是1。因此如果输入9，该函数输出2。""
"""


class Solution:
    def solve_wrong(self, num):
        """
        不断右移，每次和1做与运算，结果为1就加1.
        NOTE：但是输入负数会死循环。
        """
        cnt = 0
        while num:
            if num & 1:
                cnt += 1
            num >>= 1
        return cnt

    def solve(self, num):
        """
        不太能想出来：把一个数字不断和它的 num-1 与运算，能做几次就有几个 1
        用一条语句判断一个整数是不是2的整数次方。一个整数如果是2的整数次方，那么它的二进制表示中有且只有一位是1，
        而其他所有位都是0。根据前面的分析，把这个整数减去1之后再和它自己做与运算，这个整数中唯一的1就会变成0。
        """
        cnt = 0
        while num:
            num = (num - 1) & num
            cnt += 1
        return cnt

    def solve_py(self, num):
        """python有一种比较 tricky 的方式来做
        """
        s = format(num, 'b')
        return s.counts('1')


def test():
    s = Solution()
    assert s.solve(9) == 2
    assert s.solve(1) == 1
    assert s.solve(8) == 1
    assert s.solve(0) == 0


if __name__ == '__main__':
    test()
