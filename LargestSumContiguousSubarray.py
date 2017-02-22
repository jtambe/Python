def LargestSumContiguousSubarray(a):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1,len(a)):
        curr_max = max(a[i], curr_max+a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far



def main():
    a = [4,2,-8,1,-7,3,2]
    print(LargestSumContiguousSubarray(a))

if __name__ == "__main__":
    main()