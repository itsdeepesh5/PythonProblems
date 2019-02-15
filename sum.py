#Python code to find sum of any 2 numbers in a list is equal to a given number.

def findSum(l,s):
  d=[]
  for i in l:
    #Add a difference list
#   d[s-i]= d.get(s-i,1)
    if i in d:
      return (i, s-i)
    else:
      d.append(s-i)
  return False
  #parse list and for each individual record, save the diff in the list
  #if that differnce exist in the list, we found the sum pair

def findSumEff(l,s):
  d={}
  for i in l:
    #Add a difference list
    if d.get(s-i,0)==0:
      return (i, s-i)
    else:
      d[s-i]=d.get(s-i)
    print(d)  
  return False
  #parse list and for each individual record, save the diff in the list
  #if that differnce exist in the list, we found the sum pair

str=[1,2,3,4,5]
sum=7
print(findSum(str, sum))
