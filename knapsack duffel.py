cake_tuples=[(5,10),(2,15), (3,30)]
capacity=20

def max_duffel_bag_value(cake_tuples, capacity):
    if not cake_tuples:
        return 0

    if capacity ==0:
        return 0

    max_at_capacity = [0]*(capacity+1)
    
    for current_capacity in range(capacity+1):
        current_max_value = 0
        
        for cake_weight, value in cake_tuples:

            if cake_weight <= current_capacity:

                current_max_value= max(current_max_value, max_at_capacity[current_capacity-cake_weight] + value)

        max_at_capacity[current_capacity]= current_max_value

    return max_at_capacity[capacity]
            

print(max_duffel_bag_value(cake_tuples, 20))
