# Implementation of famous sorting algorithms and comparing their performance

## Selection Sort
This sorting algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from the unsorted part and putting it at the beginning. 
- Time complexity = O(n<sup>2</sup>)
- Space complexity = O(1)
- Useful when:
    - the array is small.
    - memory space is limited.

## Bubble Sort
Bubble sort is the most basic sorting method, which in each pass compares all adjacent numbers and swap them if they are in the wrong order. For example, with the first pass the largest/smallest number will end up in the last index.
- Time complexity = O(n<sup>2</sup>)
- Space complexity = O(1)
- Useful when:
    - array is extremely small.
    - array is early sorted set of data.

## Insertion Sort
Insertion sort works similar to the sorting of playing cards in hands. It is assumed that the first card is already sorted in the card game, and then we select an unsorted card. If the selected unsorted card is greater than the first card, it will be placed at the right side; otherwise, it will be placed at the left side. Similarly, all unsorted cards are taken and put in their exact place.
- Time complexity = O(n<sup>2</sup>)
- Space complexity = O(1)
- Useful when:
    - the array is small or nearly sorted.
    - memory space is limited.
    - the elements compared equally need to retain their original order (stablity).

## Merge Sort
Merge Sort is a divide and conquer algorithm. It works by recursively breaking down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly. The solutions to the sub-problems are then combined to give a solution to the original problem: 

1. If it is only one element in the list it is already sorted, return.
2. Divide the list recursively into two halves until it can no more be divided.
3. Merge the smaller lists into new list in sorted order.
- Time complexity = O(n log(n))
- Space complexity = O(n)
- Useful for:
    - linked lists which doesn???t support random access
    - stable sorting

## Quick Sort
Quicksort first selects a pivot element and partitions the list around the pivot, putting every smaller element into a low array and every larger element into a high array. Putting every element from the low list to the left of the pivot and every element from the high list to the right positions the pivot precisely where it needs to be in the final sorted list. This means that the function can now recursively apply the same procedure to low and then high until the entire list is sorted.
- Time complexity - AVG = O(n log(n))
- Space complexity = O(log (n))
- Useful for:
    - array that can fit in memory (i.e. not good for very large arrays)

## Bucket Sort
As described in "Introduction to Algorithms" (CLRS book) Bucket sort runs in O(n) when input is drawn from a uniform distribution. The idea of bucket sort is to divide the interval [0, 1) into n equal-sized
buckets, and then distribute the n input numbers into the buckets. Since the inputs are uniformly distributed over [0, 1), we don't expect many numbers to fall into each bucket. We then simply sort the numbers in each bucket and  go through the buckets in order, listing the elements in each.
- Time complexity - AVG = O(n)
- Space complexity = O(nk)
- Useful for:
    - arrays with uniformly distributed numbers.

## Counting Sort
Counting sort is a sorting algorithm that sorts the elements of an array by counting the number of occurrences of each unique element in the array. The count is stored in an auxiliary array and the sorting is done by mapping the count as an index of the auxiliary array.

- Time complexity = O(n * MAX)
- Space complexity = O(MAX)
- Useful for:
    - arrays having a range of less than size of array

## Radix Sort
Radix sort is an integer sorting algorithm that sorts data with integer keys by grouping the keys by individual digits that share the same significant position and value (place value). Radix sort uses counting sort as a subroutine to sort an array of numbers.

- Time complexity = O(n * max_digit_num) 
- Space complexity = O(n + max_digit_num)
- Useful for:
    - lexicographically sorting (strings)
    - running algorithm on parallel machines
    - stably sorting


## Performance comparison
<img src="https://github.com/mz-zarei/SortingAlgorithms/blob/master/plot.png" alt="comparison" width="500"/>





