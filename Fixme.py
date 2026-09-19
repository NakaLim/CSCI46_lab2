#!/usr/bin/python3

def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''
    num_to_n = list(map(lambda x: x, range(n + 1)))
    even_num = filter(lambda x: x % 2 == 0, num_to_n)
    return list(even_num)
