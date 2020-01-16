#快排思想
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(num, low, high):
			'''降序'''
            pivot = num[low]
            while (low < high):
                while (low < high and num[high] <= pivot):
                    high -= 1
                num[low] = num[high]
                while (low < high and num[low] > pivot):
                    low += 1
                num[high] = num[low]
            num[high] = pivot
            return high
 
        def findkth(num,low,high,k):   #找到数组里第k个数
            index=partition(num,low,high)
            if index==k:
                return num[index]
            if index<k:
                return findkth(num,index+1,high,k)
            else:
                return findkth(num,low,index-1,k)

        return findkth(nums,0,len(nums)-1,k-1)




class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quick_sort(nums,head,tail):  
            if head >= tail:
                return None

            base = nums[head]
            left = head
            right = tail

            while left!=right:
                while (left<right) and (nums[right]>base):
                    right -= 1
                while (left<right) and (nums[left]<=base):
                    left += 1
                if left != right:
                    temp = nums[right]
                    nums[right] = nums[left]
                    nums[left] = temp

            temp = nums[left]
            nums[left] = nums[head]
            nums[head] = temp
            quick_sort(nums,right+1,tail)
            quick_sort(nums,head,left-1)
            
        largest_list = nums[0:k]
        quick_sort(largest_list,0,k-1)

        for i in nums[k:]:
            if i > largest_list[0]:
                for j in range(len(largest_list)):
                    if (i < largest_list[j]):
                        largest_list.insert(j,i)
                        break
                    if (len(largest_list)-1) == j:
                        largest_list.append(i)
                largest_list =largest_list[1:]
        return largest_list[0]
  
  
  
  