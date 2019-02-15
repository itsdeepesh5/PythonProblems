A=[-2,1,-3,4,-1,2,1,-5,4]

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray2(self, A):

        max_sum_so_far= -float('inf')
        max_sum=-float('inf')
        if not A:
            return 0
            
        for i in range(len(A)): #-2 -1
            sum=0
            for j in range(i+1, len(A)): #-3, -4, -1
                for k in range(i, j):
                    sum+=A[k]
            max_sum= max(sum, max_sum)
        max_sum_so_far= max(max_sum, max_sum_so_far) # 1 4 5 6

        return max_sum_so_far

    def maxSubArray(self, A):
        
        #start, end           
       
        # keep adding numbers
        start= 0
        end=1
        max_sum_so_far =A[0]

        while(start<= len(A) and end <=len(A)):
            new_sum = max_sum_so_far + sum(A[start:end])
            if new_sum > max_sum_so_far:
                end+=1
            else:
                start+=1
            max_sum_so_far= max(max_sum_so_far, new_sum)

        return max_sum_so_far
    
    def maxSubArray1(self, A):

        max_sum_so_far= -float('inf')
        current_sum=-float('inf')
        if not A:
            return 0
            
        for num in A:
            if current_sum + num <= 0:
                current_sum= -float('inf')
            else:
                current_sum+= num
            max_sum_so_far= max(current_sum, max_sum_so_far) # 1 4 5 6
        return max_sum_so_far


    def maxSubArray3(self, A):
        max_sum_so_far= 0
        current_sum=0
        if not A:
            return 0
            
        if len(A) ==1:
            return A[0]
        
        mid = int(len(A)/2)
        first_half= self.maxSubArray(A[:mid]) #-2,1,-3,4
        second_half= self.maxSubArray(A[mid+1:]) #-1,2,1,-5,4
        
        right_sum= left_sum=-2**31-1
        
        c_sum=0
        
        for i in range(mid, -1,-1):
            c_sum+=A[i]
            left_sum= max(left_sum, c_sum)
        c_sum=0
        for i in range(mid+1, len(A)):
            c_sum+=A[i]
            right_sum= max(right_sum, c_sum)
    
        maximum_sum= max(first_half, second_half, left_sum, right_sum, left_sum+right_sum)
        
        return maximum_sum
s= Solution()
print(s.maxSubArray2(A))
