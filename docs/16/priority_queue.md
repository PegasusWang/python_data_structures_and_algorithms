# 优先级队列
你可能比较奇怪，队列不是早就讲了嘛。这里之所以放到这里讲优先级队列，是因为虽然名字有队列，
但其实是使用堆来实现的。上一章讲完了堆，这一章我们就趁热打铁来实现一个优先级队列。


# 实现优先级队列
优先级队列(Priority Queue) 顾名思义，就是入队的时候可以给一个优先级，通常是个数字或者时间戳等，
当出队的时候我们希望按照给定的优先级出队，我们按照 TDD(测试驱动开发) 的方式先来写测试代码：

```py
def test_priority_queue():
    size = 5
    pq = PriorityQueue(size)
    pq.push(5, 'purple')    # priority, value
    pq.push(0, 'white')
    pq.push(3, 'orange')
    pq.push(1, 'black')

    res = []
    while not pq.is_empty():
        res.append(pq.pop())
    assert res == ['purple', 'orange', 'black', 'white']
```

上边就是期望的行为，写完测试代码后我们来编写优先级队列的代码，按照出队的时候最大优先级先出的顺序：


```py
class PriorityQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._maxheap = MaxHeap(maxsize)

    def push(self, priority, value):
        # 注意这里把这个 tuple push 进去，python 比较 tuple 从第一个开始比较
        # 这样就很巧妙地实现了按照优先级排序
        entry = (priority, value)    # 入队的时候会根据 priority 维持堆的特性
        self._maxheap.add(entry)

    def pop(self, with_priority=False):
        entry = self._maxheap.extract()
        if with_priority:
            return entry
        else:
            return entry[1]

    def is_empty(self):
        return len(self._maxheap) == 0
```


# 练习题
- 请你实现按照小优先级先出队的顺序的优先级队列
