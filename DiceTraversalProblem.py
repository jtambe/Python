'''
If the finishing point is “n” spaces away from the starting point,
please implement a program that calculates
how many possible ways are there to arrive exactly at the finishing point.
'''

# This solution uses bottom-up approach


def RollingDiceCount(n):

    maxCount = 0

    # if there are 6 or less steps then we calculate number of steps using following formula
    if(n <= 6):
        return 2 ** (n-1)
    else:

        # otherwise maintain a list of counts at each step
        listOfCounts = [0]*n
        # 0 steps at last postion. no more rolling of dice
        listOfCounts[n-1] = 0

        # for previous 6 positions in list counts array, we set up values, using the formula above
        i = n-2
        x = 0
        while(i >= n - 7):
            listOfCounts[i] = 2 ** x
            x += 1
            i -= 1

        # above code covers last 7 position counts

        #  for 8th count onwards we use following logic
        # for each step, counts would be only limited to 6 steps => p range(1,7).
        # As one can only travel 6 steps at the most using a 6faced dice
        # for each step, we find what is max number of possible ways and update variable
        #  by adding listcount[position] + number of ways to get there from current position
        for i in reversed(range(n-7)):
            for p in range(1,7):
                if maxCount < ( 2**(p-1) + listOfCounts[i+p] ):
                    maxCount = ( 2**(p-1) + listOfCounts[i+p] )
                    listOfCounts[i] = ( 2**(p-1) + listOfCounts[i+p] )

        print(listOfCounts)
        return listOfCounts[0]

print(RollingDiceCount(610))