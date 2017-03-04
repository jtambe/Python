'''

TripletsWithSumSmallerthanGivenValue

1) Sort the input array in increasing order.
2) Initialize result as 0.
3) Run a loop from i = 0 to n-2.  An iteration of this loop finds all
   triplets with arr[i] as first element.
     a) Initialize other two elements as corner elements of subarray
        arr[i+1..n-1], i.e., j = i+1 and k = n-1
     b) Move j and k toward each other until they meet, i.e., while (j < k)
            (i) if (arr[i] + arr[j] + arr[k] >= sum), then do k--

            // Else for current i and j, there can (k-j) possible third elements
            // that satisfy the constraint.
            (ii) Else Do ans += (k - j) followed by j++

'''

def TripletsWithSumSmallerthanGivenValue(arr, sum):

    #sort the array
    arr = sorted(arr)
    n = len(arr)
    #print(arr)
    #initialize result count = 0
    count = 0

    # for all elements in j
    for i in range((n - 2)+1):

        # next element of current iterator
        j = i+1
        # always start with last index, which max number for summation comparison
        k = n-1

        while(j < k):
            # if summation is greater for current index i, and elements at j and k,
            # reduce k by one as it is highest number amongst three
            if arr[i]+ arr[j] + arr[k] >= sum:
                k -= 1
            else:
                # if sum of elemtns at i,j,k is less than given sum,
                # all elements in between also have sum less than given input sum
                count += (k -j)
                j += 1

    return count



arr = [5, 1, 3, 4, 7]
#print(arr)
#find triplets with sum < 12
tripletCount = TripletsWithSumSmallerthanGivenValue(arr, 12)
print(tripletCount)
