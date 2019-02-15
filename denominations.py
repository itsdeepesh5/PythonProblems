amount= 40
denominations=[1,2,3,4]
cache={}
def change_possibilities(amount, denominations):

    answer= top_down_approach(amount, denominations, 0)
    #answer=bottoms_up(amount, denominations)
    return answer

def top_down_approach(amount_left, denominations, current_index):

    # edge cases
    if amount_left == 0:
        return 1

    if current_index == len(denominations):
        return 0
    
    if amount_left < 0:
        return 0
    current_coin = denominations[current_index]
    memo_key= (current_coin, amount)

    if memo_key in cache:
        return cache[memo_key]
    
    num_of_possibility = 0
    while amount_left >=0:
        num_of_possibility += top_down_approach(amount_left, denominations, current_index+1)
        amount_left -= current_coin    

    cache[memo_key] = num_of_possibility
    return  num_of_possibility

def bottoms_up(amount, denominations):
    # edge cases
    if amount <0:
        return 0
    if not denominations:
        raise Exception('No denominations provided')

    ways_to_do = [0]*(amount+1)
    ways_to_do[0]= 1

    #1,2,3
    #4

    #3
    for coin in denominations:

        for amt in range(coin, amount+1): #3, 4  
            ways_to_do[amt]+= ways_to_do[amt- coin]  # [1]= 1 [2]= 1+1 [3]= 1+1+1 [4]= 1+2+1

    return ways_to_do[amount]

import time as t

t1= t.time()
print(change_possibilities(amount, denominations))
t2=t.time()
print(t2-t1)

