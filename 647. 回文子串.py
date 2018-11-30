class Solution:
    
    count = 0
    

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            left = i
            right = i
            while (left>=0) & (right<len(s)):
                if (s[left] == s[right]):
                    count = count + 1
                    left = left - 1
                    right = right + 1
                else:
                    break
                
            left = i
            right = i + 1
            while (left>=0) & (right<len(s) ):
                if (s[left] == s[right]):
                    count = count + 1
                    left = left - 1
                    right = right + 1
                else:
                    break
            
        return count
    
    
        
        
        