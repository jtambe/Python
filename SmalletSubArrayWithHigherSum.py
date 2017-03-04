#works in O(n^2)

def LengthOfSmallestSubarrayWithSumHigher(arr, x):

    minLength = len(arr)+1
    n = len(arr)
    currentSum = 0
    start, end = 0,0

    while(end < len(arr)):

        #keep adding sum of elements while it is less than given input
        while(currentSum <= x and end < n):
            currentSum += arr[end]
            end += 1

        # if sum is greater, then move start index
        while(currentSum > x and start < n):

            # if new minlength found, assign it
            if end -start < minLength:
                minLength = end - start

            # and remove starting elements till that sum is higher than given input
            currentSum -= arr[start]
            start += 1

    return minLength

inputArr = [1, 2, 10, 5, 4, 5, 33, 21, 78]

print(LengthOfSmallestSubarrayWithSumHigher(inputArr, 70))