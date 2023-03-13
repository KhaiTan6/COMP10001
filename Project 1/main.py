# Question 1
def smallest_first(capacity, bookings):
    """Takes a number for capacity and a list for bookings. It then returns the 
    total number of diners within the capacity, starting from smallest group
    first."""
    
    # sort the number of diners from smallest to largest according to size
    booking_quantity = []
    for tup in bookings:
        booking_quantity.append(tup[1])
    booking_quantity_sorted = sorted(booking_quantity)
    
    # sum up the number of diners according to group without exceeding capacity
    max_cap = 0
    for num in booking_quantity_sorted:
        if max_cap + num <= capacity:
                max_cap += num
    return max_cap        

# Question 2
def biggest_first(capacity, bookings):
    """Takes a number for capacity and a list for bookings. It then returns the 
    total number of diners within the capacity, starting from biggest group 
    first."""
    
    # sort the number of diners from largest to smallest according to size
    booking_quantity = []
    for tup in bookings:
        booking_quantity.append(tup[1])
    booking_quantity_sorted = sorted(booking_quantity, reverse=True)
    
    # sum up the number of diners according to group without exceeding capacity
    max_cap = 0
    for num in booking_quantity_sorted:
        if max_cap + num <= capacity:
                max_cap += num
    return max_cap

# Question 3          
def exhaustive_search(capacity, bookings):
    """Takes a number for capacity and a list for bookings. It then returns the 
    most number of diners within the capacity."""
    
    # append number of diners by group into a list
    booking_quantity = []
    for tup in bookings:
        booking_quantity.append(tup[1])
    
    # append all possible combinations of booking as tuple into a list
    import itertools
    # (https://www.kite.com/python/answers/how-to-find-all-combinations-of-a-l
    # ist-in-python)
    all_combinations = []
    for r in range(len(booking_quantity) + 1):
        combinations_object = itertools.combinations(booking_quantity, r)
        combinations_list = list(combinations_object)
        all_combinations += combinations_list
        
    # sum up the number of diners according to group without exceeding capacity
    max_cap = 0
    for tuples in sorted(all_combinations, key=sum, reverse=True):
        for elem in tuples:
            if elem == capacity:
                max_cap = elem
                return max_cap
                break
            max_cap += elem
        if max_cap == capacity:
            return max_cap
        elif max_cap <= capacity:
            return max_cap
        max_cap = 0
    return max_cap


# Question 4
#incomplete
#biggest first search strat
def biggest_spend_first(capacity, bookings):

    # TODO implement this function.
    """Takes a number for capacity and a list for bookings. It then returns the 
    most number of diners in the accepted bookings."""
    
    # append number of diners and amount spend as tuples into a list
    booking_quantity1 = []
    for tup in bookings:
        booking_quantity1.append(tup[1])
    
    booking_quantity2 = []
    for tup in bookings:
        booking_quantity2.append(tup[2])
    
    # append all possible combinations of booking in tuple into a list
    import itertools
    # (https://www.kite.com/python/answers/how-to-find-all-combinations-of-a-l
    # ist-in-python)
    all_combinations1 = []
    for r in range(len(booking_quantity1) + 1):
        combinations_object1 = itertools.combinations(booking_quantity1, r)
        combinations_list1 = list(combinations_object1)
        all_combinations1 += combinations_list1
        
    all_combinations2 = []
    for r in range(len(booking_quantity2) + 1):
        combinations_object2 = itertools.combinations(booking_quantity2, r)
        combinations_list2 = list(combinations_object2)
        all_combinations2 += combinations_list2
    
    all_combinations1_sorted = sorted(all_combinations1, key=len, reverse=True)
    all_combinations2_sorted = sorted(all_combinations2, key=len, reverse=True)
    
    maxcap_maxrev_list = []
    for tuples1, tuples2 in zip(all_combinations1_sorted, all_combinations2_sorted):
        maxcap_maxrev_list.append((sum(tuples1),sum(tuples2)))
        
        
    # sum up the number of diners according to group without exceeding capacity
    max_cap = 0
    max_rev = 0
    for tuples in maxcap_maxrev_list:
        if tuples[0] == capacity:
            max_cap = tuples[0]
            max_rev = tuples[1]
        if tuples[0] <= capacity and tuples[1] > max_rev:
            max_rev = tuples[1]
    return max_rev

#exhaustive search strat
def biggest_spend_first(capacity, bookings):
    # Please mark this question.
    """Takes a number for capacity and a list for bookings. It then returns the 
    maximum revenue for the total number of diners dining within the 
    capacity."""
    
    # append number of diners as tuples into a list
    booking_quantity = []
    for tup in bookings:
        booking_quantity.append(tup[1])
    
    # append amount spend as tuples into a list
    revenue_quantity = []
    for tup in bookings:
        revenue_quantity.append(tup[2])
    
    # append all possible combinations of booking as tuples into a list
    import itertools
    # (https://www.kite.com/python/answers/how-to-find-all-combinations-of-a-l
    # ist-in-python)
    booking_combinations = []
    for r in range(len(booking_quantity) + 1):
        combinations_object1 = itertools.combinations(booking_quantity, r)
        combinations_list1 = list(combinations_object1)
        booking_combinations += combinations_list1
    
    # append all possible combinations of amount spend as tuples into a list
    revenue_combinations = []
    for r in range(len(revenue_quantity) + 1):
        combinations_object2 = itertools.combinations(revenue_quantity, r)
        combinations_list2 = list(combinations_object2)
        revenue_combinations += combinations_list2
    
    booking_combinations_sorted = sorted(booking_combinations, key=len,
                                         reverse=True)
    revenue_combinations_sorted = sorted(revenue_combinations, key=len,
                                         reverse=True)
    
    # append the sum of bookings and the sum of amount spend 
    # as tuples into a list.
    maxcap_maxrev_list = []
    for tuples1, tuples2 in zip(booking_combinations_sorted,
                                revenue_combinations_sorted):
        maxcap_maxrev_list.append((sum(tuples1), sum(tuples2)))
        
        
    # sum up the amount spend according to group without exceeding capacity.
    max_rev = 0
    for tuples in maxcap_maxrev_list:
        if tuples[0] == capacity and tuples[1] > max_rev:
            max_rev = tuples[1]
        if tuples[0] <= capacity and tuples[1] > max_rev:
            max_rev = tuples[1]
    return max_rev