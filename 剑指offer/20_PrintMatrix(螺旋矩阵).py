# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/spiral-matrix/

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


# https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
看到了这个天才的解法，只需要一行

spiral_order([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

= [1, 2, 3] + spiral_order([[6, 9],
                            [5, 8],
                            [4, 7]])

= [1, 2, 3] + [6, 9] + spiral_order([[8, 7],
                                     [5, 4]])

= [1, 2, 3] + [6, 9] + [8, 7] + spiral_order([[4],
                                              [5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + spiral_order([[5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + spiral_order([])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + []

= [1, 2, 3, 6, 9, 8, 7, 4, 5]
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:  # 注意递归出口，凡是涉及递归的都要注意
            return []
        first_row = matrix.pop(0)  # 弹出第一行元素
        rotate_matrix = list(zip(*matrix))[::-1]
        return list(first_row) + self.spiralOrder(rotate_matrix)  # 注意 list(first_row)强转


def test():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s = Solution()
    assert s.spiralOrder(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


if __name__ == '__main__':
    test()
