"""
面试题38：数字在排序数组中出现的次数
题目：统计一个数字在排序数组中出现的次数。例如输入排序数组{1,2,3,3,3,3,4,5}和数字3，由于3在这个数组中出现了4次，因此输出4


https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


def find_left(array, beg, end, target):
    while beg < end:
        mid = (beg + end) // 2
        if target > array[mid]:
            beg = mid + 1
        else:
            end = mid
    if beg != len(array) and array[beg] == target:
        return beg
    return -1


def find_right(nums, beg, end, target):
    while beg < end:
        mid = (beg + end) >> 1
        if target >= nums[mid]:  # 条件是>=，找到之后beg会在 target 后一个位置
            beg = mid + 1
        else:
            end = mid
    before = beg - 1
    if before != len(nums) and nums[before] == target:
        return before
    return -1


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        l = find_left(nums, 0, len(nums), target)
        r = find_right(nums, 0, len(nums), target)
        return [l, r]


def test_left():
    nums = [5, 7, 7, 8, 8, 10]
    assert find_left(nums, 0, len(nums), 5) == 0
    assert find_left(nums, 0, len(nums), 10) == 5
    assert find_left(nums, 0, len(nums), 8) == 3
    assert find_left(nums, 0, len(nums), 9) == -1
    assert find_left(nums, 0, len(nums), 4) == -1


def test_right():
    nums = [5, 7, 7, 8, 8, 10]
    assert find_right(nums, 0, len(nums), 5) == 0
    assert find_right(nums, 0, len(nums), 10) == 5
    assert find_right(nums, 0, len(nums), 11) == -1
    assert find_right(nums, 0, len(nums), 8) == 4


def test():
    s = Solution()
    assert s.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]


test_left()
test_right()
