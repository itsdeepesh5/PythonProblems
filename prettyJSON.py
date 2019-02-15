class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def prettyJSON(self, A):


        # Edge Cases
        if not A:
            return 0
        tabs="\t"
        #Read each element
        special_chars_start=set(['[','{'])
        special_chars_end=set(['}',']'])
        merge_list=[]
        tabs_count=0
        for char in A:
            if char in special_chars_start:
                #print('TABS',tabs_count )
                print ('\n')
                tabs_count+=1
                print (tabs*tabs_count, end='')
                print(char, end='')
                print ('\n')
                print (tabs*tabs_count, end='')
            elif char in special_chars_end:
                
                print ('\n')
                print (tabs*tabs_count, end='')
                #print('TABS',tabs_count)
                print(char, end='')
                tabs_count-=1
            elif char in ',':
                print(char, end='')
                print ('\n')
                print (tabs*tabs_count, end='')
            else:
                print(char, end='')
        return 



Input= '["foo", {"bar":["baz",null,1.0,2]}]'
A="Helloworld"
B="world"
s= Solution()
s.prettyJSON(Input)
