# 每次冒泡，将最大的元素冒到最后面
# 第一次是前n个元素，最大的元素冒到最后
# 第二次是前n-1个元素，最大的元素冒到倒数第二个位置

alist = [3,8,5,11,7,6,2]
alist2 = [1,2,3,4,5,6,7]
def sort(alist):
    for j in range(len(alist)-1):# 外层循环次数递增，内层循环次数递减
        for i in range(len(alist)-1-j):# 将乱序序列中的最大值，逐一移动到序列的最后
            if alist[i] > alist[i+1]:# 若前一个元素大于后一个元素，交换两者位置
                alist[i],alist[i+1] = alist[i+1],alist[i]
    return alist
print(sort(alist2))
