#Find max element of a given list
l=[-1,2,3,4,235,1234567]
#Setup temporary dictionary variable
current_max= l[0]
#for each item in list , if more than current max, swap else skip
for i in l:
    if i > current_max:
        current_max=i
print(current_max)


