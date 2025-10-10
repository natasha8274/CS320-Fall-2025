import math

def radix_base(values_to_sort, base):
    if values_to_sort is None or values_to_sort == [] or base < 2:
        raise ValueError("invalid arguments")
    
    for i in values_to_sort:
        #  for negatives 
        if i < 0:
            raise ValueError("invalid list element")
        
        #  checks math operations
        try:
            test = i % 1
        except Exception:
            raise ValueError("invalid list element")
    
    #  checks for only 0s
    if not values_to_sort:
        return []
    #  returns empty list
    
    max_value = max(values_to_sort)
    
    return 
