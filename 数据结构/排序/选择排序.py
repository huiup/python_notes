# 将乱序序列中的元素两两比较，找出最大值，然后直接将最大值放置到序列最后的位置
alist = [3,8,5,11,7,6,2]
def sort(alist):
    for j in range(len(alist)-1):
        max_index = 0#假设下标为0的元素为最大值
        for i in range(len(alist)-1-j):
            if alist[max_index] < alist[i+1]:# 与下一位比较
                max_index = i+1
        alist[len(alist)-1-j],alist[max_index] = alist[max_index],alist[len(alist)-1-j]# 交换
    return alist

print(sort(alist))