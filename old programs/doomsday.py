# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 15:20:02 2017

@author: Deepesh K Rana
"""
  
#m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

def inc(start, i):
    start+= i
    i+=1
    return start
def givevalues(start, length):
    return [start+length, length-1]

 #   l= [range(start , start+leng)]
    #start+=length
#    return l
def xor(a,b):
    return a^b

def answer(start, length):
    leng= length
    
    #while(leng > 0):
    print([ range(start, start+len) for start, len in givevalues(start, leng)])
    #    leng-=1
     #   start+= length    
    return 0 #reduce(xor,l)

        #l1.append(l)
        #temp+=length 
        #print(temp, l, l1)
    #print(17^18^19^20^21^22^23^25^26^29)
    #print(m[i] for i in range(len(m)))
    return 1 #range(length*length)

if __name__ == "__main__":

    a = answer(0,3)
    print(a)
    
