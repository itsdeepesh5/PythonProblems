s="abcde"
print(s[::-1])
sl=list(s)
n=len(s)
for i in range(n//2):
  temp=sl[i]
  sl[i]=sl[n-1-i]
  sl[n-1-i]=temp
  s="".join(sl)
print(s)


# Left and Right
left=0
right=len(s)-1
tmp=0
s=list(s)
while left < right:
  tmp=s[left]
  s[left]= s[right]
  s[right]=tmp
  left+=1
  right-=1
s1="".join(s)
print(s1)
