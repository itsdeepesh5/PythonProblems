A=[-5,-1,-2,-3,-4, -5]

def getSubArray(A):
    
    print 'Hello, World'
    start= 0
    end =0 
    gmax=0
    cmax=0
    # edge cases- need to think more
    if not A:
        return False
    for i in range(len(A)):
        cmax+= A[i]

        if cmax < A[i]:
            start = i            
            cmax= A[i]

        if cmax > gmax:
            gmax= cmax
            start=i
    return gmax    

print(getSubArray(A))


def getSubArrayI(A):
    
    prev=0
    count=0
    # edge cases- need to think more
    if not A:
        return False
    for i in range(len(A)):
        if prev < A[i]:
            count+=1
        prev= A[i]
    return count

print(getSubArrayI(A))
