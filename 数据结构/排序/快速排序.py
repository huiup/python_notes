

alist = [6,12,7,9,3,4,5,10,8]

def sort(alist,left,right):# 用left和right的指向区分不同的子序列
    low = left# 第一个元素下标
    high = right# 最后一个元素下标

    # 结束递归条件
    if low > high:
        return

    p = alist[low]# 基点
    while low != high:
        # 先偏移high
        while low < high:
            if p < alist[high]:# 向左偏移high
                high = high - 1
            else:# 将小于基点的值放到左侧的空位
                alist[low] = alist[high]
                break
        # 向右偏移
        while low < high:
            if p >= alist[low]:
                low += 1
            else:
                alist[high] = alist[low]
                break
    alist[low] = p# alist[high] = p


    # 以上为核心操作，需要将核心操作递归作用到左右子序列中
    
    sort(alist,left,low-1)# 作用到左侧序列中
    sort(alist,high+1,right)# 作用到右侧序列中
    return alist

print(sort(alist,0,len(alist)-1))