"""
面试题28：字符串的排列
题目：输入一个字符串，打印出该字符串中字符的所有排列。
例如输入字符串abc，则打印出由字符a、b、c所能排列出来的所有字符串abc、acb、bac、bca、cab和cba。

https://leetcode.com/problems/permutations/

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
  ]


https://leetcode.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution1:
    def permute(self, nums):
        """
        思路：使用递归。
        可以把问题拆解为更小的问题，分成两步走：(固定第一个字符并求解其后边数组的全排列)
        1. 首先求解可能出现在第一个位置的所有字符（即把第一个字符和后边的所有字符交换）
        2. 求该字符后的所有字符的全排列

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def _per(nums, beg, end, res):
            print(nums)
            if beg == end - 1:
                res.append(nums[:])
            else:
                for i in range(beg, end):
                    nums[i], nums[beg] = nums[beg], nums[i]
                    _per(nums, beg + 1, end, res)
                    nums[i], nums[beg] = nums[beg], nums[i]
        res = []
        _per(nums, 0, len(nums), res)
        return res


class Solution2:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        nums.sort()

        def _per(nums, beg, end, res):
            if beg == end - 1:
                res.append(nums[:])  # appen copy

            for i in range(beg, end):
                if nums[i] not in nums[beg:i]:
                    nums[i], nums[beg] = nums[beg], nums[i]
                    _per(nums, beg + 1, end, res)
                    nums[i], nums[beg] = nums[beg], nums[i]

        res = []
        _per(nums, 0, len(nums), res)
        return res


def test_per1():
    s = Solution1()
    nums = [1, 2, 3]
    for i in s.permute(nums):
        print(i, '=')


def test_per2():
    s = Solution2()
    nums = [1, 1, 2]
    for i in s.permuteUnique(nums):
        print(i, '=')
    print('\n')
    nums = [1, 2, 3]
    for i in s.permuteUnique(nums):
        print(i, '=')


def test():
    # test_per1()
    test_per2()


def perms(nums, beg, end):
    if beg == end - 1:
        print(nums)
    for i in range(beg, end):
        nums[i], nums[beg] = nums[beg], nums[i]
        perms(nums, beg + 1, end)
        nums[i], nums[beg] = nums[beg], nums[i]


if __name__ == '__main__':
    nums = [1, 2, 3]
    perms(nums, 0, len(nums))
