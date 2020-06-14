"""
面试题30：最小的k个数
题目：输入n个整数，找出其中最小的k个数。例如输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
这道题最简单的思路莫过于把输入的n个整数排序，排序之后位于最前面的k个数就是最小的k个数。这种思路的时间复杂度是O（nlogn），面试官会提示我们还有更快的算法。


思路1：O(n)
如果能修改数组，我们可以用 parittion 函数求前 k 个(前k 个最小的，不一定是排序的)

思路2：nlogk
适合大数据处理，用一个最大堆
"""

import heapq


class MaxHeap:
    """
    https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
    py 的 heapq 模块提供了方便的最小堆，但是最大堆需要我们自己实现。
    有两种方式实现：
    1. 对放入的数字取反。比如 10 放入 -10 ，然后取出来的时候再取反。个人喜欢这种方式
    2. 新建一个对象重写 __lt__ 方法。这种方式也可以，但是重写魔术方法修改了语义不太好

    import heapq

    class MaxHeapObj(object):
        def __init__(self,val): self.val = val
        def __lt__(self,other): return self.val > other.val
        def __eq__(self,other): return self.val == other.val
        def __str__(self): return str(self.val)
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.minheap = []

    def push(self, val):
        heapq.heappush(self.minheap, -val)  # 取反后的数字

    def pop(self):
        val = heapq.heappop(self.minheap)
        return -val

    def max(self):
        return -self.minheap[0]

    def __iter__(self):
        for val in self.minheap:
            yield -val


def test_maxheap():
    mh = MaxHeap(3)
    mh.push(2)
    mh.push(1)
    mh.push(3)
    assert mh.max() == 3
    assert mh.pop() == 3
    assert mh.pop() == 2
    assert mh.pop() == 1


class Solution:

    def min_k(self, nums, k):
        """最小的 k 个数字
        分析时间复杂度
        """
        maxheap = MaxHeap(k)
        for idx, val in enumerate(nums):
            if idx < k:
                maxheap.push(val)
            else:
                maxval = maxheap.max()
                if val < maxval:
                    maxheap.pop()
                    maxheap.push(val)
        return [i for i in maxheap]


def test():
    s = Solution()
    nums = [4, 5, 1, 6, 2, 7, 3, 8]
    res = s.min_k(nums, 4)
    assert sorted(res) == [1, 2, 3, 4]
