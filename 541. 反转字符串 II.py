class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s_rtn = ""
        s_len = len(s)
        if s_len <k:
            return s[::-1]
        elif s_len<2*k:
            return s[:k][::-1]+s[k:]
        else:
            return s[:k][::-1]+s[k:2*k]+self.reverseStr(s[2*k:],k)
        