"""
面试题31：连续子数组的最大和
题目：输入一个整型数组，数组里有正数也有负数。数组中一个或连续的多个整数组成一个子数组。
求所有子数组的和的最大值。 要求时间复杂度为O（n）。

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

https://leetcode.com/problems/maximum-subarray/
"""


class Solution:
    def maxSubArray(self, nums):
        """ 动态规划问题。写出来状态转移方程。
        dp[i] = max(dp[i-1]+nums[i], dp[i])
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        size = len(nums)
        max_list = [0] * size
        for i in range(size):
            if i == 0:
                max_list[i] = nums[i]
            else:
                max_list[i] = max(nums[i] + max_list[i-1], nums[i])
        return max(max_list)


def test():
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert s.maxSubArray(nums) == 6


test()
