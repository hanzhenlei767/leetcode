#找出数组中出现次数超过一半的数

#使用字典统计数组元素出现的词数，一旦有元素出现词数过半直接返回该元素。
#时间复杂度为O(n),空间复杂度比较高，需要字典存储数组。

def FindNum(arr):
    h_dict = {}
    h_v = len(arr)//2
    for i in arr:
        if i in h_dict:
            h_dict[i] += 1
        else:
            h_dict[i] = 1
        if h_dict[i] > h_v:
            return i
			
#使用抵消机制。数组中过半的元素最终将保留下来。
#时间复杂度O(n),空间复杂度较低。
def FindNumMemery(arr):
    count = 1
    value = arr[0]
    for i in arr[1:]:
        if value == i:
            count += 1
        elif count == 0:
            value = i
            count = 1
        else:
            count -= 1

    return value