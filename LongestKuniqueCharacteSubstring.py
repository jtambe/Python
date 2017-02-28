def LongestKUniqueCharactersSubstring(inputstr, K):

    start,end = 0,0

    windowsSize, windowStart = 1,0

    dict = {}
    dict[inputstr[0:1]] = 1

    for i in range(1,len(inputstr)):
        if inputstr[i] in dict:
            dict[inputstr[i]] += 1
        else:
            dict[inputstr[i]] = 1
        end += 1

        while( not IsLessThan(dict, K )):
            dict[inputstr[start]] = dict[inputstr[start]] - 1
            start += 1

        if(end - start + 1 >= windowsSize):
            windowsSize = end - start + 1
            windowStart = start


    return inputstr[windowStart:windowStart+ windowsSize]


def IsLessThan(dict, K):
    count = 0

    for key in dict:
        if dict[key] > 0:
            count += 1

    return (count <= K)


answer = LongestKUniqueCharactersSubstring("abbbbccdddddddfeeeeeeeee", 2)
print(answer)
answer = LongestKUniqueCharactersSubstring("karappa", 2)
print(answer)
answer = LongestKUniqueCharactersSubstring("abbbbccddddddddddfeeeeeeeee", 2)
print(answer)