class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        def get_next(s):
            if s == "":
                return None
            s_len = len(s)
            last_str = ""
            count = 1
            base = s[0]
            for i in range(1,s_len):
                if s[i] == base:
                    count = count+1
                else:
                    last_str += str(count)+str(base)
                    base = s[i]
                    count = 1
            last_str += str(count)+str(base)
            return last_str
        temp = get_next("1")
        for i in range(n-2):
            temp = get_next(temp)
        return temp
        