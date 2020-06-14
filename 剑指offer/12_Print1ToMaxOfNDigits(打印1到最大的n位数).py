"""
面试题12：打印1到最大的n位数
题目：输入数字n，按顺序打印出从1最大的n位十进制数。比如输入3，则打印出1、2、3一直到最大的3位数即999。

思路：不能上来直接模拟。时间复杂度太大。
因为 python 其实支持大数字运算，不需要像其他语言一样使用数组模拟大数。
"""


class Solution:
    def solve(self, n):
        """递归的思路输出所有排列"""
        nums = [0] * n
        self._solve(nums, 0, n)

    def _solve(self, nums, beg, end):
        if beg == end:
            print(nums)
            return
        for i in range(10):
            nums[beg] = i
            self._solve(nums, beg + 1, end)


def test():
    s = Solution()
    s.solve(9)


if __name__ == '__main__':
    test()
