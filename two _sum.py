nums = [21,4,16,8,13,5,11,2,19]
target = 24

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
print(two_sum(nums, target))
