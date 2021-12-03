# 链式结构

上一节讲到了支持随机访问的线性结构，这次我们开始讲链式结构, 视频里我会说下这两种结构的区别，然后讲解最常见的单链表和双链表。
之前在专栏文章[那些年，我们一起跪过的算法题[视频]](https://zhuanlan.zhihu.com/p/35175401)里实现过一个 lru_cache，
使用到的就是循环双端链表，如果感觉这篇文章有点难理解，我们这里将会循序渐进地来实现。
后边讲到哈希表的冲突解决方式的时候，我们会再次提到链表。

上一节我们分析了 list 的各种操作是如何实现的，如果你还有印象的话，list
在头部进行插入是个相当耗时的操作（需要把后边的元素一个一个挪个位置）。假如你需要频繁在数组两头增删，list 就不太合适。
今天我们介绍的链式结构将摆脱这个缺陷，当然了链式结构本身也有缺陷，比如你不能像数组一样随机根据下标访问，你想查找一个元素只能老老实实从头遍历。
所以嘛，学习和了解数据结构的原理和实现你才能准确地选择到底什么时候该用什么数据结构，而不是瞎选导致代码性能很差。


# 单链表
和线性结构不同，链式结构内存不连续的，而是一个个串起来的，这个时候就需要每个链接表的节点保存一个指向下一个节点的指针。
这里可不要混淆了列表和链表（它们的中文发音类似，但是列表 list 底层其实还是线性结构，链表才是真的通过指针关联的链式结构）。
看到指针你也不用怕，这里我们用的 python，你只需要一个简单赋值操作就能实现，不用担心 c 语言里复杂的指针。

先来定义一个链接表的节点，刚才说到有一个指针保存下一个节点的位置，我们叫它 next， 当然还需要一个 value 属性保存值

```py
class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
```
然后就是我们的单链表 LinkedList ADT:

```py
class LinkedList(object):
    """ 链接表 ADT
    [root] -> [node0] -> [node1] -> [node2]
    """
```
实现我们会在视频中用画图来模拟并且手动代码实现，代码里我们会标识每个步骤的时间复杂度。这里请高度集中精力，
虽然链表的思想很简单，但是想要正确写对链表的操作代码可不容易，稍不留神就可能丢失一些步骤。
这里我们还是会用简单的单测来验证代码是否按照预期工作。

来看下时间复杂度：

链表操作                      | 平均时间复杂度 |
------------------------------|----------------|
linked_list.append(value)     | O(1)           |
linked_list.appendleft(value) | O(1)           |
linked_list.find(value)       | O(n)           |
linked_list.remove(value)     | O(n)           |


# 双链表
上边我们亲自实现了一个单链表，但是能看到很明显的问题，单链表虽然 append 是 O(1)，但是它的 find 和 remove 都是 O(n)的，
因为删除你也需要先查找，而单链表查找只有一个方式就是从头找到尾，中间找到才退出。
这里我之前提到过如果要实现一个 lru 缓存（访问时间最久的踢出），我们需要在一个链表里能高效的删除元素，
并把它追加到访问表的最后一个位置，这个时候单链表就满足不了了，
因为缓存在 dict 里查找的时间是 O(1)，你更新访问顺序就 O(n)了，缓存就没了优势。

这里就要使用到双链表了，相比单链表来说，每个节点既保存了指向下一个节点的指针，同时还保存了上一个节点的指针。

```py
class Node(object):
    # 如果节点很多，我们可以用 __slots__ 来节省内存，把属性保存在一个 tuple 而不是 dict 里
    # 感兴趣可以自行搜索  python  __slots__
    __slots__ = ('value', 'prev', 'next')

    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next
```

对， 就多了 prev，有啥优势嘛？

- 看似我们反过来遍历双链表了。反过来从哪里开始呢？我们只要让 root 的 prev 指向 tail 节点，不就串起来了吗？
- 直接删除节点，当然如果给的是一个值，我们还是需要查找这个值在哪个节点？ - 但是如果给了一个节点，我们把它拿掉，直接让它的前后节点互相指过去不就行了？哇欧，删除就是 O(1) 了，两步操作就行啦

好，废话不多说，我们在视频里介绍怎么实现一个双链表 ADT。你可以直接在本项目的 `docs/03_链表/double_link_list.py` 找到代码。
最后让我们看下它的时间复杂度:(这里 CircularDoubleLinkedList 取大写字母缩写为 cdll)

循环双端链表操作                       | 平均时间复杂度 |
---------------------------------------|----------------|
cdll.append(value)                     | O(1)           |
cdll.appendleft(value)                 | O(1)           |
cdll.remove(node)，注意这里参数是 node | O(1)           |
cdll.headnode()                        | O(1)           |
cdll.tailnode()                        | O(1)           |


# 小问题：
- 这里单链表我没有实现 insert 方法，你能自己尝试实现吗？  insert(value, new_value)，我想在某个值之前插入一个值。你同样需要先查找，所以这个步骤也不够高效。
- 你能尝试自己实现个 lru cache 吗？需要使用到我们这里提到的循环双端链表
- 借助内置的 collections.OrderedDict，它有两个方法 popitem 和 move_to_end，我们可以迅速实现一个 LRU cache。请你尝试用 OrderedDict 来实现。
- python 内置库的哪些数据结构使用到了本章讲的链式结构？


# 相关阅读

[那些年，我们一起跪过的算法题- Lru cache[视频]](https://zhuanlan.zhihu.com/p/35175401)

# 勘误：

视频中 LinkedList.remove 方法讲解有遗漏， linked_list.py 文件已经修正，请读者注意。具体请参考 [fix linked_list & add gitigonre](https://github.com/PegasusWang/python_data_structures_and_algorithms/pull/3)。视频最后增加了一段勘误说明。

# Leetcode

反转链表 [reverse-linked-list](https://leetcode.com/problems/reverse-linked-list/)

这里有一道关于 LRU 的练习题你可以尝试下。
[LRU Cache](https://leetcode.com/problems/lru-cache/description/)

合并两个有序链表 [merge-two-sorted-lists](/https://leetcode.com/problems/merge-two-sorted-lists/submissions/)
