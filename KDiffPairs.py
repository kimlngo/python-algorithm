from collections import Counter

def findPairs(nums: list[int], k: int) -> int:
    if len(nums) == 1:
        return 0
    
    count = 0
    if k == 0:
        #if k = 0, the problem is simplified to finding how many elements in nums
        #appear more than 1 times --> build frequency counter and return count of
        #elements with frequency >= 2
        freq_counter = dict(Counter(nums))

        for _, val in freq_counter.items():
            if val >= 2:
                count += 1
        
        return int(count)

    else:
        distInt = list(set(nums))

        for n in distInt:
            greater = n + k
            smaller = n - k

            if greater in distInt:
                count += 1
            
            if smaller in distInt:
                count += 1

        return int(count / 2)
    

print(findPairs([3, 1, 4, 1, 5], 2))
print(findPairs([1, 2, 3, 4, 5], 1))
print(findPairs([1, 3, 1, 5, 4], 0))