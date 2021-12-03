# 字典 dict

上一章我们介绍了哈希表，其实 python 内置的 dict 就是用哈希表实现的，所以这一章实现 dict 就非常简单了。
当然 cpython 使用的是 c 语言实现的，远比我们写的复杂得多 (cpython/Objects/dictobject.c)。
上一章我们用 python 自己写的一个 Array 来代表定长数组，然后用它实现的 HashTable，它支持三个最基本的方法

- add(key ,value): 有 key 则更新，否则插入
- get(key, default=None): 或者 key 的值，不存在返回默认值 None
- remove(key): 删除一个 key，这里其实不是真删除，而是标记为 Empty

字典最常使用的场景就是 k,v 存储，经常用作缓存，它的 key 值是唯一的。
内置库 collections.OrderedDict 还保持了 key 的添加顺序，其实用我们之前实现的链表也能自己实现一个 OrderedDict。

# 实现 dict ADT

其实上边 HashTable 实现的三个基本方法就是我们使用字典最常用的三个基本方法， 这里我们继承一下这个类，
然后实现更多 dict 支持的方法，items(), keys(), values()。不过需要注意的是，在 python2 和 python3 里这些方法
的返回是不同的，python3 里一大改进就是不再返回浪费内存的 列表，而是返回迭代器，你要获得列表必须用 list() 转换成列表。 这里我们实现 python3 的方式返回迭代器。


```py
class DictADT(HashTable):
    pass
```

视频里我们将演示如何实现这些方法，并且写单测验证正确性。

# Hashable
作为 dict 的 key 必须是可哈希的，也就是说不能是 list 等可变对象。不信你在 ipython 里运行如下代码：

```py
d = dict()
d[[1]] = 1
# TypeError: unhashable type: 'list'
```

我引用 python 文档里的说法，大家可以自己理解下：

```
An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__() method), and can be compared to other objects (it needs an __eq__() or __cmp__() method). Hashable objects which compare equal must have the same hash value.

Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally.

All of Python’s immutable built-in objects are hashable, while no mutable containers (such as lists or dictionaries) are. Objects which are instances of user-defined classes are hashable by default; they all compare unequal (except with themselves), and their hash value is derived from their id().
```


# 思考题：
- 你能在哈希表的基础上实现 dict 的其他操作吗？
- 对于 python 来说，哪些内置数据类型是可哈希的呢？list, dict, tuple, set 等类型哪些可以作为字典的 key 呢?
- 你了解可变对象和不可变对象的区别吗？
- 你了解 python 的 hash 函数吗？你了解 python 的`__hash__`  和 `__eq__` 魔术方法吗？它们何时被调用

# 延伸阅读
阅读 python 文档关于 dict 的相关内容
