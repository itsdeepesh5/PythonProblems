#Find recurring element from the given list, if there are exact even number of elements
l=[10,40,20,50,40,50,10]

#Create a dictionary or set
s=()
cnt=0
#For each element in the list, check if it exist in dic, remove it else add it.
for i in l:
    if i in s:
       s.remove[i]
    else:
       s.add(i)
print(s)
