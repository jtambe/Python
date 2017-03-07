# A solution for longest increasing subsequence in O(nlogn)



def CeilIndex(tailtable, left, right, key):

    while( right - left > 1):
        mid = left + (right -left)//2

        if tailtable[mid]  >= key:
            right = mid
        else:
            left = mid

    return right


def LISLength(arr):

    tailtable = [0]*len(arr)

    length = 0

    tailtable[0] = arr[0]
    length = 1

    for i in range(1,len(arr)):

        if arr[i] < tailtable[i]:
            tailtable[0] = arr[i]

        elif arr[i] > tailtable[length -1]:
            tailtable[length] = arr[i]
            length += 1

        else:
            tailtable[CeilIndex(tailtable,-1, len -1, arr[i])] = arr[i]


    return length




def LIS(arr):

    parent = [None]*len(arr) # store parent of the element in sequence
    increasingSub = [None]*(len(arr)+1) # store ends of each increasing subsequence
    length = 0 # length of longest increasing subsequence

    for i in range(len(arr)):
        left = 1
        right = length

        while(left <= right):

            mid = (left + right)//2
            if arr[increasingSub[mid]] < arr[i]:
                left = mid + 1
            else:
                right = mid -1

        pos = left
        parent[i]  = increasingSub[pos -1]
        increasingSub[pos] = i
        if pos > length:
            length = pos
        #return length

    LongestIncreasingSubSequence = [None]*length
    k = increasingSub[length]

    for j in reversed(range(length-1)):
        LongestIncreasingSubSequence[j] =arr[k]
        k = parent[k]

    print(LongestIncreasingSubSequence)

arr = [10,20,30,5,60,70]
arr = [3,1,5,2,6,4,9]
LISLength(arr)