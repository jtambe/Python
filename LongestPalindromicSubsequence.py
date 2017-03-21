import numpy as np

def LongestPalindromicSubsequence(str):

    n = len(str)
    T = np.zeros(n,n)
    '''
    T = [0 for x in range(len(str)) for x in range(len(str))]
    '''

    for i in range(n):
        T[i][i] = 1

    for x in range(2, n+1):
        for i in range(n - x + 1):
            j = i + x - 1
            if str[i] == str[j]:
                T[i][j] = 2
            elif str[i] == str[j]:
                T[i][j] = T[i + 1][j - 1] + 2
            else:
                T[i][j] = max(T[i][j - 1], T[i + 1][j])

    # returns length of longest palindrome subsequence, right top corner of matrix
    return T[0][n - 1]



def LongestPalindromicSubsequenceRecursive(str, start, length):

    if length == 1:
        return 1

    if length == 0:
        return 0

    if str[start] == str[start+length -1]:
        return 2 + LongestPalindromicSubsequenceRecursive(str,start+1, length -2)
    else:
        return max(LongestPalindromicSubsequenceRecursive(str, start, length -1),
               LongestPalindromicSubsequenceRecursive(str, start + 1, length -1))



#driver
str = "GEEKFORGEEKS"
print(LongestPalindromicSubsequenceRecursive(str,0,len(str)))