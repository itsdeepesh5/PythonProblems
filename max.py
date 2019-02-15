l=[1,20,3,4,5,6,7,5]


#find the mx no from the given set of elements in an array (without using max function)/ Print Max element of a given ist 
print("Printing", sorted(l)[len(l)-1])

max=0
d=set(l)
for i in d:
    if max < i:
        max=i
print(max)
