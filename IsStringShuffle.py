

#
# varSet = set("Jayesh")
# print(varSet)
#
# if('J','a') in varSet:
#     print("exists")
#

# a = ['x','y','z']
# b = ['p','q','r']
#
# varSet = set()
# varSet.add((a,b))
#
# # if(a,b) in varSet:
# #     print("exists")
#
# print(a,b)




def IsStringShuffle2(str1, str2, str3, cache=set()):
    if (str1, str2) in cache: # if we encounter already unmatched set of 2 input strings, dismiss further process
        return False

    if len(str1) + len(str2) != len(str3):
        return False

    if not str1 or not str2 or not str3:
        if str1 + str2 == str3:
            return True
        else:
            return False

    if str1[0] != str3[0] and str2[0] != str3[0]:
        return False

    if str1[0] == str3[0] and IsStringShuffle2(str1[1:], str2, str3[1:], cache):
        return True
    if str2[0] == str3[0] and IsStringShuffle2(str1, str2[1:], str3[1:], cache):
        return True

    # if neither of the string's first char matched, we start storing results in cache
    cache.add((str1, str2))

    return False



def IsStringShuffle1(str1, str2, str3):

    if( not str1 or not str2 or not str3 ): # one of the strings doesn't exist
        if(str1 + str2 == str3): # if str1 doesnt exists but str2 == str3 or str1 == str3
            return True
        else:
            return False

    if( len(str1) + len(str2) != len(str3) ): # their lengths don't sum up, then it is definitely not shuffled
        return False

    if(str1[0] != str3[0] and str2[0] != str3[0]): # is starting character is not matching with either of str1 or str2
        return False

    if(str1[0] == str3[0] and IsStringShuffle1(str1[1:], str2, str3[1:])): #remove the matched character and proceed
        return True
    if(str2[0] == str3[0] and IsStringShuffle1(str1, str2[1:], str3[1:])): #remove the matched character and proceed
        return True

    return False

def main():
    print(IsStringShuffle1("abc","def","abdcef"))
    print(IsStringShuffle1("abc", "def", "abcpqr"))
    print(IsStringShuffle1("abc", "def", "abcdef"))

    print('\n')

    cache = set()
    print(IsStringShuffle2("abc","def","abdcef",cache))
    cache = set()
    print(IsStringShuffle2("abc", "def", "abcpqr", cache))
    cache = set()
    print(IsStringShuffle2("abc", "def", "abcdef", cache))



if __name__ == "__main__":
    main()