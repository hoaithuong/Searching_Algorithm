# Linear Search

def search(a,x):
    #exist = 0
    count = 0
    for i in range(0, len(a)):
        if x == a[i]:
            #print 'Phan tu ' +str(a[i])+' co vi tri la: ' + str(i)
            #exist = 1
            count = count+1
    #if exist == 0:
        #print 'Khong co phan tu ' + str(x)+' nao trong mang a!'
    print('Phan tu ' +str(x) + ' xuat hien ' + str(count) + ' lan trong mang a')
list = [10,8,9,4,6,5,3,2,7,1,0,4,6,3,5,7,11,9,6,14,8,3,19,20,3,5,21]
search(list, 9)
