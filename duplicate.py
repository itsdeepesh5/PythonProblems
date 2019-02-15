#Find recurring element from the given list, if there are exact even number of elements
names = ["Bob", "Jill", "Bob", "Alice"]
print("Unordered",set(names))
dup=[]
dic=set()
for i in names:
    if i in dic:
       dup.append(i)
    else:
       dic.add(i)
print(dup)    
