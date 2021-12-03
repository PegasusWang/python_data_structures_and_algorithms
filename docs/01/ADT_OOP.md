# Python 一切皆对象

举个例子，在 python 中我们经常使用的 list

```py
l = list()    # 实例化一个 list 对象 l
l.append(1)    # 调用 l 的 append 方法
l.append(2)
l.remove(1)
print(len(l))    # 调用对象的 `__len__` 方法
```

在后面实现新的数据类型时，我们将使用 python 的 class 实现，它包含属性和方法。
属性一般是使用某种特定的数据类型，而方法一般是对属性的操作。
这里你只需了解这么多就行了， 我们不会使用继承等特性。


# 什么是抽象数据类型 ADT

实际上 python 内置的 list 就可以看成一种抽象数据类型。

ADT: Abstract Data Type，抽象数据类型，我们在组合已有的数据结构来实现一种新的数据类型， ADT 定义了类型的数据和操作。

我们以抽象一个背包(Bag) 数据类型来说明，背包是一种容器类型，我们可以给它添加东西，也可以移除东西，并且我们想知道背包里
有多少东西。于是我们可以定义一个新的数据类型叫做 Bag.

```py
class Bag:
    """ 背包类型 """
    pass
```


# 实现一个 Bag ADT
视频中我们将使用 python 的 class 来实现一个新的容器类型叫做 Bag。


# 实现 ADT 我们应该注意什么？
- 如何选用恰当的数据结构作为存储？
- 选取的数据结构能否满足 ADT 的功能需求
- 实现效率如何？


# 小问题：
- 你了解 python 的魔术方法吗？ 比如 `__len__` ，调用 len(l) 的时候发生了什么？
- 你了解单测吗？我们以后将使用 pytest 运行单元测试，保证我们实现的数据结构和算法是正确的。你可以网上搜索下它的简单用法

# 延伸阅读：

[数据结构与算法--ADT](http://www.atjiang.com/data-structures-using-python-ADT/)

[http://www.nhu.edu.tw/~chun/CS-ch12-Abstract%20Data%20Types.pdf](http://www.nhu.edu.tw/~chun/CS-ch12-Abstract%20Data%20Types.pdf)
