import math

def longestCommonPrefix(arr1: list[int], arr2: list[int]) -> int:
    #1) construct the prefix for arr1
    prefix1 = set()

    for num in arr1:
        while num not in prefix1 and num > 0:
            prefix1.add(num)
            num = int(num / 10)
    
    longestPrefix = 0

    #2) iterate through each num in arr2 and check if the prefix in num1 can be used
    for num in arr2:
        while num not in prefix1 and num > 0:
            num = int(num / 10)

        if num > 0:
            longestPrefix = max(longestPrefix, int(math.log10(num)) + 1)

    return longestPrefix

print(longestCommonPrefix([10], [17,11]))