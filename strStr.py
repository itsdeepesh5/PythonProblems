class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        n=len(B)
        h=len(A)
        
        if n > h:
            return -1
        if A==B:
            return 0
        #helloworld 
        #world
        
        for i in range(0,h-n+1):
            # A[0:5] dee
            # 1:4
            print(A[i:i+n], B)
            if A[i:i+n] == B:
                return i

        return -1

A="Helloworld"
B="world"
s= Solution()
print(s.strStr(A,B))
