'''
关键变量：增量--gap
gap：初始值为len(alist)//2
    - 表示分组的组数
    - 每一组数据之间的距离

插入排序就是增量gap为1的希尔排序
'''
alist = [3,8,5,11,7,6,2]

def sort(alist):
    gap = len(alist) // 2
    while gap>=1:
        for i in range(gap,len(alist)):
            while i>0:
                if alist[i-gap] > alist[i]:
                    alist[i-gap],alist[i] = alist[i],alist[i-gap]
                i -= 1
        gap //= 2
    return alist

print(sort(alist))