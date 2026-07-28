# kadane algorithm
def max_sub_sum_arr(nums):
    
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum
nums = [4,-1,2,1,-5,4,3]
print(max_sub_sum_arr(nums))