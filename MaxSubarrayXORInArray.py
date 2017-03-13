



def MaxSubarrayXOR(arr):

    ans = float("-infinity")

    for i in range(len(arr)):
        curr_XOR = 0

        for j in range(i, len(arr)):
            curr_XOR = curr_XOR ^ arr[j]
            ans = max(ans, curr_XOR)

    return ans



arr = [8,1,2,12,7,6]

print(MaxSubarrayXOR(arr))
