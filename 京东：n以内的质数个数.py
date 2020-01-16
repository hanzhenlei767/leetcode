
#求n以内的质数个数
def countPrimes(n):
    """
    :type n: int
    """
    import math
    num=0
    for i in range(2,n):
        flag=1
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                flag=0
                break
        if flag==1:
            num+=1
    return num