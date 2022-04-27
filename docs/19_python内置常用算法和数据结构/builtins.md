# Python 刷题常用内置算法和数据结构

相信到这里大家对常用的数据结构和算法及其实现都比较熟悉了。
之前在每章的数据结构和算法中涉及到的章节我都会提到对应的 python 内置模块，一般如果内置的可以满足需求，我们优先使用内置模块，
因为在性能和容错性方面内置模块要好于我们自己实现（比如有些是 c 实现的）。本章我们不会再对每个模块的原理详细说明，仅列举出一些常见模块供大家参考，
如果有需要最好的学习方式就是参考 Python 的官方文档。很多高级的数据结构我们也可以通过 google 搜索现成的库拿来直接用。

- 常用内置数据类型：list, tuple, dict, set, frozenset
- collections 模块：Counter(计数器), deque(双端队列), OrderedDict(有序字典)，defaultdict(默认值字典)
- heapq: 堆操作
- bisect: 二分查找

下边我列了一个常用 python 内置数据结构和算法的表格，如果有遗漏可以在 issue 中提出。确保你了解这些数据结构和算法的使用以及时间、空间复杂度。

| 数据结构/算法 | 语言内置                        | 内置库                                                                  |
|---------------|---------------------------------|-------------------------------------------------------------------------|
| 线性结构      | list(列表)/tuple(元组)          | array(数组，不常用)/collections.namedtuple                              |
| 链式结构      |                                 | collections.deque(双端队列)                                             |
| 字典结构      | dict(字典)                      | collections.Counter(计数器)/OrderedDict(有序字典)/defaultdict(默认字典) |
| 集合结构      | set(集合)/frozenset(不可变集合) |                                                                         |
| 排序算法      | sorted                          |                                                                         |
| 二分算法      |                                 | bisect模块                                                              |
| 堆算法        |                                 | heapq模块                                                               |
| 优先级队列    |                                 | queue.PriorityQueue/heapq                                               |
| 缓存算法      |                                 | functools.lru_cache(Least Recent Used, python3)/cache                   |

# 一些坑

如果你使用 python2 or python3 刷题（比如力扣leetcode），有一些坑或者技巧需要注意：

- 字典顺序。python3 和 python2 的 dict 有所用不同，python3.7 之后的 dict 会保持插入顺序(不是字典序), python2 不要依赖 dict 迭代顺序，请使用 OrderedDict
- 矩阵。正确初始化一个不可变对象的二维数组：`dp = [ [0]*col for _ in range(row) ]`，不要用 `dp = [[0] * n] * m`， 否则里边都
引用的同一个 list，修改一个都会变。`[[0 for _ in range(col)] for _ in range(row)]` 也可以(稍慢)，因为数字 0 是不可变对象
- 深浅拷贝。经常在回溯题中需要`res,path=[],[]`，path 是用来回溯的路径。找到一个结果的时候需要用 `res.append(path[:])` 而
不是`res.append(path)#错！` ，因为这里append的path的引用，之后修改了 path 结果就是错的！(或者用copy模块，不过不如[:]语法简洁)
- int范围。python在数值范围建议用：`MAXINT = 2**63-1; MININT = -2**63` 。因为 python2 sys.maxint 和 python3 sys.maxsize 不统一
- 优先级队列：使用内置queue.PriorityQueue or heapq ，定义一个 Item 类实现"小于" 魔术方法就可以实现，下边有代码演示
- 缓存。python3 的 functools 模块自带了 cache(等价于lru_cache(maxsize=None)) 和 lru_cache 装饰器，在一些需要递归记忆化搜索的时候会很方便
- 除法变更：python2和 python3 除法做了变更要注意。还有负数除法。 python2 `int(6/-123)==-1, int(-3/2)==-2`，但是 python3 `int(6/-123)==0, int(-3/2)==-1`。
正数的整数除法统一用"//"。比如二分求中间值 `mid=(l+r)//2` 或者 `mid=l+(r-l)//2`，因为python天生支持大数不会溢出两种写法都行。负数整数除法统一写 int(a/b)。
凡是遇到除法运算的题目建议统一使用 python3 提交。
- 自定义排序函数。python2 可以用 `nums.sort(cmp=lambda a, b: a - b)`，但是python3移除了cmp参数。
python3如果想要用自定义排序函数可以使用 functools.cmp_to_key 函数改成 `nums.sort(key=cmp_to_key(lambda a, b: a - b))`

# python 递归暴栈(栈溢出)

python 递归函数默认递归深度比较小，你可以通过 `sys.getrecursionlimit()` 函数打印出来。
我在 mac 机器上测试的时候，以下结果 python2 输出 1000。这就导致一些递归函数测试用例稍微多一些就会报错。
(一个用例超过上千个数据就会报错了)

```py
import sys
print(sys.getrecursionlimit()) # 我的 mac 机器上输出 1000
```

可以把以下代码设置最大栈深度，放到文件开头，在牛客上提交代码的时候可以避免一些递归代码报错。
(leetcode 似乎给设置了，类似的题目发现力扣上提交不会栈溢出但是在牛客就会)

```py
import sys
sys.setrecursionlimit(100000) # 设置函数栈深度足够大，避免栈溢出错误
```

# python int 值范围

```
# 乘方 （比较推荐，py2/3 都兼容不容易出错)
MAXINT = 2**63-1
MININT = -2**63

# py3
import sys
MAXINT = sys.maxsize
MININT = -sys.maxsize - 1

# py2
sys.maxint

# 位运算
MAXINT = (1<<63) - 1
MININT = ~MAXINT
```

# python list/dict 排序等技巧

```py
# python 根据 key，value 排序字典
d = {'d': 4, 'a': 1, 'b': 2, 'c':3}
# dict sort by key and reverse
dict(sorted(d.items()))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict(sorted(d.items(), reverse=True)) # {'d': 4, 'c': 3, 'b': 2, 'a': 1}

# dict sort by value and reverse
dict(sorted(d.items(), key = lambda kv:kv[1])) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict(sorted(d.items(), key = lambda kv:kv[1], reverse=True)) # {'d': 4, 'c': 3, 'b': 2, 'a': 1}

# 排序嵌套 list
l = [('a', 1), ('c', 2), ('b',3)]
sorted(l, key=lambda p:p[0]) # 根据第1个值排序，[('a', 1), ('b', 3), ('c', 2)]
sorted(l, key=lambda p:p[1]) # 根据第2个值排序，[('a', 1), ('c', 2), ('b', 3)]

# 同时获取最大值的下标和值
l = [1,2,5,4,3]
maxi, maxval = max(enumerate(l), key=lambda iv: iv[1]) # 2, 5

# 获取字典对应的最大值对应的 key,value
mydict = {'A':4,'B':10,'C':0,'D':87}
maximum = max(mydict, key=mydict.get)  # Just use 'min' instead of 'max' for minimum.
maxk, maxv = maximum, mydict[maximum]
# 或者
maxk, maxv = max(mydict.items(), key=lambda k: k[1])

# python3 排序list自定义函数(python2 直接用 cmp 参数)
from functools import cmp_to_key
nums = [3,2,1,4,5]
sorted(nums, key= cmp_to_key(lambda a,b: a-b) ) # [1 ,2 ,3, 4, 5]
sorted(nums, key= cmp_to_key(lambda a,b: b-a) ) # [5, 4, 3, 2, 1]

# 一行代码判断列表是否有序
issorted = all(l[i] <= l[i+1] for i in range(len(l) - 1))

# python3 一行代码求前缀和
from itertools import accumulate
presums = list(accumulate([1,2,3])) # [1, 3, 6]

# 一行代码求矩阵和 https://stackoverflow.com/questions/10713150/how-to-sum-a-2d-array-in-python
allsum = sum(map(sum, matrix)) # 或者 allsum = sum((sum(row) for row in matrix))
```

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
    实际上是利用了元组tuple比较从第一个开始比较的性质
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

    def __lt__(self, other): # heapq 源码实现只用了 小于 比较，这里定义了就可以 push 一个 item 类
        return self.weight < other.weight

#   def __eq__(self, other): # 这个可以省略，只要定义了 __lt__ 魔法函数就可以了
#       return self.weight == other.weight
#
#   def __str__(self):
#       return '{}:{}'.format(self.key,self.weight)

# Item.__lt__ = lambda self, other: self.weight < other.weight # 对于已有的类，直接加一句就可以实现作为 heap item 了

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

# python 如何实现最大堆
python自带了heapq 模块实现了最小堆(min-heaq)，但是如果想要实现最大堆(max-heap)，有几种实现方式：

1. 对放入的数字取反。比如 10 放入 -10 ，然后取出来的时候再取反。个人倾向于这种，可以自己封装一个类防止来回取反搞晕
2. 直接根据 heapq 模块的函数封装几个最大堆的函数，也是通过取反实现
3. 新建一个对象重写 `__lt__` 魔术方法。这种方式也可以，但是重写魔术方法修改了语义不太好(个人不推荐)

```py
# 方法1:封装一个 max heap 类
import heapq
class MaxHeap:
    """
    https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.minheap = []

    def push(self, val):
        heapq.heappush(self.minheap, -val)  # push取反后的数字, 1 -> -1

    def pop(self):
        val = heapq.heappop(self.minheap)
        return -val # 拿出来的数字再取反

    def max(self):
        return -self.minheap[0] # min-heap 的数组最小值是 m[0]，最大值取反

# 方法2: 重新定几个新的 max-heap 方法
import heapq
def maxheappush(h, item):
    return heapq.heappush(h, -item)

def maxheappop(h):
    return -heapq.heappop(h)

def maxheapval(h):
    return -h[0]
```

# lru_cache/cache 优化记忆化搜索

python3 functools 模块的 cache 功能和 lru_cache(maxsize=None) 一样，不过更加轻量更快。在记忆化递归搜索的时候很方便。
注意这里的参数 `maxsize=None` 一定要设置为 None，否则默认的 maxsize=128。
举一个力扣上的例子，如果不加 cache 递归函数因为会大量重复计算直接超时，但是加一个装饰器就可以通过。
当然了如果你用 python2 没有这个装饰器，你可以直接用 python 的 dict 来实现。(存在就返回，否则计算结果保存到 dict 里)

```py
"""
[337] 打家劫舍 III
https://leetcode-cn.com/problems/house-robber-iii/description/
"""
# cache 等价于 functools.lru_cache(maxsize=None), 不过python3版本低可能没有 cache 只有 lru_cache
from functools import cache, lru_cache


class Solution(object):
    def rob(self, root):
        """
        思路 1：递归求解（注意不加 cache 会超时！！)
        :type root: TreeNode
        :rtype: int
        """
        # @lru_cache(maxsize=None) # 注意如果 python3 版本不是很新的话，只能用 lru_cache(maxsize=None)
        @cache  # NOTE: 不加 cache 会直接超时，就只能用动态规划了
        def dfs(root):
            if root is None:
                return 0

            if root.left is None and root.right is None:  # 左右孩子都是空
                return root.val
            # 不偷父节点,考虑偷 root 的左右孩子
            val1 = dfs(root.left) + dfs(root.right)
            # 偷父节点
            val2 = root.val
            if root.left:
                val2 += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                val2 += dfs(root.right.left) + dfs(root.right.right)
            return max(val1, val2)

        return dfs(root)

```


# leetcode 二叉树调试函数

```py
"""
二叉树树相关问题调试函数
"""


class TreeNode(object):  # leetcode tree 节点定义
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "TreeNode:{} left:{} right:{}".format(self.val, self.left, self.right)
    __repr__ = __str__


def gen_tree_from_lc_input(vals_str):  # [1,2,3] -> root TreeNode
    """ 根据 输入生成一个 tree，返回 root 节点，注意输入字符串
    # [450] 删除二叉搜索树中的节点
    # https://leetcode-cn.com/problems/delete-node-in-a-bst/description/
    # 比如 450 题目单测代码可以这么写
    def test():
        s = Solution()
        root = gen_tree_from_lc_input("[2,1]")
        key = 1
        res = "[2]"
        assert to_lc_tree_str(s.deleteNode(root, key)) == res
    """
    import ast
    valids = vals_str.replace("null", "None")
    vals = ast.literal_eval(valids)
    # 以下就是 gen_tree 函数的内容，为了方便单独使用不调用函数了
    if not vals:
        return None
    nodemap = {}
    for i in range(len(vals)):
        if vals[i] is not None:  # 一开始写的 if vals[i]，但是 0 节点就错了! 应该显示判断是否为 None(空节点)
            nodemap[i] = TreeNode(vals[i])
        else:
            nodemap[i] = None

    root = nodemap[0]
    for i in range(len(vals)):
        l = 2*i + 1
        r = 2*i + 2
        cur = nodemap.get(i, None)
        left = nodemap.get(l, None)
        right = nodemap.get(r, None)
        if cur:
            cur.left = left
            cur.right = right
    return root


def to_lc_tree_str(root):  # root TreeNode -> [1,2,3,null]
    """返回层序序列化后的树字符串，可以和 leetcode 输出结果比对字符串"""
    import json
    if not root:
        return '[]'
    curnodes = [root]
    res = [root.val]
    while curnodes:
        nextnodes = []
        for node in curnodes:
            if node:
                if node.left:
                    nextnodes.append(node.left)
                    res.append(node.left.val)
                else:
                    nextnodes.append(None)
                    res.append(None)
                if node.right:
                    nextnodes.append(node.right)
                    res.append(node.right.val)
                else:
                    nextnodes.append(None)
                    res.append(None)
        curnodes = nextnodes

    while res[-1] is None:  # 最后空节点去掉
        res.pop()
    s = json.dumps(res)
    s = s.replace(" ", "")
    return s


def gen_tree(vals):
    """
    根据层序遍历结果生成二叉树并且返回 root。
    把题目中输入 null 换成 None
    vals = [1,2,3,None,5]
    """
    if not vals:
        return None
    nodemap = {}
    for i in range(len(vals)):
        if vals[i]:
            nodemap[i] = TreeNode(vals[i])
        else:
            nodemap[i] = None

    root = nodemap[0]
    for i in range(len(vals)):
        l = 2*i + 1
        r = 2*i + 2
        cur = nodemap.get(i, None)
        left = nodemap.get(l, None)
        right = nodemap.get(r, None)
        if cur:
            cur.left = left
            cur.right = right
    return root
```

# python 交换列表元素的坑

```
# 41. 缺失的第一个正数 https://leetcode-cn.com/problems/first-missing-positive/
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        平常习惯了 python 里边交换元素 a,b=b,a 这里你可能这么写，那就中招了!
        nums[i], nums[nums[i]-1] =  nums[nums[i]-1], nums[i] # 这么写死循环！
        这个等价于
        x, y = nums[nums[i]-1], nums[i]
        nums[i] = x  # 这一步 nums[i] 已经修改了，下边一句赋值不是期望的 nums[i]了
        nums[nums[i]-1] = y

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                # NOTE: 注意这一句交换右边有副作用的，不能颠倒！！！
                # nums[i], nums[nums[i]-1] =  nums[nums[i]-1], nums[i] # 这么写死循环！
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(n):
            if nums[i] != i+1:
                return i+1

        return n+1
```

# 兼容代码ACM/核心提交格式

注意牛客网有两种模式，一种是和 leetcode 一样的提交(无需处理输入)，只需要提交核心代码。
一种是 ACM 模式，还需要自己处理输入和输出。
建议使用这种兼容写法，同样的题目可以同时提交到 牛客、leetcode 和 acwing(python3)。
这道题目为例子 [679] 奖品分配 https://www.acwing.com/problem/content/681/

```py
# 这段代码可以直接以OJ输入模式提交，如果题目一样，直接复制 Solution 类就可以同时提交到leetcode
class Solution:
    def solve(self, scores):
        """
        思路：记忆化搜索。时间O(N)
        对于旁边都比自己大的点，它肯定是1
        对于旁边有比自己小的点，先算出比自己小的点的值再+1就好了。
        每个点如果计算过了就记忆化，下次再计算他的时候不用重复递归直接返回。
        参考：https://www.acwing.com/solution/acwing/content/1520/
        """
        from functools import lru_cache
        n = len(scores)

        @lru_cache(maxsize=None)
        def dfs(x):
            left = (x-1+n) % n
            right = (x+1) % n

            if scores[x] <= scores[left] and scores[x] <= scores[right]:  # 注意是 <= ，下边是 <
                return 1

            l, r = 0, 0
            if scores[left] < scores[x]:
                l = dfs(left)
            if scores[right] < scores[x]:
                r = dfs(right)

            return max(l, r) + 1

        return sum([dfs(i) for i in range(n)])


if __name__ == "__main__":  # python3 提交，python3 input 都当做 str 输入
    so = Solution() # 构造 Solution 实例后续调用
    n = int(input())
    for i in range(n):
        arrlen = input()
        arr = list(map(int, input().split()))
        print(so.solve(arr))
```
