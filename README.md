# Implementation of famous sorting algorithms and comparing their performance

## Bubble Sort
Bubble sort is the most basic sorting method, which in each pass compares all adjacent numbers and swap them if they are in the wrong order. For example, with the first pass the largest/smallest number will end up in the last index.
- Time complexity = O(n<sup>2</sup>)
- Space complexity = O(1)

## Insertion Sort
Insertion sort works similar to the sorting of playing cards in hands. It is assumed that the first card is already sorted in the card game, and then we select an unsorted card. If the selected unsorted card is greater than the first card, it will be placed at the right side; otherwise, it will be placed at the left side. Similarly, all unsorted cards are taken and put in their exact place.
- Time complexity = O(n<sup>2</sup>)
- Space complexity = O(1)

## Merge Sort
Merge Sort is a divide and conquer algorithm. It works by recursively breaking down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly. The solutions to the sub-problems are then combined to give a solution to the original problem: 

1. If it is only one element in the list it is already sorted, return.
2. Divide the list recursively into two halves until it can no more be divided.
3. Merge the smaller lists into new list in sorted order.
- Time complexity = O(n log(n))
- Space complexity = O(n)

## Quick Sort
Quicksort first selects a pivot element and partitions the list around the pivot, putting every smaller element into a low array and every larger element into a high array. Putting every element from the low list to the left of the pivot and every element from the high list to the right positions the pivot precisely where it needs to be in the final sorted list. This means that the function can now recursively apply the same procedure to low and then high until the entire list is sorted.
- Time complexity - AVG = O(n log(n))
- Space complexity = O(log (n))

## Bucket Sort
As described in "Introduction to Algorithms" (CLRS book) Bucket sort runs in O(n) when input is drawn from a uniform distribution. The idea of bucket sort is to divide the interval [0, 1) into n equal-sized
buckets, and then distribute the n input numbers into the buckets. Since the inputs are uniformly distributed over [0, 1), we don't expect many numbers to fall into each bucket. We then simply sort the numbers in each bucket and  go through the buckets in order, listing the elements in each.

- Time complexity - AVG = O(n)
- Space complexity = O(nk)

## Performance comparison
<img src="https://github.com/mz-zarei/SortingAlgorithms/plot.png" alt="comparison" width="500"/>





