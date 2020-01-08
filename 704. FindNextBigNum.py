def FindNextBigNum(nums,target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left+right)//2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left    
        
arr = [0,1,2,3,3,3,3,3,3,4,5,6,8,9]
FindNextBigNum(arr,3)




