
def binary_search(nums, target):
    if len(nums) == 0:
        return -1
    elif len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(binary_search([5, 7, 7, 8, 9, 10], 8))
print(binary_search([5, 7], 5))
print(binary_search([5, 7], 7))
print(binary_search([5, 7, 7, 8, 8, 8], 8))
print(binary_search([5, 7, 7, 8, 8, 8], 6))
print(binary_search([5, 7, 7, 8, 8, 8], 5))
print(binary_search([5, 7, 7, 8, 8, 10], 10))
print(binary_search([5, 7, 7, 8, 8, 10], 7))