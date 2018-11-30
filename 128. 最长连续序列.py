class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        hash_dict = []
        
        def find_value(value,nums,d):
            if d == 0:#小方向
                if (value-1) in nums:
                    return True
                else:
                    return False
            else:#大方向
                if (value+1) in nums:
                    return True
                else:
                    return False

        def find_min_max_longest(nums,i):
            
            hash_dict.append(nums[i])
            
            longest_num = 1
            
            tmp = nums[i] 
            down = find_value(tmp,nums,0)
            while(down == True):
                hash_dict.append(tmp-1)
                longest_num = longest_num+1
                tmp = tmp-1
                down = find_value(tmp,nums,0)
                
            temp = nums[i]
            up = find_value(temp,nums,1)
            while(up == True):
                hash_dict.append(temp+1)
                longest_num = longest_num+1
                temp = temp+1
                up = find_value(temp,nums,1)
            return longest_num
        
        i = 0
        longest = find_min_max_longest(nums,i)
        for i in range(1,len(nums)):
            if nums[i] not in hash_dict:
                tmp_longest = find_min_max_longest(nums,i)
                if tmp_longest > longest:
                    longest = tmp_longest
        return longest
            
