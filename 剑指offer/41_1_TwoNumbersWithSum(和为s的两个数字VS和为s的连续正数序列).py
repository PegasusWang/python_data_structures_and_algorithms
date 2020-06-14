"""
2-sum问题

面试题41：和为s的两个数字VS和为s的连续正数序列
题目一：输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，
输出任意一对即可。
"""


class Solution:
    def twoSum(self, nums, target):
        """ 注意这题目 letcode 不是有序的，剑指offer 上的是有序的。一种方式是用 hash 来做
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_idx_map = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in num_idx_map:
                return [num_idx_map[diff], idx]
            else:
                num_idx_map[num] = idx

    def twoSum1(self, nums, target):
        """ 注意这题目 letcode 不是有序的，剑指offer 上的是有序的。可以先排序来做。之后首位指针向中间归并
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pairs = [(num, i) for i, num in enumerate(nums)]
        nums = sorted(pairs)
        print(nums)
        beg, end = 0, len(nums) - 1
        while beg < end:
            sum2 = nums[beg][0] + nums[end][0]
            if sum2 == target:
                break
            elif sum2 > target:
                end -= 1
            else:
                beg += 1
        return [nums[beg][1], nums[end][1]]


def test():
    s = Solution()
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([2, 7], 9) == [0, 1]
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([1, 2, 4, 7, 11, 15], 15) == [2, 4]
