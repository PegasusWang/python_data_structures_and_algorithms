# 字典 dict

上一章我们介绍了哈希表，其实 python 内置的 dict 就是用哈希表实现的，所以这一章实现 dict 就非常简单了。
当然 cpython 使用的是 c 语言实现的，远比我们写的复杂得多 (cpython/Objects/dictobject.c)。
上一章我们用 python 自己写的一个 Array 来代表定长数组，然后用它实现的 HashTable，它支持三个最基本的方法

- add(key ,value): 有 key 则更新，否则插入
- get(key, default=None): 或者 key 的值，不存在返回默认值 None
- remove(key): 删除一个 key，这里其实不是真删除，而是标记为 Empty

字典最常使用的场景就是 k,v 存储，经常用作缓存，它的 key 值是唯一的。
内置库 collections.OrderDict 还保持了 key 的添加顺序，其实用我们之前实现的链表也能自己实现一个 OrderDict。

# 实现 dict

其实上边 HashTable 实现的三个基本方法就是我们使用字典最常用的三个基本方法， 这里我们继承一下这个类，
然后实现更多 dict 支持的方法，items(), keys(), values()。不过需要注意的是，在 python2 和 python3 里这些方法
的返回是不同的，python3 里一大改进就是不再返回浪费内存的 列表，而是返回迭代器，你要获得列表必须用 list() 转换成列表。 这里我们实现 python3 的方式返回迭代器。


```py
class DictADT(HashTable):
    pass
```

视频里我们将演示如何实现这些方法，并且写单侧验证正确性。
