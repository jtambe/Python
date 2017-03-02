








suffixArray = []
LCP = [] # LCP = longest common prefix


import collections
def GetSuffixLCPArray(str): # works in o(nlogn)

    global suffixArray
    global LCP
    auxDictionary = {}

    for i in reversed(range(len(str))):
        auxDictionary[i] = str[i:]

    sortedAuxDictionary = collections.OrderedDict(sorted(auxDictionary.items(), key=lambda t:t[1]))

    print(auxDictionary)
    print(sortedAuxDictionary)

    for k in sortedAuxDictionary:
        suffixArray.append(k)


    orderedSuffixes = []
    for k in sortedAuxDictionary:
        orderedSuffixes.append(sortedAuxDictionary[k])

    for i in range(len(orderedSuffixes)-1):
        minsize = min(len(orderedSuffixes[i]), len(orderedSuffixes[i+1]))
        lcpValue = 0
        j = 0
        while j < minsize:
            if (orderedSuffixes[i][j] == orderedSuffixes[i+1][j]):
                lcpValue += 1
                j += 1
            else:
                break
        LCP.append(lcpValue)


    LCP.append(0)

    print(suffixArray)
    print(LCP)



def main():
    str = "jayesh"
    str = "banana"
    GetSuffixLCPArray(str)


if __name__ == "__main__":
    main()