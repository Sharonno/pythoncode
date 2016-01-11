#-*-coding:utf-8-*-
#!/usr/bin/python

def bubbleSort(a):
    l = len(a)
    for i in range(l-1):
        for j in range(i, l):
            if a[i] > a[j]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
    return a
def insertSort(a):
    
    pass
if __name__ == '__main__':
    a = [3,2,4,5,1]
    print bubbleSort(a)
