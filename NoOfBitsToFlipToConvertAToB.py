# aim here is not to convert a into b

'''
http://www.geeksforgeeks.org/count-number-of-bits-to-be-flipped-to-convert-a-to-b/

1. Calculate XOR of A and B.
        a_xor_b = A ^ B
2. Count the set bits in the above calculated XOR result.
        countSetBits(a_xor_b)

A  = 1001001
B  = 0010101
a_xor_b = 1011100
No of bits need to flipped = set bit count in a_xor_b i.e. 4

'''


def CountFlippingBits(a, b):

    xorOutput =  a ^ b
    count = 0

    while(xorOutput):

        xorOutput &= xorOutput -1 # this operation removes LSB from number
        count += 1

    return count

print(CountFlippingBits(10,1))
print(CountFlippingBits(10,0))



