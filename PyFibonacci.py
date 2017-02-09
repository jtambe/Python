


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


def main():
    fibonacci(10)
    print(fiboRecursive(9))

if __name__ == '__main__':
    main()