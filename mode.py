l=[5,2,2,2,5,5,2,5]


#find the mx no from the given set of elements in an array (without using max function)/ Print Max element of a given ist 


def findmax(l):
    d={}
    current_max=(0,0)
    for i in l:
        d[i] = d.get(i,0)+ 1
        if current_max[1] < d[i]:
            current_max=(i, d[i])
    return current_max[0]
print(findmax(l))
