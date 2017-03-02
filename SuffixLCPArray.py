


suffixArray = [] # array of indices with ordered suffixes, ordered by character
LCP = [] # LCP array = longest common prefix array


import collections
def GetSuffixLCPArray(str): # works in o(nlogn)

    global suffixArray
    global LCP

    # using this auxiliary dictionary to store suffixes at indices as (index,suffix) pair
    auxDictionary = {}
    for i in reversed(range(len(str))):
        auxDictionary[i] = str[i:]

    # sorting the auxDictionary based on character values in suffixes in ascending order
    sortedAuxDictionary = collections.OrderedDict(sorted(auxDictionary.items(), key=lambda t:t[1]))

    print(auxDictionary)
    print(sortedAuxDictionary)

    # get the indices from ordered dictionary to create suffix array
    for k in sortedAuxDictionary:
        suffixArray.append(k)


    # created a temporary list for suffixes in ordered format as in sortedAuxDictionary
    orderedSuffixes = []
    for k in sortedAuxDictionary:
        orderedSuffixes.append(sortedAuxDictionary[k])



    for i in range(len(orderedSuffixes)-1):
        # to compare matching characters at current level with next level,
        # I need minimum length for me to travel in comparison
        minsize = min(len(orderedSuffixes[i]), len(orderedSuffixes[i+1]))
        lcpValue = 0
        j = 0
        while j < minsize:
            # for each matching character in comparison, lcpValue increments
            if (orderedSuffixes[i][j] == orderedSuffixes[i+1][j]):
                lcpValue += 1
                j += 1
            else:
                break
        LCP.append(lcpValue)

    # finally last index in LCP is always zero because there is no next string to compare with and have matching characters
    LCP.append(0)

    print(suffixArray)
    print(LCP)



def main():
    str = "jayesh"
    str = "banana"
    GetSuffixLCPArray(str)


if __name__ == "__main__":
    main()