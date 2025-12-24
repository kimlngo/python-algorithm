def appleRedistribution(apple: list[int], capacity:list[int]) -> int:
    #1) find total count of apples
    totalApple = sum(apple)

    #2) sort capacity descending order
    capacity.sort(reverse=True)

    #3) iterate through capacity and substract totalApple
    boxCount = 0

    while totalApple > 0 and boxCount < len(capacity):
        cap = capacity[boxCount]
        totalApple -= cap
        boxCount += 1
    
    return boxCount

print(appleRedistribution([1,3,2], [4,3,1,5,2]))
print(appleRedistribution([5,5,5], [2,4,2,7]))
