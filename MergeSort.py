
# coding: utf-8

def MergeSort(left, right):
    # 比较传过来的两个序列left,right，返回一个排好的序列
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 这时候i或者j到了序列的最后
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def SortByMerge(arr, size):
    if size <= 1:
        return arr
    i = int(size/2)
    left = SortByMerge(arr[:i], i)
    right = SortByMerge(arr[i:], size - i)
    return MergeSort(left, right)


arr = [12, 11, 13, 5, 7, 6]
print(SortByMerge(arr, len(arr)))

