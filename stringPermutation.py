
#generate all permutations of a given string
#credits : http://www.ardendertat.com/2011/10/28/programming-interview-questions-11-all-permutations-of-string/

#O(n!)

def permutations(word):
    if len(word) <= 1:
        return [word]

    # get all permutations of length N-1
    perms = permutations(word[1:])
    char = word[0]
    result = []
    # iterate over all permutations of length N-1
    for perm in perms:
        # insert the character into every possible location
        for i in range(len(perm) + 1):
            result.append(perm[:i] + char + perm[i:])
    return result


# print(4*3*2*1)

result = permutations("abcd")
print(len(result))
for item in result:
    print(item)