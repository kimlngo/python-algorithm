
def product_except_self(nums):
    prefix = 1
    suffix = 1

    result = [1] * len(nums)
    
    #pass 1
    for i, num in enumerate(nums):
        result[i] = prefix
        prefix *= num
    
    #pass 2
    index = len(nums) - 1
    while index >= 0:
        result[index] *= suffix
        suffix *= nums[index]
        index -= 1

    return result

print(product_except_self([4,2,8,3]))
print(product_except_self([1,2,3,4]))
print(product_except_self([-1,1,0,-3,3]))