# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Mohammad Zarei
# Created Date: 9 Aug 2022
# ---------------------------------------------------------------------------
"""Implementation of famous sorting algorithms
    Insertion sort
    Bubble sort
    Merge sort
    Quick sort
    Heap sort
"""
# ---------------------------------------------------------------------------
from cmath import inf
from itertools import count
from random import randint

def bubble(array):
    """
    Bubble sort
        time: O(n^2) 
        space: O(1)
    """

    N = len(array)

    for i in range(N):
        array_sorted = True
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
                array_sorted = False
        if array_sorted:
            break
    
    return array


def insertion(array):
    """
    Insertion sort
        time: O(n^2) 
        space: O(1)
    """
    N = len(array)
    for i in range(1, N):
        key = array[i]
        j = i-1
        while j>=0 and key<array[j]:
            array[j] = array[j+1]
            j -= 1
        array[j+1] = key
    return array


def merge(array):
    """
    Merge sort
        time: O(n log n) 
        space: O(n)
    """
    if len(array) < 2:
        return array
    
    mid = len(array) // 2

    return _merge(merge(array[:mid]), merge(array[mid:]))



def quick(array):
    """
    Quick sort
        time: O(n log n) 
        space: O(log n)
    """
    if len(array) < 2:
        return array
    
    low, same, high = [], [], []
    pivot_ind = randint(0, len(array)-1)

    for num in array:
        if num == array[pivot_ind]:
            same.append(num)
        elif num > array[pivot_ind]:
            high.append(num)
        else:
            low.append(num)
    
    return quick(low)+same+quick(high)



def bucket(array, num_buckets = 10):
    """
    Bucket sort
        time (avg): O(n) 
        space: O(n * num_buckets)
    """
    MAX = max(array)
    buckets = [[] for _ in range(num_buckets)]

    for value in array:
        buckets[int(value/MAX * num_buckets -1)].append(value)

    result = []
    for i in range(num_buckets):
        buckets[i] = insertion(buckets[i])
        result += buckets[i]

    return result


def counting(array, upper=None, lower=0):
    """
    Counting sort
        time: O(n * MAX) 
        space: O(MAX)
    """

    if len(array) <= 1:
        return array

    if not upper:
        upper = float(-inf)
        lower = float(inf)
        for num in array:
            if num < lower:
                lower = num
            if num > upper:
                upper = num
    counts = [0]*(upper - lower + 1)
    for num in array:
        counts[num-lower] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]
    
    ordered = array[:]
    
    for i in range(len(array) - 1, -1, -1):
        num = array[i]
        ordered[counts[num-lower] - 1] = num
        counts[num-lower] -= 1

    return ordered


def radix(array):
    """
    Radix sort
        time: O(n * k), k: length of longest number
        space: O(n + k)
    """
    MAX = max(array)
    div = 1

    while MAX/div > 1:
        
        counts = [0] * 10
        for num in array:
            digit = (num // div) % 10
            counts[digit] += 1
        for i in range(1, 10):
            counts[i] += counts[i - 1]
        res = array[:]
        for i in range(len(array) - 1, -1, -1):
            num =array[i]
            digit = (num // div) % 10
            res[counts[digit] - 1] = num
            counts[digit] -= 1
        div *= 10
        array = res[:]

    return res









def _merge(left, right):

    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    
    merged = []
    r = l = 0

    while len(merged) < len(left)+len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
        
        if r == len(right):
            merged += left[l:]
            break

        if l == len(left):
            merged += right[r:]
            break
    return merged


# from random import randint
# array = [randint(0, 100) for i in range(10)]
# array = radix(array)
# print(array)


