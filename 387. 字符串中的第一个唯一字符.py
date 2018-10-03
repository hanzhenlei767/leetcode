
#利用hash table
#python dict类型有些环境下是有序的，有些环境下是无序的。
#dict无序情况下，用list记录顺序


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return -1
        hash_dict = {}
        hash_list = []
        for i in range(len(s)):
            if s[i] in hash_dict:
                hash_dict[s[i]][1] += 1
            else:
                hash_dict[s[i]] = [i,1]
                hash_list.append(s[i])
        
        for j in hash_list:
            if hash_dict[j][1] == 1:
                return hash_dict[j][0]
        return -1