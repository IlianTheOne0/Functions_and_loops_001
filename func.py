from math import sqrt

def is_the_biggest_check(a, b):
    a, b = (b, a) if a > b else (a, b)
    return a, b

def is_prime_number(a, b):
    temp = str()

    while a < b + 1:
        print(a == 6*n - 1)
        # if (6 * a + 1) % 2 != 0 and (6 * a - 1) % 3 != 0:
        #     temp += str(a) + ' '
        a += 1

    return temp