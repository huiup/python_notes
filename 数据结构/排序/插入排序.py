# 把列表分为两部分，前面一部分有序，
# 后面一部分无序，每次从后面选择第一个元素插入到前面有序序列中

alist = [3,8,5,11,7,6,2]
def sort(alist):
    for i in range(1,len(alist)):
        while i>0:
            #alist[i-1]:有序部分最后一个元素下标
            #alist[i]:无序部分第一个元素下标
            if alist[i-1] > alist[i]:
                alist[i-1],alist[i] = alist[i],alist[i-1]
            i -= 1
    return alist

print(sort(alist))
