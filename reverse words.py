s="    the sky is blue "

class Solution(object):
    
    def reverseString(self, s, start, end):
        # Edge Cases
        
        while start < end:
            s[start], s[end] = s[end], s[start]
            start+=1
            end-=1
        return True
    
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #
        #"the sky is blue"
        # "  eulb si yks  eht "
        s= list(s)
        
        #Edge Cases
        #reverse whole String
        self.reverseString(s, 0, len(s)-1)
        #length=0
        start=0
        for i in range(len(s)+1):
            if i == len(s) or s[i] ==" ":
                self.reverseString(s,start,i-1)
                start=i+1
                    
        return ''.join(s)


sol= Solution()
print(sol.reverseWords(s))
