# this function checks if all elements in array are paired
# it uses bitwise XOR logic

def IsArrayOfPairs(arr):
    var = arr
    checker = 0
    for i in range(len(arr)):
        checker ^= ord(arr[i])

    if checker == 0:
        print("All pairs")
    else:
        print("At least one odd entry")

def main():
    arr = ['A','A','B','B','N','N','M','M',]
    IsArrayOfPairs(arr)


    arr = ['A', 'A', 'B', 'B', 'N', 'N', 'M', 'X', ]
    IsArrayOfPairs(arr)

if __name__ == '__main__':
    main()
