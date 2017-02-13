
def isUnique(str):
    checker  = 0
    strList = list(str)
    for i in range(len(strList)):
        val = ord(strList[i]) - ord('a')
        if( checker & (1 << val) > 0):
            return False
        #checker |= (1 << val)
        checker = checker | (1 << val)
        #a += 7

    return True



print(isUnique("jayesh"))
print(isUnique("aaol"))






# print (1 << 0)
