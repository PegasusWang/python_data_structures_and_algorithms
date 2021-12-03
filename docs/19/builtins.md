# Python 常用内置算法和数据结构
相信到这里大家对常用的数据结构和算法及其实现都比较熟悉了。
之前在每章的数据结构和算法中涉及到的章节我都会提到对应的 python 内置模块，一般如果内置的可以满足需求，我们优先使用内置模块，
因为在性能和容错性方面内置模块要好于我们自己实现（比如有些是 c 实现的）。本章我们不会再对每个模块的原理详细说明，仅列举出一些常见模块供大家参考，
如果有需要最好的学习方式就是参考 Python 的官方文档。很多高级的数据结构我们也可以通过 google 搜索现成的库拿来直接用。

- 常用内置数据类型：list, tuple, dict, set, frozenset
- collections
- heapq
- bisect

下边我列了一个常用的表格，如果有遗漏可以在 issue 中提出。确保你了解这些数据结构和算法的使用以及时间、空间复杂度。

|  数据结构/算法 | 语言内置                        | 内置库                                                        |
|----------------|---------------------------------|---------------------------------------------------------------|
| 线性结构       | list(列表)/tuple(元祖)          | array(数组，不常用)/collections.namedtuple                    |
| 链式结构       |                                 | collections.deque(双端队列)                                   |
| 字典结构       | dict(字典)                      | collections.Counter(计数器)/OrderedDict(有序字典)/defaultdict |
| 集合结构       | set(集合)/frozenset(不可变集合) |                                                               |
| 排序算法       | sorted                          |                                                               |
| 二分算法       |                                 | bisect模块                                                    |
| 堆算法         |                                 | heapq模块                                                     |
| 缓存算法       |                                 | functools.lru_cache(Least Recent Used, python3)               |
