'''
http://www.geeksforgeeks.org/rotate-bits-of-an-integer/


rotate bits of n by d count
rotation can be right side or left side
'''

def LeftRotate(n, d):

    totalBits = 64
    return (n << d) | ( n >> (totalBits - d) )


def RightRotate(n, d):

    totalBits = 64
    return (n >> d) | (n << (totalBits - d))



#driver

print(bin(LeftRotate(5, 2)))


