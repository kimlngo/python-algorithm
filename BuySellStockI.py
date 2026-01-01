def maxProfit(prices: list[int]) -> int:
    maxProfit = 0
    minSofar = 10001

    for price in prices:
        if price < minSofar:
            minSofar = price
        else:
            maxProfit = max(maxProfit, price - minSofar)
        
    
    return maxProfit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))