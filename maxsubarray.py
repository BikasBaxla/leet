#brute force method
def max_sub_array(nums):
    max_sum = nums[0]
    for i in range(len(nums)):
        current_sum =0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum> max_sum:
                max_sum = current_sum
    return max_sum
nums = [4,-1,2,1,-5,4,3]
print(max_sub_array(nums))