
import numpy as np


# sorting and finding median of list of 5 elements or less O(1)
def FindMedian(FiveElementArr):
    sorted(FiveElementArr)
    n = len(FiveElementArr)
    return FiveElementArr[n//2]


# partitioning array around median of median
def Partition(arr, x): # O(n)
    # print("x: "+ str(x))
    for i in range(len(arr)):
        if arr[i] == x:
            arr[i], arr[0] = arr[0], arr[i] # swap 1st element and median of median in array

    # after placing pivot element at the first position, keep sliding it till the position where
    # all elements to the left of it are smaller
    border = 0
    for i in range(len(arr)):
        if arr[i] < x:
            border += 1
            arr[border], arr[i] = arr[i], arr[border]

    # finally move the first element(pivot), and place it at border position
    arr[border], arr[0] = arr[0], arr[border]
    # print("partitioned: "+ str(arr))
    return border


# finding median of median
def MedianOfMedian(arr, k):

    if k > 0 and k <= len(arr): # as long as k is less than total number of elements in array

        n = len(arr) # length of array
        if n%5 == 0: # if length is divisible by 5
            setsOfFive = True
            median = np.zeros((n // 5)) # create median list of n//5
        else:
            setsOfFive = False
            median = np.zeros((n // 5) + 1) # else we will need one additional element of last set which is less than 5 elements

        # filling up of that median list by finding medians of each subsets of 5 and less
        i = 0
        while i < (n//5):
            medianOfEachSet = FindMedian( arr[(i*5):((i+1)*5)] )
            median[i] = medianOfEachSet
            i += 1
        if setsOfFive == False: # if there is additional subset of less than 5 elements, compute its median and add it
            medianOfLastSet = FindMedian(arr[(i*5):])
            median[i] = medianOfLastSet


        if len(median) == 1: # if recursive computation of median leaves only one element in median list
            medianOfMedian = median[0]
        else: # otherwise, keep computing till it finds the median of median
            medianOfMedian = MedianOfMedian(median, len(median) // 2)
        # medianOfMedian = median[i-1] if len(median)==1 else MedianOfMedian(median,len(median)//2)


        return medianOfMedian



def KthSmallestElement(arr,k):

    # find median of median for given array
    medianOfMedian = MedianOfMedian(arr,k)

    # find position of that median in the given array
    pos = Partition(arr, medianOfMedian)

    # pos = np.where(arr == medianOfMedian)
    # partitioned = np.partition(arr,pos)
    # pos = np.where(partitioned == medianOfMedian)

    # if position matches given k value return it
    # it compares with k-1 because position in array starts with index 0,
    # so 5th smallest element in array is at position 4, thus pos = k-1
    if pos == k-1:
        return arr[pos]
    # if position in of median is higher that needed number, find the median of median in left subarray
    if pos > k-1:
        return KthSmallestElement(arr[:pos], k)
    # if position of median is smaller, then find the median of median in right subarray
    else:
        return KthSmallestElement(arr[pos + 1:], k - pos - 1)


def main():

    arr = np.array([i for i in range(1,11)])
    arr = np.array([i for i in range(51,101)])
    arr = [19,23,85,75,114,332,45,12,142,14,565,896,4521,11,147,235]
    print(sorted(arr))
    #[11, 12, 14, 19, 23, 45, 75, 85, 114, 142, 147, 235, 332, 565, 896, 4521]


    # median = np.zeros(22//5 + 1)
    # print(median)
    ans = KthSmallestElement(arr, 5) # 23
    print("answer: " +str(ans))


if __name__ == "__main__":
    main()