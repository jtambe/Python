
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
    max = ~0 # set all 1's , 1's compliment
    print(bin(max))

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
print(updateBits(n,m,i,j))



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








