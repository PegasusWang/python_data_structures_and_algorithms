import random


def bubble_sort(seq):  # O(n^2), n(n-1)/2 = 1/2(n^2 + n)
    n = len(seq)
    for i in range(n-1):
        for j in range(n-1-i):  # 这里之所以 n-1 还需要 减去 i 是因为每一轮冒泡最大的元素都会冒泡到最后，无需再比较
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]


def test_bubble_sort():
    # 注意 py3 返回迭代器，所以我都用 list 强转了，py2 range return list
    seq = list(range(10))
    random.shuffle(seq)
    bubble_sort(seq)
    # 注意呦，内置的 sorted 就不是 inplace 的，它返回一个新的数组，不影响传入的参数
    assert seq == sorted(seq)
