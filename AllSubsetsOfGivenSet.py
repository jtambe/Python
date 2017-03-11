


# Find all subsets of given set
# credits: http://www.geeksforgeeks.org/finding-all-subsets-of-a-given-set-in-java/

# Input: Set[], set_size
# 1. Get the size of power set
#     powet_set_size = pow(2, set_size)
# 2  Loop for counter from 0 to pow_set_size
#      (a) Loop for i = 0 to set_size
#           (i) If ith bit in counter is set
#                Print ith element from set for this subset
#      (b) Print seperator for subsets i.e., newline

def getSubsets(arr):

    allSubsets = []
    arrayLength = len(arr)
    max = 1 << len(arr) # powet_set_size = pow(2, set_size)

    for i in range(max): # (a) Loop for i = 0 to set_size

        subset = []
        print("{" , end="")
        for j in range(arrayLength):

            if((i & (1 << j)) > 0): # If ith bit in counter is set
                subset.append(arr[j]) # gives list of lists
                print(str(arr[j]) + " ", end="") # Print ith element from set for this subset

        print("}", end="")
        allSubsets.append(subset)

    print('\n')
    return  allSubsets




#driver
arr = [1,2,3,4]
print(getSubsets(arr))
print('\n')
arr = ['a','b','c','d']
print(getSubsets(arr))


# following commented code is from Gayle McDowels book. Did not work in python
# subset = []
# k = i
# index = 0
# while (k & 1 > 0):
#     subset.append(arr[index])
# k = k >> 1
# index += 1
# allSubsets.extend(subset)
