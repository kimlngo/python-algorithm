import BinarySearch

NOT_FOUND = [-1,-1]

def search_range(nums, target):
    if len(nums) == 0:
        return NOT_FOUND
    elif len(nums) == 1:
        if nums[0] == target:
            return [0,0]
        else:
            return NOT_FOUND
    
    firstIdx = BinarySearch.binary_search(nums, target)
    if firstIdx == -1:
        return NOT_FOUND
    
    i = firstIdx
    leftIdx = -1
    while i >= 0:
        if nums[i] == target:
            leftIdx = i
            i -= 1
        else:
            break
    
    i = firstIdx
    rightIdx = -1
    while i < len(nums):
        if nums[i] == target:
            rightIdx = i
            i += 1
        else:
            break
    
    return [leftIdx, rightIdx]


print(search_range([5,7,7,8,8,10], 8))
print(search_range([5,7,7,8,8,10], 6))
print(search_range([], 6))
print(search_range([0,3], 3))
print(search_range([0,3], 0))