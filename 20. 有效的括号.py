class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = ['(','[','{']
        s2 = [')',']','}']
        s3 = ['()','[]','{}']
        
        temp_s = []
        for i in s:
            if i in s1:
                temp_s.append(i)
            elif i in s2:
                if temp_s != []:
                    if (temp_s.pop()+i) in s3:
                        pass
                    else:
                        return False
                else:
                    return False
        if len(temp_s) != 0:
            return False
        return True