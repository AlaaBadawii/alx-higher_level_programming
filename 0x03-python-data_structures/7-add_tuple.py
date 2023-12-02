#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a == 0:
        tuple_a_0 = 0
        tuple_a_1 = 0
    elif len_a == 1:
        tuple_a_0 = tuple_a[0]
        tuple_a_1 = 0
    else:
        tuple_a_0 = tuple_a[0]
        tuple_a_1 = tuple_a[1]

    if len_b == 0:
        tuple_b_0 = 0
        tuple_b_1 = 0
    elif len_b == 1:
        tuple_b_0 = tuple_b[0]
        tuple_b_1 = 0
    else:
        tuple_b_0 = tuple_b[0]
        tuple_b_1 = tuple_b[1]

    a = tuple_a_0 + tuple_b_0
    b = tuple_a_1 + tuple_b_1

    new_tuple = (a, b)
    
    return (new_tuple)
