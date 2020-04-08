#问题：有一个文本串S，和一个模式串P，现在要查找P在S中的位置

#暴力法
def KMP(s,p):
    s_len = len(s)
    p_len = len(p)
    if s_len < p_len:
        return -1
    for i in range(0,s_len-p_len+1):
        for j in range(p_len):
            if p[j] != s[i+j]:
                break
            else:
                if j == p_len-1:
                    return i
    return -1
	
	
#KMP算法（ Knuth-Morris-Pratt 字符串查找算法）
	
	


























