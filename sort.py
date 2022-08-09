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
        

# from random import randint
# array = [randint(0, 100) for i in range(100)]
# array = insertion(array)
# print(array)


