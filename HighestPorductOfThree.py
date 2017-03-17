
from itertools import islice

def HighestProductOf3(arr):

    if len(arr) < 3:
        raise IndexError("need at least three elements")


    highest = max(arr[0], arr[1])
    lowest = min(arr[0], arr[1])

    highestProductOf2 = arr[0] * arr[1]
    lowestProductOf2 = arr[0] * arr[1]

    highestProductOf3 = arr[0] * arr[1] * arr[2]

    for current in islice(arr, 2, None):
        highestProductOf3 = max(
            highestProductOf3,
            current * highestProductOf2,
            current * lowestProductOf2
        )

        highestProductOf2 = max(
            highestProductOf2,
            current * highest,
            current * lowest
        )

        lowestProductOf2 = min(
            highestProductOf2,
            current * highest,
            current * lowest
        )

        highest = max(highest, current)
        lowest = min(lowest, current)


    return highestProductOf3




arr = [1,2,3,4,5,6,15,16,17,1,2,3,4]

ans = HighestProductOf3(arr)
print(ans)
