# 查找

查找可以说是我们业务代码里用得最多的操作，比如我们经常需要在一个列表里找到我们需要的一个元素，然后返回它的位置。
其实之前我们介绍的哈希表就是非常高效率的查找数据结构，很明显地它是用空间换时间。这一节介绍两个基本的基于线性结构的查找。

# 线性查找
线性查找就是从头找到尾，直到符合条件了就返回。比如在一个 list 中找到一个等于 5 的元素并返回下标：

```py
number_list = [0, 1, 2, 3, 4, 5, 6, 7]


def linear_search(value, iterable):
    for index, val in enumerate(iterable):
        if val == value:
            return index
    return -1


assert linear_search(5, number_list) == 5

```
是不是 so easy。当然我们需要来一点花样，比如传一个谓词进去，你要知道，在 python 里一切皆对象，所以我们可以把函数当成一个参数传给另一个函数。

```py
def linear_search_v2(predicate, iterable):
    for index, val in enumerate(iterable):
        if predicate(val):
            return index
    return -1


assert linear_search_v2(lambda x: x == 5, number_list) == 5
```

效果是一样的，但是传入一个谓词函数进去更灵活一些，比如我们可以找到第一个大于或者小于 5 的，从而控制函数的行为。
还能玩出什么花样呢？前面我们刚学习了递归，能不能发挥自虐精神没事找事用递归来实现呢？

```py
def linear_search_recusive(array, value):
    if len(array) == 0:
        return -1
    index = len(array)-1
    if array[index] == value:
        return index
    return linear_search_recusive(array[0:index], value)


assert linear_search_recusive(number_list, 5) == 5
assert linear_search_recusive(number_list, 8) == -1
assert linear_search_recusive(number_list, 7) == 7
assert linear_search_recusive(number_list, 0) == 0
```
这里的 assert 我多写了几个，包括正常情况、异常情况和边界值等，因为递归比较容易出错。注意这里的两个递归出口。
当然业务代码里如果碰到这种问题我们肯定是选上边最直白的方式来实现，要不你的同事肯定想打你。

# 二分查找
上一小节说的线性查找针对的是无序序列，假如一个序列已经有序了呢，我们还需要从头找到尾吗？当然不用，折半(二分)是一种经典思想。日常生活中还有哪些经典的二分思想呢？

- 猜数字游戏
- 一尺之棰,日取其半,万世不竭
- 有些民间股神，告诉一堆人某个股票会涨，告诉另一半人会跌。后来真涨了，慢慢又告诉信了他的一半人另一个股票会涨，另一半说会跌。就这样韭菜多了总有一些人信奉他为股神。。。

其实之前写过博客[《抱歉，我是开发，你居然让我写单测[视频]》](https://zhuanlan.zhihu.com/p/35352024)讲过二分查找，当时主要是为了引入单元测试这个概念的，因为很多不正规的项目代码很糙，更别说写单测了。这里我就直接贴代码啦

```py
def binary_search(sorted_array, val):
    if not sorted_array:
        return -1

    beg = 0
    end = len(sorted_array) - 1

    while beg <= end:
        mid = int((beg + end) / 2)  # beg + (end-beg)/2， 为了屏蔽 python 2/3 差异我用了强转
        if sorted_array[mid] == val:
            return mid
        elif sorted_array[mid] > val:
            end = mid - 1
        else:
            beg = mid + 1
    return -1


def test_binary_search():
    a = list(range(10))

    # 正常值
    assert binary_search(a, 1) == 1
    assert binary_search(a, -1) == -1

    # 异常值
    assert binary_search(None, 1) == -1

    # 边界值
    assert binary_search(a, 0) == 0
```


# 思考题
- 给你个挑战，用递归来实现本章的二分查找。你要十分注意边界条件，注意用单测测试呦，在你写代码的时候，可能会碰到边界问题或者无穷递归等。 如果你想不起来，可以看看本章的代码示例
- 二分查找有一个变形，比如我们想在一个有序数组中插入一个值之后，数组仍保持有序，请你找出这个位置。(bisect 模块)


# 延伸阅读
这里没给链接，请善用 google 等搜索引擎和 Dash(mac) 等文档查询工具，在你学习代码的过程中你会非常频繁地使用它们。
或者如果你有时间也可以跳转到这些模块的源码，看看它们的实现方式。标准库都是些高手写的，肯定能学到一些姿势。

- 阅读 python 文档关于二分的 bisect 模块。
- 阅读 python 文档 itertools 相关模块和常见的几个函数 takewhile, dropwhile, from_iterable, count, tee 等用法
- [每个程序员都应该会点形式化证明](https://zhuanlan.zhihu.com/p/35364999?group_id=967109293607129088)


# Leetcode

[找旋转过的排序数组中最小的数 find-minimum-in-rotated-sorted-array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

[已排序的数组中找到第一和最后一个元素 find-first-and-last-position-of-element-in-sorted-array/](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/)
