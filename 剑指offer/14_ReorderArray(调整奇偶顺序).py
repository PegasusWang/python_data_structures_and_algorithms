"""
面试题14：调整数组顺序使奇数位于偶数前面
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分

https://www.lintcode.com/problem/partition-array-by-odd-and-even/description
"""


class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """

    def partitionArray(self, nums):
        """
        和快排的 partition 比较类似，只不过一个是根据数据的大小，一个是根据是否是 奇数和偶数
        """
        beg, end = 0, len(nums)-1
        while True:
            while beg < end and nums[beg] % 2 == 1:
                beg += 1
            while beg < end and nums[end] % 2 == 0:
                end -= 1
            if beg >= end:
                break
            else:
                nums[beg], nums[end] = nums[end], nums[beg]


def test():
    s = Solution()
    ll = [1, 2, 3, 4]
    s.partitionArray(ll)
    assert ll == [1, 3, 2, 4]

    ll = []
    s.partitionArray(ll)
    assert ll == []


if __name__ == '__main__':
    test()
