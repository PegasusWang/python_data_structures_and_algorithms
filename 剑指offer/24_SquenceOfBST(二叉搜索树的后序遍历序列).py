# -*- coding: utf-8 -*-
"""
面试题24：二叉搜索树的后序遍历序列
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回true，否则返回false。假设输入的数组的任意两个数字都互不相同。
例如输入数组{5,7,6,9,11,10,8}，则返回true，因为这个整数序列是图4.6二叉搜索树的后序遍历结果。如果输入的数组是{7,4,6,5}，由于没有哪棵二叉搜索树的后序遍历的结果是这个序列，因此返回false。

类似练习：https://leetcode.com/problems/validate-binary-search-tree/
"""


class Solution:
    def solve(self, nums):
        """考点：二叉搜索树，性质：左子树都小于根节点值，右子树都大于根节点值

        思路：递归求解
        - 注意递归出口
        - 找到左右子树
        - 判断是否右子树值都是大于根节点的，如果不是，直接 return False
        - 递归判断左子树和右子树
        """
        if len(nums) == 1:  # 递归出口，只有一个元素怎么遍历都是自己
            return True

        root_val = nums[-1]  # 后根序，根节点的值
        left_end = 0
        while nums[left_end] < root_val:
            left_end += 1
        left_part = nums[0:left_end]
        right_part = nums[left_end: -1]

        for val in right_part:
            if val < root_val:  # 右子树必须都要大于根节点的值
                return False

        return self.solve(left_part) and self.solve(right_part)


def test():
    s = Solution()
    nums = [5, 7, 6, 9, 11, 10, 8]
    assert s.solve(nums) is True

    nums = [5]
    assert s.solve(nums) is True

    nums = [7, 4, 6, 5]
    assert s.solve(nums) is False


if __name__ == '__main__':
    test()
