# -*- coding: utf-8 -*-


import random


def bubble_sort(seq):  # O(n^2), n(n-1)/2 = 1/2(n^2 + n)
    n = len(seq)
    for i in range(n-1):
        print(seq)    # 我打印出来让你看清楚每一轮最高、次高、次次高...的小朋友会冒泡到右边
        for j in range(n-1-i):  # 这里之所以 n-1 还需要 减去 i 是因为每一轮冒泡最大的元素都会冒泡到最后，无需再比较
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
        print(seq)


def test_bubble_sort():
    seq = list(range(10))  # 注意 python3 返回迭代器，所以我都用 list 强转了，python2 range 返回的就是 list
    random.shuffle(seq)   # shuffle inplace 操作，打乱数组
    sorted_seq = sorted(seq)  # 注意呦，内置的 sorted 就不是 inplace 的，它返回一个新的数组，不影响传入的参数
    bubble_sort(seq)
    assert seq == sorted_seq


def select_sort(seq):
    n = len(seq)
    for i in range(n-1):
        min_idx = i    # 我们假设当前下标的元素是最小的
        for j in range(i+1, n):    # 从 i 的后边开始找到最小的元素，得到它的下标
            if seq[j] < seq[min_idx]:
                min_idx = j    # 一个 j 循环下来之后就找到了最小的元素它的下标
        if min_idx != i:    # swap
            seq[i], seq[min_idx] = seq[min_idx], seq[i]


def test_select_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    select_sort(seq)
    assert seq == sorted_seq


def insertion_sort(seq):
    """ 每次挑选下一个元素插入已经排序的数组中,初始时已排序数组只有一个元素"""
    n = len(seq)
    print(seq)
    for i in range(1, n):
        value = seq[i]    # 保存当前位置的值，因为转移的过程中它的位置可能被覆盖
        # 找到这个值的合适位置，使得前边的数组有序 [0,i] 有序
        pos = i
        while pos > 0 and value < seq[pos-1]:
            seq[pos] = seq[pos-1]  # 如果前边的元素比它大，就让它一直前移
            pos -= 1
        seq[pos] = value    # 找到了合适的位置赋值就好
        print(seq)
