
# coding: utf-8

#冒泡排序，升序排列

def bubbleSort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 最后一个元素i已经就位
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

