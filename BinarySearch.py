# Binary Search

def binarysearch(a, x):
    first = 0
    last = len(a)-1
    mid = (first+last)//2
    exist = 1
    while a[mid] != x:
        if a[mid] > x:
            last = mid-1
            mid = (first+last)//2
        if a[mid] < x:
            first = mid+1
            mid = (first+last)//2
        if first > last:
            print('Khong co phan tu '+ str(x)+ ' trong mang a')
            exist = 0
            break
    if exist==1:
        print('Vi tri cua ' + str(x) + ' la ' + str(mid))

list = [1,2,3,4,5,6,7,8,9,10]
binarysearch(list,100)
