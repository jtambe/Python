def ascii_deletion_distance(str1, str2):
    # if(len(str1))


    len1 = len(str1)
    len2 = len(str2)

    if(len1 == 0):
        return len2
    if(len2 == 0):
        return len1


    if(str1[len1-1] ==  str2[len2-2]):
        return ascii_deletion_distance(str1[:len1], str2[:len2])

    return 1 + min(ascii_deletion_distance(str1[:len1], str2[:len2-1]),
                   ascii_deletion_distance(str1[:len1-1], str2[:len2]),
                   ascii_deletion_distance(str1[:len1-1], str2[:len2-1]),
                   )

'''
The deletion distance between two strings is the minimum sum of ASCII values of characters that you need to delete in the two strings in order to have the same string. 
The deletion distance between "cat" and "at" is 99, because you can just delete the first character of cat and the ASCII value of 'c' is 99. 
The deletion distance between "cat" and "bat" is 98 + 99, because you need to delete the first character of both words. 
Of course, the deletion distance between two strings can't be greater than the sum of their total ASCII values, 
because you can always just delete both of the strings entirely.

 Implement an efficient function to find the deletion distance between two strings.

 You can refer to the Wikipedia article on the algorithm for edit distance if you want to. 
 The algorithm there is not quite the same as the algorithm required here, but it's similar.

at cat = 99
boat got = 298
though sloughs = 674

'''
