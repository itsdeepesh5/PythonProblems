def find_repeat(the_list):
    floor = 1
    ceiling = len(the_list) - 1

    while floor < ceiling:
	# Divide our range 1..n into an upper range and lower range
	# (such that they don't overlap)
	# Lower range is floor..midpoint
	# Upper range is midpoint+1..ceiling
        midpoint = floor + int((ceiling - floor) / 2) #4  
        lower_range_floor, lower_range_ceiling = floor, midpoint # 0, 4 [4, 1, 4, 8, 3
        upper_range_floor, upper_range_ceiling = midpoint+1, ceiling #5, 9 # 2, 7, 6, 5
    
	# Count number of items in lower range
        items_in_lower_range = 0
        for item in the_list:
            # Is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1
        distinct_possible_integers_in_lower_range = (lower_range_ceiling- lower_range_floor+ 1)
        
        if items_in_lower_range > distinct_possible_integers_in_lower_range:
		# There must be a duplicate in the lower range
		# so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
		# There must be a duplicate in the upper range
		# so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling
    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor

print(find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5]))
