def GetMaxProfit(stockPriceArray):

    # If there is less than two entries given in array,
    # return error
    if( len(stockPriceArray) < 2):
        raise IndexError("Need at least 2 entries for profit calculation")

    # Keep a track of minimum price of stocks as max profit will be when current price - min price is highest
    # Greedily set max_profit and minimum price

    minPrice = stockPriceArray[0]
    maxProfit = stockPriceArray[1] - stockPriceArray[0]


    for index, currentPrice in enumerate(stockPriceArray):

        # we cannot sell before buying
        # so cannot calculate max profit at index 0
        if index == 0:
            continue

        currentProfit = currentPrice - minPrice

        # get max profit value
        maxProfit = max(currentProfit, maxProfit)

        # minPrice is always calculated after currentProfit,
        # other if currentPrice == minprice, then that would be as if buying and selling at the same time,
        # which is not possible
        minPrice = min(minPrice, currentPrice)

    return maxProfit


# driver program
stockPriceArray = [2, 7, 9, 12, 3, 7, 10, 25]
print(GetMaxProfit(stockPriceArray)) #23