def BS(num, x):
    if len(num)==0 or x is None:
        return -1

    floor=0
    ceil= len(num)

    while floor < ceil: # 0 < 9  5 < 9  5<7
        middle = int((ceil+floor)/2) #4  7 6
        guess=num[middle]  #4 #7  6
        print('Search', x)        
        if guess==x: 
            return middle
        elif guess > x: 
            ceil=middle
        elif guess < x:
            floor=middle+1
    return -1

def find_rotation_point(words):
    
    if len(words) < 2:
        return words
        #['grape', 'orange', 'plum', 'radish', 'apple']
    return binarySearch(words, words[0])
    
def binarySearch(words, word):
    #middle= len(words)/2
    floor=0
    ceil=len(words)  
    
    # Find the rotation point in the list
   
    while floor < ceil:
        middle= int((ceil+floor)/2) #4
        if middle >= 1 and words[middle] < words[middle-1]:
            return middle
        elif words[middle] > word:
            floor= middle+1
        elif word > words[middle]:
            ceil= middle
        
    return -1  


num=['apple', 'grape', 'orange', 'plum', 'radish']

#print(BS(num, 2))
print(find_rotation_point(num))

