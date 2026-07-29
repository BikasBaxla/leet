"""
def search(nums , target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
nums = [87,12,45,78,90,23,56,89]
target = 23
print("Target found at index: ",str(search(nums, target)))
"""
"""
def search(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right)//2

        if nums[mid]== target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[right] < target <= nums[right]:
                left = mid + 1
            else:
                left = mid -1
    return -1
nums = [15,18,20,25,2,5,8,10]
target = 10
print("Target found at index: "+ str(search(nums, target)))

"""
def search(nums, minimum):
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (left + right)//2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
nums = [4,5,7,1,-4,0,9 ]
minimum = nums
print("Minimum value is :",search(nums, minimum))
