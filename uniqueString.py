
def isUnique(str):
    checker  = 0
    strList = list(str)
    for i in range(len(strList)):

        # ord is used to find ASCII value of character in python
        val = ord(strList[i]) - ord('a')

        # if ASCII value of their differences was already added by shifting 1 as many times in bitwise
        # representation of checker, then this time bitwise & will return true as at least one bit will be
        # set high in bitwise and
        if( checker & (1 << val) > 0):
            return False

        #left shift 1 and add it in bitwise representation of checker
        checker = checker | (1 << val)
        # checker |= (1 << val)

    return True



print(isUnique("jayesh"))
print(isUnique("aaol"))






# print (1 << 0)
