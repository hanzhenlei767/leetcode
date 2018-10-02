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
  