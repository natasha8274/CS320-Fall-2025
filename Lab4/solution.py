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

    i_max_value = max(values_to_sort)

    if i_max_value == 0:
        i_max_passes = 1
    else:
        i_max_passes = math.ceil(math.log(i_max_value + 1, base))

    curr_list = list(values_to_sort)
    i_position = 1

    for i_pass_count in range(i_max_passes):
        i_list = [[] for j in range(base)]

        for i_num in curr_list:
            #  isolate num
            i_curr_pos_value = i_num // i_position
            #  Get the digit
            i_digit = i_curr_pos_value % base
            #  Put the whole num in right list of list
            i_list[i_digit].append(i_num)

        #  reset working list
        curr_list = []
        for i_lists in i_list:
            curr_list.extend(i_lists)

        i_position *= base

    #  returns the fully sorted list
    return curr_list

