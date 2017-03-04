
#given an array check if there is a pythagorean triplet in it
#works in O(n^2)
def IfTripletExists(arr):

    SquaredArr = []

    for i in arr:
        SquaredArr.append(i**2)

    SortedSquaredArr = sorted(SquaredArr)

    for i in reversed(range(len(SortedSquaredArr))):
        l = 0
        r = i-1
        while(l < r):
            if SortedSquaredArr[l] + SortedSquaredArr[r] == SortedSquaredArr[i]:
                return True
            else:
                if (SortedSquaredArr[l] + SortedSquaredArr[r] < SortedSquaredArr[i]):
                    l += 1
                else:
                    r -= 1
                #(l += 1) if (SortedSquaredArr[l] + SortedSquaredArr[r] < SortedSquaredArr[i]) else (r -= 1)
                #1 if (SortedSquaredArr[l] + SortedSquaredArr[r] < SortedSquaredArr[i]) else r -= 1


    return False



arr = [1,2,3,4,6,7,8,5]
print(IfTripletExists(arr))

