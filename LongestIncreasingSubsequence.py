# A solution for longest increasing subsequence in O(nlogn)

#credit https://github.com/mission-peace/interview/blob/master/src/com/interview/array/LongestIncreasingSubSequenceOlogNMethod.java


#Returns index in T for ceiling of s
def CeilIndex(arr, T, end, s):
    start = 0
    length = end

    while(start <= end):
        mid = (start + end)//2

        if mid < length and arr[T[mid]] < s and s <= arr[T[mid+1]]:
            return mid+1

        elif (arr[T[mid]] < s):
            start = mid + 1
        else:
            end = mid - 1


    return -1






def LISLength(arr):

    T = [0]*len(arr)
    R = [0]*len(arr)

    print(arr)
    print(T)


    for i in range(len(R)):
        R[i] = -1

    print(R)

    T[0] = 0
    length = 0

    for i in range(1,len(arr)):
        if (arr[T[0]] > arr[i]): #if input[i] is less than 0th value of T then replace it there.
            T[0] = i
        elif (arr[T[length]] < arr[i]): #if input[i] is greater than last value of T then append it in T
            length += 1
            T[length] = i
            R[T[length]] = T[length-1]
        else: #do a binary search to find ceiling of input[i] and put it there
            index = CeilIndex(arr, T, length, arr[i])
            T[index] = i
            R[T[index]] = T[index-1]


    #print increasing subsueunce in reverse
    index = T[length]
    while index != -1:
        print(arr[index], end=",")
        index = R[index]

    return length +1



arr = [10,20,30,5,60,70]
arr = [3,1,5,2,6,4,9]
LISLength(arr)