def count3Sum(s, target):
    nums = sorted(s)
    #Check Edge cases
    
    # if  i >= sum add, return it
    
    #Starting from 0 to len-3
    if (not s) and len(s) < 3:
        return False
    result = [[]]
    temp= []
    
    
    for i in range(len(s)-1):
        start=i+1
        end = len(nums)-1
        while(start < end):
            print(start, end)
        #Check if i+1, i+2 = 0 if yes, add it to your list
            if(nums[start]+nums[end] == target-nums[i]):
                temp =  sorted([nums[i],nums[start],nums[end]])
                if temp not in result:
                    result.append(temp)
                    start+=1
            elif(nums[start]+nums[end] < target-nums[i]):
                start+=1
            else:
                end-=1
            
                            
    #return list
    return result
    
           
S = [-1, 0, 1, 2, -1, -4]
S = [-4, -1,-1, 0, 1, 2]

count3Sum(S, 0)