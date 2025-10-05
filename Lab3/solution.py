from collections import Counter
# this a = 1 b = 2 for string 2 to find them in any order 


def countPermStr(string1, string2):
    if not string2:
        raise ValueError("String empty")
    if string2 is None or string1 is None:
        raise ValueError("String is none")
    if len(string1) < len(string2):
        raise ValueError("String2 is longer than string 1")
    amount = 0
    m = len(string2)
    n = len(string1)
    count_string2 = Counter(string2) 
    #  starting counter for string 2
    current_string1 = Counter(string1[0:m])
    #  quicker and easier way to get the string

    #  if the string matches the amount of matches increases
    if current_string1 == count_string2:
        amount += 1

    #  remove the first letter in current string1 counter
    #  start at m and go up to n 
    for i in range(m, n):
        remove = string1[i - m]
        current_string1[remove] -= 1

        # Add the new letter to the check counter
        adding = string1[i]
        current_string1[adding] += 1

        #  check if there is a match in the current substring
        if current_string1 == count_string2:
            amount += 1

    return amount
