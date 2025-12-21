
def climbStairs(n):
    if n < 4: 
        return n
    
    first = 1
    second = 2

    for _ in range(2, n):
        third = first + second
        first = second
        second = third

    return second


for i in range(1,46):
    print(f"i = {i} - # of steps: {climbStairs(i)}")