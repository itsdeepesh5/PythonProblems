arr = [1, 2, 2, 3, 1]
def finddups(arr):

    if not arr and len(arr) <2 :
        return []
    
    dic=set()
    result= []
    
    for item in arr:
        if item in dic:
            result.append(item)
        else:
            dic.add(item)
    
    return result

arr1 = 'CAT'

def findsubsets(arr):
    if not arr:
        return []
    
    if len(arr)<= 1:
        return set([arr])
    
    print('CAlled for', arr)
    # 3 2, 1
    last_item = arr[-1]
    all_subsets= findsubsets(arr[:-1])
    #print('All subsets', all_subsets)
    result=[]

    for subset in all_subsets:
        for i in range(len(arr)):
            result.append((subset[:i]+last_item+subset[i:]))
        
    return result
    
arr1 = [1,2,3]


def findsubsets1(arr):
    if not arr:
        return []
    
    if len(arr)<= 1:
        return set([arr])
    # 1,2,3

#[]    
#[1]
#[2] [1,2]
#[3], [2, 3] [1,2, 3]  
    
    result=[[]]
    subset=[]
    temp=[]
    for item in arr: #1
        for i in range(len(result)):
            #temp= result.append(result[i])
            #temp.append(item)
            result.append(result[i]+[item])
        
    return result
    
    
import time as t

t1= t.time()
print(findsubsets1(arr1))
t2=t.time()
print('Time', t2-t1)
