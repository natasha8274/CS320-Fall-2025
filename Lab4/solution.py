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
    
    if not values_to_sort:
        return []
    #  returns empty list
    
    max_value = max(values_to_sort)
    
    if max_value == 0:
        max_passes = 1
    else:
        max_passes = math.ceil(math.log(max_value + 1, base))
    
    current_list = list(values_to_sort)
    return 
