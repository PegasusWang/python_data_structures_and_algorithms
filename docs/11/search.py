# -*- coding: utf-8 -*-

number_list = [0, 1, 2, 3, 4, 5, 6, 7]


def linear_search(value, iterable):
    for index, val in enumerate(iterable):
        if val == value:
            return index
    return -1


assert linear_search(5, number_list) == 5


def linear_search_v2(predicate, iterable):
    for index, val in enumerate(iterable):
        if predicate(val):
            return index
    return -1


assert linear_search_v2(lambda x: x == 5, number_list) == 5


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


def binary_search_recursive(sorted_array, beg, end, val):
    if beg >= end:
        return -1
    mid = int((beg + end) / 2)  # beg + (end-beg)/2
    if sorted_array[mid] == val:
        return mid
    elif sorted_array[mid] > val:
        return binary_search_recursive(sorted_array, beg, mid, val)    # 注意我依然假设 beg, end 区间是左闭右开的
    else:
        return binary_search_recursive(sorted_array, mid+1, end, val)


def test_binary_search_recursive():
    # 我们测试所有值和边界条件
    a = list(range(10))
    for i in a:
        assert binary_search_recursive(a, 0, len(a), i) == i

    assert binary_search_recursive(a, 0, len(a), -1) == -1
    assert binary_search_recursive(a, 0, len(a), 10) == -1
