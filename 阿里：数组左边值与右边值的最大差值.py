# 求数组左边值与右边值的最大差值

#O(n)解法
def maxDiff(nums):
    if len(nums) < 2:
        return -1
    
    max_val = nums[0]
    max_dif = -float("inf")
    
    for i in range(1,len(nums)):
        if max_val - nums[i] > max_dif:
            max_dif = max_val - nums[i]
            
        if nums[i] > max_val:
            max_val = nums[i]
    return max_dif

nums = [1,2,3,-4,1,2,3,4]
maxDiff(nums)


#O(n2)解法
def maxDiff(nums):
    max_dif = -float("inf")
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] - nums[i] > max_dif:
                max_dif = nums[j] - nums[i]
    return max_dif
    
    
nums = [1,2,3,-4,1,2,3,4]
maxDiff(nums)