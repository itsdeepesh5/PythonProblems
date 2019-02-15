l= [ i for i in range(2000000)]
import time
def BinarySearch(l, n):
    
    mid= int(len(l)/2)
    if len(l) < 1:
        return False
    if n == l[mid]:
        return True
    if n > l[mid]:
        return BinarySearch(l[mid:], n)
    elif n < l[mid]:
        return BinarySearch(l[:mid], n)
    return False


def BSNon(l,n):
    start=0
    end = len(l)
    while start < end: # 0,6  , 3 < 6  
        mid =int((end+start)/2) #3 
        if l[mid] == n: # 4=5
            return True
        elif l[mid] < n:  #4 < 5 
            start= mid  
        elif l[mid] > n:
            end=mid+1
    return False

t0=time.time()
print(BinarySearch(l,555)) 
t1=time.time()
print('Time Take', t1-t0)



t0=time.time()
print(BSNon(l,555)) 
t1=time.time()
print('Time Take', t1-t0)
