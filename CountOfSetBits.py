def CountSetBits(n):

    count = 0

    while(n):

        n = n & (n-1)
        count += 1

    return count


print(CountSetBits(5))
print(CountSetBits(10))
print(CountSetBits(15))
print(CountSetBits(8))
