'''
Given an integer array of n integers, find sum of bit differences in all pairs that can be formed from array elements. Bit difference of a pair (x, y) is count of different bits at same positions in binary representations of x and y.
For example, bit difference for 2 and 7 is 2. Binary representation of 2 is 010 and 7 is 111 ( first and last bits differ in two numbers).


Input: arr[] = {1, 2}
Output: 4
All pairs in array are (1, 1), (1, 2)
                       (2, 1), (2, 2)
Sum of bit differences = 0 + 2 +
                         2 + 0
                      = 4


O(n)
'''


'''

credit: http://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/

An Efficient Solution can solve this problem in O(n) time using
the fact that all numbers are represented using 32 bits (or some fixed number of bits).
The idea is to count differences at individual bit positions.
We traverse from 0 to 31 and count numbers with i’th bit set. Let this count be ‘count’.
There would be “n-count” numbers with i’th bit not set.
So count of differences at i’th bit would be “count * (n-count) * 2”.
'''


def SumOfBitDifferences(arr):

    ans = 0
    arrayLength = len(arr)
    # since i am working on 64 bit machine

    # for each bit in all elements of array
    for i in range(64):

        count = 0
        # this part is checking all ith bits of all elements in array
        for j in range(arrayLength):

            if (arr[j] & (1 << i)):
                count += 1


        # count => number of elements with ith bit set
        # arrayLength - count => number of elements with ith bit not set
        # count * (arrayLength - count) => pairs that can be formed with such elements
        # *2 => pairs can be formed either way i.e. {1,3} and {3,1} represent 2 pairs

        ans = ans + (count * (arrayLength - count) * 2 )

    return ans


arr = [1,3,5]
print(SumOfBitDifferences(arr))