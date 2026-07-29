def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) -2):
        if i > 0 and nums[i] == nums[i -1]:
            continue
        left = i + 1
        right = len(nums) -1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left],nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result
nums = [-2,-1,3,0,1,2]
print("triplet number sum = 0 :",three_sum(nums))    
