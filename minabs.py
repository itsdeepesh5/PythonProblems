l=[1,20,3,4,5,6,7,-5]


#find the mx no from the given set of elements in an array (without using max function)/ Print Max element of a given ist 


def findmax(l):
    max=0
    min=9999999
    d=set(l)
    for i in d:
        if max < i:
            max=i
        if min > i:
            min=i
    return([max-min])

def findabsmin(l):
    diff=set()
    prev=0
    l.sort()
    for i in range(len(l)):
        if i>0:
            diff.add(abs(l[i]-prev))
        prev=l[i]
    return min(diff)
print(findabsmin(l))
