#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
    # initialize the list with the first two numbers of the fibonacci sequence
        initial_int = [0, 1]
    # keep adding numbers to the list until it reaches the desired length
        while len(initial_int) < length:
    # the next num in the sequence is the sum of the last two numbers
            initial_int.append(initial_int[-1] + initial_int[-2])
    # print the final list
        print(initial_int)
    pass