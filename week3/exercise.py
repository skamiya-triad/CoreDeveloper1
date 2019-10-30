#!/usr/bin/env python

# Week 3 Exercises: Functions

# EXERCISE 1:

# Implement FizzBuzz using function(s) with Clean Code standards

# -----FIZZBUZZ CODE HERE-----


def fizzbuzz(num):

    if num % 15 == 0:
        return 'FIZZBUZZ'
    elif num % 5 == 0:
        return 'BUZZ'
    elif num % 3 == 0:
        return 'FIZZ'
    else:
        return num


if __name__ == '__main__':

    list_1to100 = range(1, 100)
    list_FIZZBUZZ = []

    for i in list_1to100:
        list_FIZZBUZZ.append(fizzbuzz(i))

    print(list_FIZZBUZZ)

# -----END FIZBUZZ CODE-----

# EXERCISE 2:

# Review the payroll.java code in Listing 3-4 in the book

# Re-implement it as clean Python code. See Listing 3-5 for guidance.

# -----PAYROLL CODE HERE-----


# -----END PAYROLL CODE-----
