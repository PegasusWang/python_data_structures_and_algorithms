# python3
class MinHeap:
    def __init__(self):
        """
        这里提供一个最小堆实现。如果面试不让用内置的堆非让你自己实现的话，考虑用这个简版的最小堆实现。
        一般只需要实现 heqppop,heappush 两个操作就可以应付面试题了
        parent: (i-1)//2。注意这么写 int((n-1)/2)， python3 (n-1)//2当n=0结果是-1而不是0
        left:  2*i+1
        right: 2*i+2
        参考：
        https://favtutor.com/blogs/heap-in-python
        https://runestone.academy/ns/books/published/pythonds/Trees/BinaryHeapImplementation.html
        https://www.askpython.com/python/examples/min-heap
        """
        self.pq = []

    def min_heapify(self, nums, k):
        """递归调用，维持最小堆特性"""
        l = 2*k+1  # 左节点位置
        r = 2*k+2  # 右节点
        if l < len(nums) and nums[l] < nums[k]:
            smallest = l
        else:
            smallest = k
        if r < len(nums) and nums[r] < nums[smallest]:
            smallest = r
        if smallest != k:
            nums[k], nums[smallest] = nums[smallest], nums[k]
            self.min_heapify(nums, smallest)

    def heappush(self, num):
        """列表最后就加入一个元素，之后不断循环调用维持堆特性"""
        self.pq.append(num)
        n = len(self.pq) - 1
        # 注意必须加上n>0。因为 python3 (n-1)//2 当n==0 的时候结果是-1而不是0!
        while n > 0 and self.pq[n] < self.pq[(n-1)//2]:  # parent 交换
            self.pq[n], self.pq[(n-1)//2] = self.pq[(n-1)//2], self.pq[n]  # swap
            n = (n-1)//2

    def heqppop(self):  # 取 pq[0]，之后和pq最后一个元素pq[-1]交换之后调用 min_heapify(0)
        minval = self.pq[0]
        last = self.pq[-1]
        self.pq[0] = last
        self.min_heapify(self.pq, 0)
        self.pq.pop()
        return minval

    def heapify(self, nums):
        n = int((len(nums)//2)-1)
        for k in range(n, -1, -1):
            self.min_heapify(nums, k)


def test_MinHeqp():
    import random
    l = list(range(1, 9))
    random.shuffle(l)
    pq = MinHeap()
    for num in l:
        pq.heappush(num)
    res = []
    for _ in range(len(l)):
        res.append(pq.heqppop())  # 利用 heqppop,heqppush 实现堆排序

    def issorted(l): return all(l[i] <= l[i+1] for i in range(len(l) - 1))
    assert issorted(res)
