"""

题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O（n），
空间复杂度是O（1）。

我们还是从头到尾依次异或数组中的每一个数字，那么最终得到的结果就是两个只出现一次的数字的异或结果。因为其他数字都出现了两次，
在异或中全部抵消了。由于这两个数字肯定不一样，那么异或的结果肯定不为0，也就是说在这个结果数字的二进制表示中至少就有一位为1。
我们在结果数字中找到第一个为1的位的位置，记为第n位。现在我们以第n位是不是1为标准把原数组中的数字分成两个子数组
，第一个子数组中每个数字的第n位都是1，而第二个子数组中每个数字的第n位都是0。由于我们分组的标准是数字中的某一位是1还是0，
那么出现了两次的数字肯定被分配到同一个子数组。因为两个相同的数字的任意一位都是相同的，我们不可能把两个相同的数字分配到两个子数组中去，
于是我们已经把原数组分成了两个子数组，每个子数组都包含一个只出现一次的数字，而其他数字都出现了两次。
我们已经知道如何在数组中找出唯一一个只出现一次数字，因此到此为止所有的问题都已经解决了。



https://leetcode.com/problems/single-number-iii/

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""


class Solution1:
    def singleNumber(self, nums):
        """
        类似题：求只出现一次的数字，其他都出现两次。
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        for num in nums:
            first ^= num
        return first


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def get_single_num(nums):
            first = 0
            for num in nums:
                first ^= num
            return first

        single = get_single_num(nums)
        print(single)
        mask = 1
        while single & mask == 0:
            mask = mask << 1

        print(mask, '||||||||||||||||||')
        left = [i for i in nums if i & mask]
        right = [i for i in nums if not(i & mask)]
        return [get_single_num(left), get_single_num(right)]


class Solution(object):
    def singleNumber(self, nums):
        """
        思路：异或。

        136 题做过只出现一次的一个数字，本题有两个只出现一次的数字。
        核心在于把数组分成两个。怎么分组呢？

        假设只出现一次的数字式 x1,x2，所有元素异或结果是 x。一定有 x=x1^x2。
        x不能是0，否则x1==x2，就不是只出现一次的数字了。
        *可以用位运算 x&-x 取出x 二进制位最低位的 1，设其实是第 L 位置。*
        可以据此分类数组，一组是二进制第 L位置为 0 的数字，一组L 位置为 1的数字。
        x1,x2会分别出现在两个组中。这样第一组全部异或得到x1, 第二组全部异或得到 x2

        :type nums: List[int]
        :rtype: List[int]
        """
        x = 0
        for num in nums:
            x ^= num

        low1pos = x & -x  # 这里也可以用移位运算，x&-x 不太好想，类似上边那个解法
        x1, x2 = 0, 0

        for num in nums:
            if num & low1pos:
                x1 ^= num
            else:
                x2 ^= num

        return x1, x2


def test():
    s = Solution()
    assert s.singleNumber([1, 2, 1, 3, 2, 5]) == [3, 5]


test()
