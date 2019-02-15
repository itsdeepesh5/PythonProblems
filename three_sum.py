
nums=[-1, 0, 1, 2, -1, -4]
class Solution:
    def twoSum(self,nums: 'List[int]', start, end, target) -> 'List[int]':
        
        dic={}
        dic2={}
        result=[]
        for num in nums[start:end+1]:
            if target-num not in dic:
                dic[num]=1
            else:
                if num not in dic2:   
                    result.append([num, target-num])
                    dic2[num]=1
        return result

    def threeSum1(self, nums: 'List[int]') -> 'List[List[int]]':
        
        #[-1, 0, 1, 2, -1, -4]
        
        res = []
        Dict = {}
        nums.sort()
        for i in range(0,len(nums)):
            start=i+1
            end= len(nums)-1
            target = -nums[i]
            if target not in Dict:
                Dict[target] =1
                l = self.twoSum(nums, start, end, target)
                if len(l) >0:
                    for x in l:
                        x.append(nums[i])
                        res.append(x)
            # else:
            #     print("hey")
            
        return sorted(res)        
    def threeSum(self, nums):
        dic = {}
        res=[]
        if len(nums)==0:
            return []
        #[-1, 0, 1, 2, -1, -4]
        for i in range(len(nums)-2):
            #print(res)
            target= -nums[i]
            if target not in dic:
                dic[target]=1
                start=i+1
                end=(len(nums)-1)
                two_sum=self.twoSum(nums, start, end, target) # 0,1, 2,-1
                if len(two_sum) > 0:
                    for item in two_sum:
                        item.append(nums[i])
                        l=sorted(item)
                        if l not in res:
                            res.append(l)
        return sorted(res)

import time as t
t1=t.time()
s=Solution()
print(s.threeSum1(nums))
t2=t.time()
print(t2-t1)
