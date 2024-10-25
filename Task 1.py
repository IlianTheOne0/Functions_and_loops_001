import func
from func import *

if __name__ == '__main__':
    try:
        a = int(input('Enter the first number: '))
        b = int(input('Enter the second number: '))

        a, b = func.is_the_biggest_check(a, b)

        print(f'Prime numbers from {a} to {b}: {func.is_prime_number(a, b)}')
    except Exception as e:
        print(f'Error: {e}')