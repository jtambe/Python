

def GetProductsOfAllExceptAtIndex(arr):

    if len(arr) < 2:
        raise IndexError('Getting the product of numbers at other indices requires at least 2 numbers')

    productsOfallExceptAtIndex = [None for i in range(len(arr))]

    print(arr)
    # print(productsOfallExceptAtIndex)
    productSoFar = 1
    i = 0
    while(i < len(arr)):
        productsOfallExceptAtIndex[i] = productSoFar
        productSoFar *= arr[i]
        i  += 1

    print(productsOfallExceptAtIndex)

    productSoFar = 1
    i = len(arr) - 1
    while (i >= 0):
        productsOfallExceptAtIndex[i] *= productSoFar
        productSoFar *= arr[i]
        i -= 1
    print(productsOfallExceptAtIndex)


    return productsOfallExceptAtIndex







arr = [15,25,7,5,3,26,0,14,12]
# arr = [1,2,3,4,5,6,7,9]

ans = GetProductsOfAllExceptAtIndex(arr)
print(ans)






