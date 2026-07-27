def product(nums):
    solution = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        solution.append(product)
    return solution
nums = [2,3,5,7,11]
print(product(nums))