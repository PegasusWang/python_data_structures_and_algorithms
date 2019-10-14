"""
python3 only
LRU cache
"""
from collections import OrderedDict
from functools import wraps


def fib(n):
    if n <= 1:  # 0 or 1
        return n
    return f(n - 1) + f(n - 2)  # 由于涉及到重复计算，这个递归函数在 n 大了以后会非常慢。 O(2^n)


"""
下边就来写一个缓存装饰器来优化它。传统方法是用个数组记录之前计算过的值，但是这种方式不够 Pythonic
"""


def cache(func):
    """先引入一个简单的装饰器缓存，其实原理很简单，就是内部用一个字典缓存已经计算过的结果"""
    store = {}

    @wraps(func)
    def _(n):   # 这里函数没啥意义就随便用下划线命名了
        if n in store:
            return store[n]
        else:
            res = func(n)
            store[n] = res
            return res
    return _


@cache
def f(n):
    if n <= 1:  # 0 or 1
        return n
    return f(n - 1) + f(n - 2)


"""
问题来了，假如空间有限怎么办，我们不可能一直向缓存塞东西，当缓存达到一定个数之后，我们需要一种策略踢出一些元素，
用来给新的元素腾出空间。
一般缓存失效策略有
- LRU(Least-Recently-Used): 替换掉最近请求最少的对象，实际中使用最广。cpu缓存淘汰和虚拟内存效果好，web应用欠佳
- LFU(Least-Frequently-Used): 缓存污染问题(一个先前流行的缓存对象会在缓存中驻留很长时间)
- First in First out(FIFO)
- Random Cache: 随机选一个删除

LRU 是常用的一个，比如 redis 就实现了这个策略，这里我们来模拟实现一个。
要想实现一个 LRU，我们需要一种方式能够记录访问的顺序，并且每次访问之后我们要把最新使用到的元素放到最后（表示最新访问）。
当容量满了以后，我们踢出最早访问的元素。假如用一个链表来表示的话：

[1] -> [2] -> [3]

假设最后边是最后访问的，当访问到一个元素以后，我们把它放到最后。当容量满了，我们踢出第一个元素就行了。
一开始的想法可能是用一个链表来记录访问顺序，但是单链表有个问题就是如果访问了中间一个元素，我们需要拿掉它并且放到链表尾部。
而单链表无法在O(1)的时间内删除一个节点（必须要先搜索到它），但是双端链表可以，因为一个节点记录了它的前后节点，
只需要把要删除的节点的前后节点链接起来就行了。
还有个问题是如何把删除后的节点放到链表尾部，如果是循环双端链表就可以啦，我们有个 root 节点链接了首位节点，
只需要让 root 的前一个指向这个被删除节点，然后让之前的最后一个节点也指向它就行了。

使用了循环双端链表之后，我们的操作就都是 O(1) 的了。这也就是使用一个 dict 和一个 循环双端链表 实现LRU 的思路。
不过一般我们使用内置的 OrderedDict(原理和这个类似)就好了，要实现一个循环双端链表是一个不简单的事情，因为链表操作很容易出错。

补充：其实 lru 有个缺点就是额外的链表比较占用空间，如果你感兴趣的话可以看看 redis 如何实现的 lru 算法
"""


class LRUCache:
    def __init__(self, capacity=128):
        self.capacity = capacity
        # 借助 OrderedDict 我们可以快速实现一个 LRUCache，OrderedDict 内部其实也是使用循环双端链表实现的
        # OrderedDict 有两个重要的函数用来实现 LRU，一个是 move_to_end，一个是 popitem，请自己看文档
        self.od = OrderedDict()

    def get(self, key, default=None):
        val = self.od.get(key, default)  # 如果没有返回 default，保持 dict 语义
        self.od.move_to_end(key)   # 每次访问就把key 放到最后表示最新访问
        return val

    def add_or_update(self, key, value):
        if key in self.od:  # update
            self.od[key] = value
            self.od.move_to_end(key)
        else:  # insert
            self.od[key] = value
            if len(self.od) > self.capacity:  # full
                self.od.popitem(last=False)

    def __call__(self, func):
        """
        一个简单的 LRU 实现。有一些问题需要思考下：

        - 这里为了简化默认参数只有一个数字 n，假如可以传入多个参数，如何确定缓存的key 呢？
        - 这里实现没有考虑线程安全的问题，要如何才能实现线程安全的 LRU 呢？当然如果不是多线程环境下使用是不需要考虑的
        - 假如这里没有用内置的 dict，你能使用 redis 来实现这个 LRU 吗，如果使用了 redis，我们可以存储更多数据到服务器。而使用字典实际上是缓存了Python进程里(localCache)。
        - 这里只是实现了 lru 策略，你能同时实现一个超时 timeout 参数吗？比如像是memcache 实现的 lazy expiration 策略
        - LRU有个缺点就是，对于周期性的数据访问会导致命中率迅速下降，有一种优化是 LRU-K，访问了次数达到 k 次才会将数据放入缓存
        """
        def _(n):
            if n in self.od:
                return self.get(n)
            else:
                val = func(n)
                self.add_or_update(n, val)
                return val
        return _


@LRUCache(10)
def f_use_lru(n):
    if n <= 1:  # 0 or 1
        return n
    return f_use_lru(n - 1) + f_use_lru(n - 2)


def test():
    import time
    beg = time.time()
    for i in range(34):
        print(f(i))
    print(time.time() - beg)
    beg = time.time()
    for i in range(34):
        print(f_use_lru(i))
    print(time.time() - beg)


# TODO 要怎么给 lru 写单测？

if __name__ == '__main__':
    test()
