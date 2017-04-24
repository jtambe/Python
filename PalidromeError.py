def almost_palindromes(str):
    count = 0
    if (len(str) <= 1):
        return 0

    i = 0
    j = len(str) - 1
    while (i < j):
        if str[i] != str[j]:
            count += 1
        i += 1
        j -= 1
    if(len(str)%2 == 0):
        return count
    else:
        return count+1


print(almost_palindromes('aba'))
print(almost_palindromes('abba'))