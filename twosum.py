def twoSum(A, B):
  #Do one pass
  dic={}
  for idx, item in enumerate(A):
    diff=B-item
    if diff not in dic:
      if item not in dic:
        dic[item]=[idx]
      else:
        dic[item].append(idx)  
    else:
        return [min(dic[diff])+1, idx+1]
    print(dic)
print(twoSum([ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ], -3))
