'''

Given a list of numbers [2,1,1,2]
and set of operators '+' ,'*'
(2+1) * (1+2)
find max output that can be generated

'''



def CreateMaxSubtree(arr):

    if len(arr) == 0:
        return
    elif len(arr)== 1:
        return arr[0]
    elif len(arr) == 2:
       x =arr[0]
       y = arr[1]
       x = 1 if x == None else x
       y = 1 if y == None else y
       product = x * y
       x = arr[0]
       y = arr[1]
       x = 0 if x == None else x
       y = 0 if y == None else y
       sum = x + y
       return max( product, sum)
    else:
        CreateMaxSubtree(arr[:1])
        CreateMaxSubtree(arr[1:])


def GetMaxOutput(nums, operators):


    maxresult = float("-infinity")
    result = float("-infinity")

    for i in range(len(nums)):

        left = CreateMaxSubtree(nums[:i])
        right = CreateMaxSubtree(nums[i:])
        x = left
        y = right
        x = 1 if x == None else x
        y = 1 if y == None else y
        product = x * y
        x = left
        y = right
        x = 0 if x == None else x
        y = 0 if y == None else y
        sum = x + y
        result = max(product, sum)

        if maxresult < result:
            maxresult = result

    return maxresult


nums = [2,1,1,2]
operatorsList = ['+','*']

print(GetMaxOutput(nums, operatorsList))