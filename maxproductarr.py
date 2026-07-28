def max_product(nums):
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]

        temp_max = max_product
        temp_min = min_product

        max_product = max(num, num * temp_max * temp_min)
        min_product = min(num, num * temp_max * temp_min)

        result = max(result, max_product)
    return result
nums = [ -2,0,-1,-3,4]
print(max_product(nums))