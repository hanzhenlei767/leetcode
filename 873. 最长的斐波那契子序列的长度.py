#最长的斐波那契数列的长度
class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n=len(A)
        tmp=set(A)
        res=0
        for i in range(n):
            for j in range(i+1,n):
                left=A[j]
                right=A[i]+A[j]
                length=2
                while right in tmp:
                    length+=1
                    left,right=right,left+right
                res=max(res,length)
        if res<3:
            return 0
        return res