# Python 常用内置算法和数据结构

相信到这里大家对常用的数据结构和算法及其实现都比较熟悉了。
之前在每章的数据结构和算法中涉及到的章节我都会提到对应的 python 内置模块，一般如果内置的可以满足需求，我们优先使用内置模块，
因为在性能和容错性方面内置模块要好于我们自己实现（比如有些是 c 实现的）。本章我们不会再对每个模块的原理详细说明，仅列举出一些常见模块供大家参考，
如果有需要最好的学习方式就是参考 Python 的官方文档。很多高级的数据结构我们也可以通过 google 搜索现成的库拿来直接用。

- 常用内置数据类型：list, tuple, dict, set, frozenset
- collections 模块：Counter(计数器), deque(双端队列), OrderedDict(有序字典)，defaultdict(默认值字典)
- heapq: 堆操作
- bisect: 二分查找

下边我列了一个常用 python 内置数据结构和算法的表格，如果有遗漏可以在 issue 中提出。确保你了解这些数据结构和算法的使用以及时间、空间复杂度。

| 数据结构/算法 | 语言内置                        | 内置库                                                        |
|---------------|---------------------------------|---------------------------------------------------------------|
| 线性结构      | list(列表)/tuple(元祖)          | array(数组，不常用)/collections.namedtuple                    |
| 链式结构      |                                 | collections.deque(双端队列)                                   |
| 字典结构      | dict(字典)                      | collections.Counter(计数器)/OrderedDict(有序字典)/defaultdict |
| 集合结构      | set(集合)/frozenset(不可变集合) |                                                               |
| 排序算法      | sorted                          |                                                               |
| 二分算法      |                                 | bisect模块                                                    |
| 堆算法        |                                 | heapq模块                                                     |
| 优先级队列    |                                 | queue.PriorityQueue                                           |
| 缓存算法      |                                 | functools.lru_cache(Least Recent Used, python3)               |

# 一些坑

如果你经常使用 python2 or python3 刷题（比如力扣leetcode），有一些坑或者技巧需要注意：

- python3 和 python2 的 dict 有所用不同，python3.7 之后的 dict 会保持插入顺序, python2 不要依赖 dict 迭代顺序，请使用 OrderedDict
- 正确初始化一个二维数组：`dp = [[0 for _ in range(col)] for _ in range(row)]`，不要用 `dp = [[0] * n] * m`， 否则里边都
引用的同一个 list，修改一个都会变
- python在数值范围建议用：`MAXINT = 2**63-1; MININT = -2**63` 。因为 python2 sys.maxint 和 python3 sys.maxsize 不统一
- 优先级队列：使用内置的 heapq ，定义一个 Item 类实现"小于" 魔术方法就可以实现


# 链表题目调试函数

```py
# 编写链表题目经常用到的一些通用函数和调试函数，定义等，方便代码调试

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return 'Node({})'.format(self.val)

    # 用来输出调试
    __repr__ = __str__


# 缩写，单测方便写，比如构建链表 1->2->3  N(1, N(2, N(3)))
N = Node = ListNode


def to_list(head):
    """linked list to python []"""
    res = []
    curnode = head
    while curnode:
        res.append(curnode.val)
        curnode = curnode.next
    return res


def gen_list(nums):
    """用数组生成一个链表方便测试 [1,2,3] 1->2->3
    """
    if not nums:
        return None
    head = ListNode(nums[0])
    pre = head
    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        pre.next = node
        pre = node
    return head


def print_list(head):
    """打印链表"""
    cur = head
    res = ""
    while cur:
        res += "{}->".format(cur.val)
        cur = cur.next
    res += "nil"
    print(res)
```


# 内置库实现优先级队列的三种方式

```py
def test_buildin_PriorityQueue():  # python3
    """
    测试内置的 PriorityQueue
    https://pythonguides.com/priority-queue-in-python/
    """
    from queue import PriorityQueue
    q = PriorityQueue()
    q.put((10, 'Red balls'))
    q.put((8, 'Pink balls'))
    q.put((5, 'White balls'))
    q.put((4, 'Green balls'))
    while not q.empty():
        item = q.get()
        print(item)


def test_buildin_heapq_as_PriorityQueue():
    """
    测试使用 heapq 实现优先级队列，保存一个 tuple 比较元素(tuple第一个元素是优先级)
    """
    import heapq
    s_roll = []
    heapq.heappush(s_roll, (4, "Tom"))
    heapq.heappush(s_roll, (1, "Aruhi"))
    heapq.heappush(s_roll, (3, "Dyson"))
    heapq.heappush(s_roll, (2, "Bob"))
    while s_roll:
        deque_r = heapq.heappop(s_roll)
        print(deque_r)


# python3 没有了 __cmp__ 魔法函数 https://stackoverflow.com/questions/8276983/why-cant-i-use-the-method-cmp-in-python-3-as-for-python-2
class Item:
    def __init__(self, key, weight):
        self.key, self.weight = key, weight

    def __lt__(self, other): # 看其来 heapq 实现只用了 小于 比较，这里定义了就可以 push 一个 item 类
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __str__(self):
        return '{}:{}'.format(self.key,self.weight)


def test_heap_item():
    """
    测试使用 Item 类实现优先级队列，因为 heapq 内置使用的是小于运算法，
    重写魔术 < 比较方法即可实现
    """
    import heapq
    pq = []
    heapq.heappush(pq, Item('c', 3))
    heapq.heappush(pq, Item('a', 1))
    heapq.heappush(pq, Item('b', 2))
    while pq:
        print(heapq.heappop(pq))
```
