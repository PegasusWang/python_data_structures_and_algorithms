"""
剑指offer 第三题。从左到右升序从上到下升序数组，判断是否能找到一个值
思路：
从右上角开始找，大于 target 排除当前列。小于 target 排除当前行
"""


class Solution:
    def solve(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        leny = len(matrix)

        x = 0
        y = leny - 1

        while x >= 0 and y >= 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False


def test():
    s = Solution()
    matrix = [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15],
    ]
    assert s.solve(matrix, 0) is False
    assert s.solve(matrix, 1) is True
    assert s.solve(matrix, 7) is True
    assert s.solve(matrix, 5) is False

    # empty
    matrix = [
        [],
    ]
    assert s.solve(matrix, 0) is False


if __name__ == '__main__':
    test()
