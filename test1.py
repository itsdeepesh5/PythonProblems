str="Aevum is my son"
cnt=[]
for i in str.split():
  cnt.append(len(i))
  print(cnt)    
print(sum(cnt)/len(str.split()))
  
