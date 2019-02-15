class Solution:
        # 
    def numDecodings(self, s: 'str') -> 'int':
        
        if len(s)==0:
            return 1
        
        if s[0]=='0':
            return 0

        if len(s)==1:
            return 1
        #dic=[0]*len(s)
        #decode_list=set(map(str,range(1,27)))
        #
        a=1
        b=1


        for digit in range(1, len(s)):
            if s[digit] =='0':
                a= 0
            if s[digit-1] =='1' or ( s[digit-1] =='2' and s[digit] <= '6'):
                a=a+b
                b=a-b
            else:
                b=a
            
        return a

