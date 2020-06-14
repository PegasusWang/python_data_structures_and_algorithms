"""
面试题8：旋转数组的最小数字
题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
"""


class Solution:
    def findMin(self, array):
        """
        思路：二分
        关键点：旋转数组的第一个数字是前半部分最小的，也是后半部分最大的
        """
        if len(array) == 1:
            return array[0]
        first = array[0]
        size = len(array)
        beg = 1
        end = size

        while beg < end:
            mid = (beg + end) // 2
            if array[mid] > first:
                beg = mid + 1
            else:
                end = mid
        if beg == size:
            return first
        else:
            return array[beg]


def test():
    s = Solution()
    assert s.findMin([0]) == 0
    assert s.findMin([1, 2]) == 1  # 注意这个特殊case
    assert s.findMin([3, 4, 5, 1, 2]) == 1


if __name__ == '__main__':
    test()
