
#1
b = int('1010',2) - int('0001',2)
a = int('1010',2) - int('0001',2)
# print(b) #9
# print(bin(a)) #1001

#2
b = int('1010',2) + int('0110',2)
a = int('1010',2) + int('0110',2)
# print(b) #16
# print(bin(a)) #10000


#3
b = int('1100',2) ^ int('0110',2)
a = int('1100',2) ^ int('0110',2)
# print(b) #10
# print(bin(a)) #1010

#4
b = int('1010',2) << 3 # multiply by 2 thrice
a = int('1010',2) << 3 # multiply by 2 thrice
# print(b) #80
# print(bin(a)) #1010000

#5
b = int('1010000',2) >> 4 # divide by 2 4 times
a = int('1010000',2) >> 4 # divide by 2 4 times
# print(b) #5
# print(bin(a)) #101

#6
b = int('1100',2) & int('0110',2)
a = int('1100',2) & int('0110',2)
# print(b) #4
# print(bin(a)) #100


#7
b = int('0xff',16) - 1
a = int('0xff',16) - 1
# print(b) #254
# print(hex(a)) #0xfe


#7
b = int('0xAB',16) + int('0xAB',16)
a = int('0xAB',16) + int('0xAB',16)
# print(b) #342
# print(hex(a)) #0x156


#Problem #1
'''
You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to set all bits between i and j in N equal to M (e.g., M becomes a substring of N located at i and starting at j).
EXAMPLE:
Input: N = 10000000000, M = 10101, i = 2, j = 6
Output: N = 10001010100
'''




def updateBits(n, m, i, j):

    nn = int(n, 16)
    mm = int(m, 16)
    q = 10
    max = q # set all 1's , 1's compliment
    #print(bin(max&1).zfill(64))
    print(bin(max).zfill(64))

    #set 1's through position j, then its all o's
    left = max - ((1 << j) -1)

    #1's after position i
    right = ((1 << i) -1)

    # 1's with 0's between i and j
    mask = left | right

    # clean i to j and place m in there
    res =  (nn & mask) | (mm << i)
    return bin(res)

n = '10000000000'
m = '10101'
i = 2
j = 6
#print(updateBits(n,m,i,j))


import numpy as np
t = bin(~np.int(10))
# print(t.zfill(64))


# number = '1123.557'
# print(number[:number.find('.')])
# print(number[number.find('.')+1:])


# def printBinary(decimalStr):
#
#     intPart = int(decimalStr[:decimalStr.find('.')])
#     decimalPart = float(decimalStr[decimalStr.find('.')+1:])
#
#     intstring = ""
#     while(intPart > 0):
#         r = intPart %2
#         intPart = intPart >> 1
#         intstring = str(r) + intstring
#
#     print(intstring)
#
#     decString = ""
#
#     while(decimalPart > 0):
#         if(len(decString) > 32):
#             raise Exception("Length out of bounds")
#         if decimalPart == 1:
#             decString.join(decimalPart)
#
#
#
# printBinary('123.897')
#
#
#
#



#check if two integers have opposite signs
x, y  = 10 , -90

# print(bin(x))
# print(bin(y))
# print(bin(~2))
# print(int('1011010',2))

areOppositeSigns = ((x ^ y) < 0)

# if(areOppositeSigns):
#     print("are opposite signs")


#find min and max
x = 23
y = -90

r1 = y ^ ((x ^ y) & -(x < y)) # minimum
# print(r1)
r2 = x ^ ((x ^ y) & -(x < y)) # maximum
# print(r2)

x = 8
y = 10
print(bin(x)) #1000
print(bin(y)) #1010

print("x^y")
print(bin(x^y)) #0010
print("x<y")
print(bin(x<y)) #0001
print("-(x<y)")
print(bin(-(x<y))) #-0001
print("(x ^ y) & -(x < y)")
'''
Bitwise and of negative number is adding with negative number's two's compliment
Therefore, & with -1 is adding two's compliment of -1
2's compliment of -1
1. 1's compliment of -1 => 1110
2. 2's compliment = 1's compliment + 1 => 1111
'''
print(bin((x ^ y) & -(x < y)))  #0010






# number of bits set in a number
v = 15
print(bin(v))
print(bin(v-1))

print(bin(v& v-1))


# unsigned int v; // count the number of bits set in v
# unsigned int c; // c accumulates the total bits set in v
# for (c = 0; v; c++) # as long as v > 0
# {
#   v &= v - 1; // clear the least significant bit set
# }
#



