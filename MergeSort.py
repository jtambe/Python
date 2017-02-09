




def Merge(leftList, rightList, inputList):

    i = j = k = 0
    # i is my increment for left sublist
    # j is my increment for right sublist
    # k is my increment for actual input list

    while i < len(leftList) and j < len(rightList):
        if leftList[i] <= rightList[j]:
            inputList[k] = leftList[i]
            i = i+1
            k = k+1
        else:
            inputList[k] = rightList[j]
            j = j+1
            k = k+1

    # as merge progresses, one of the sublist will exhaust filling in the original list first
    # the remaining portion of other sublist is filled in using following code
    # we dont know which list will exhaust first, so we write code for both of them

    while i < len(leftList):
        inputList[k] = leftList[i]
        i = i+1
        k = K=1

    while j < len(rightList):
        inputList[k] = rightList[j]
        j = j+1
        k = k+1



def MergeSort(inputList):

    listLength = len(inputList)
    # base condition for mergeSort function list division
    if listLength < 2:
        return

    #keeping it integer and not float when not divisible
    middle = (listLength)//2

    leftList = inputList[:middle]
    rightList = inputList[middle:]

    MergeSort(leftList)
    MergeSort(rightList)
    # MergeSort(inputList[first:middle+1])
    # MergeSort(inputList[middle+1:last+1])
    Merge(leftList, rightList, inputList)


def main():
    myList = [12,3,8, 45,90.65,34,-2,73,11,9,5,40,19,34,92,32,11,9,32]
    print(myList)
    MergeSort(myList)
    print(myList)

if __name__ == "__main__":
    main()

