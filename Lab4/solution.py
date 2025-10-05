def radix_base(values_to_sort, base):
    if values_to_sort is None or values_to_sort == [] or base < 2:
        raise ValueError("invalid arguments")
    return 

• If values_to_sort contains values for which mathematical operations such as division
or modulo are undefned (aka an Exception is raised when you try), or any element of
values_to_sort are less than zero, radix_base() should raise the
ValueError("invalid␣list␣element") exception.