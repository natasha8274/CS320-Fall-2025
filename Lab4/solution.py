import math


def radix_base(values_to_sort, base):
    #  not values_to_sort makes sure there are no empty lists
    if values_to_sort is None or values_to_sort == [] or base < 2 or not values_to_sort:
        raise ValueError("invalid arguments")

    for i_value in values_to_sort:
        #  for negatives
        if i_value < 0:
            raise ValueError("invalid list element")

        #  checks math operations are defined
        try:
            #  change variasble name for python conventional throw away var name
            _ = i_value % 1
        except Exception:
            raise ValueError("invalid list element")

    i_max_value = max(values_to_sort)
    
    #  calculation for i_max_passes using math.log and math.ceil
    if i_max_value == 0:
        i_max_passes = 1
    else:
        i_max_passes = math.ceil(math.log(i_max_value + 1, base))

    i_curr_list = list(values_to_sort)
    i_position = 1

    for i_pass_count in range(i_max_passes):
        i_list = [[] for i_j in range(base)]

        for i_num in i_curr_list:
            #  isolate num
            i_curr_pos_value = i_num // i_position
            #  Get the digit
            i_digit = i_curr_pos_value % base
            #  Put the whole num in right list of list
            i_list[i_digit].append(i_num)

        #  reset working list
        i_curr_list = []
        for i_lists in i_list:
            i_curr_list.extend(i_lists)

        i_position *= base

    #  returns the fully sorted list
    return i_curr_list
