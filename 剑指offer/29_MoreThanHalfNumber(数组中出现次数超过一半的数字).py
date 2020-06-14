"""
面试题29：数组中出现次数超过一半的数字
题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2} 。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。

https://leetcode.com/problems/majority-element/

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2



思路：
1. nlogn 直接排序输出中位数
2. 使用快排的 partion 求中位数
3. 遍历数组，
因此我们可以考虑在遍历数组的时候保存两个值：一个是数组中的一个数字，一个是次数。当我们遍历到下一个数字的时候，
如果下一个数字和我们之前保存的数字相同，则次数加1；如果下一个数字和我们之前保存的数字不同，则次数减1。如果次数为零，
我们需要保存下 一个数字，并把次数设为1。
由于我们要找的数字出现的次数比其他所有数字出现的次数之和还要多，那么要找的数字肯定是最后一次把次数设为1时对应的数字。
"""


class Solution3:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mid = len(nums)//2
        return sorted(nums)[mid]


def partition(array, beg, end):
    """对给定数组执行 partition 操作，返回新的 pivot 位置"""
    pivot_index = beg
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end - 1    # 开区间，最后一个元素位置是 end-1     [0, end-1] or [0: end)，括号表示开区间

    while True:
        # 从左边找到比 pivot 大的
        while left <= right and array[left] < pivot:
            left += 1

        while right >= left and array[right] >= pivot:
            right -= 1

        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    array[pivot_index], array[right] = array[right], array[pivot_index]
    return right   # 新的 pivot 位置


def nth_element(array, beg, end, nth):
    """查找一个数组第 n 大元素"""
    if beg < end:
        pivot_idx = partition(array, beg, end)
        if pivot_idx == nth - 1:    # 数组小标从 0 开始
            return array[pivot_idx]
        elif pivot_idx > nth - 1:
            return nth_element(array, beg, pivot_idx, nth)
        else:
            return nth_element(array, pivot_idx + 1, end, nth)


class Solution2:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mid = len(nums)//2+1
        return nth_element(nums, 0, len(nums), mid)  # 自己写的 partition 超时了


class Solution:
    def majorityElement(self, nums):
        """有一个次数过半，说明他出现的次数比其他所有次数和还多。
        思路：
        设置两个变量一个记录次数times，一个记录当前数字cur。
        如果下一个数字等于当前数字，times+1，否则times-1。
        如果times为0，把times重新置位1，然后赋值为当前 cur。最后返回cur 就是需要找的值
        :type nums: List[int]
        :rtype: int
        """
        cur = nums[0]
        times = 1
        for i in range(1, len(nums)):
            if nums[i] == cur:
                times += 1
            else:
                times -= 1
                if times == 0:
                    times = 1
                    cur = nums[i]
        return cur


def test():
    s = Solution()
    assert s.majorityElement([3, 2, 3]) == 3
    assert s.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2


test()
