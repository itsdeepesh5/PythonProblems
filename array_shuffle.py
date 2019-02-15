arr=[2,4,6,1,3]
import random


def get_random_index(floor, ceil):
    return random.randrange(floor, ceil+1)
    
    
def reorder(arr):
    # Get radom number between range
    # edge cases
    if len(arr) ==0:
        return []

    if len(arr) ==1:
        return arr
    
    for index in range(len(arr)-1, -1 ,-1):
        random_index= get_random_index(0, index)
        if index != random_index:
            arr[index], arr[random_index]= arr[random_index], arr[index]
        
    return arr


print('BEfore',arr)
print(reorder(arr))

    





