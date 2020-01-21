def Search(nums,low,high,target):
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        elif nums[low] < nums[high]:
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[low] > target:
                low += 1
            else:
                high -= 1
    return -1
	
Search([4,5,6,7,1,2,3],0,6,3)
	