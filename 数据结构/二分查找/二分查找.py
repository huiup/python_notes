'''
二分查找只能作用在有序序列中
'''

def find(alist, item):
    find = False
    low = 0
    high = len(alist)-1
    
    
    while low <= high:#小于等于
        mid = (low + high) // 2
        if item < alist[mid]:# 查找的元素小于中间元素，则查找的元素在中间元素的左侧
            high = mid - 1#low和high就可以表示新序列的范围
        elif item > alist[mid]:# 查找的元素在中间元素的右侧
            low = mid + 1
        else:# 查找的元素就是中间元素
            find = True
            break
    return find


alist = [1,2,3,4,5]
print(find(alist,5))