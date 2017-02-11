


#fibonacci series using dynamic programming
# O(n)
def fibonacci(length):

    #create array of length
    values = [0]*length
    values[0] = 0
    values[1] = 1
    for i in range(2,length):
        values[i] = values[i-1]+ values[i-2]
    print(values)

def fiboRecursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiboRecursive(n-1)+ fiboRecursive(n-2)


def fibonacciShort(n):
    # dual assignment
    a, b = 0, 1
    for i in range(n):
        # print horizontally
        print(a, end = " ")
        a, b = b, a+b

# Generator style
def fibonacciGenrator(n):
    a,b = 0,1
    print("")
    for i in range(n):
        yield a
        a,b = b, a+b



def main():
    #fibonacci(10)

    #print(fiboRecursive(9))

    fibonacciShort(10)

    for eachYieldResult in fibonacciGenrator(10):
        print(eachYieldResult, end=" ")


if __name__ == '__main__':
    main()