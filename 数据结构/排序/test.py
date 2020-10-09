alist = [3,8,5,11,7,6,2]

def sort(alist):
    gap = len(alist)//2
    while gap>0:
        for i in range(len(alist)):
            while i>0:
                if alist[i-1] > alist[i]:
                    alist[i-1],alist[i] = alist[i],alist[i-1]
                i -= 1
        gap //= 2            
    return alist

print(sort(alist)) 