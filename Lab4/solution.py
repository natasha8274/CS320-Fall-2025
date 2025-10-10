def radix_base(values_to_sort, base):
    if values_to_sort is None or values_to_sort == [] or base < 2:
        raise ValueError("invalid arguments")
    
    for i in values_to_sort:
        #  for negatives 
        if i < 0:
            raise ValueError("invalid list item")
    return 
