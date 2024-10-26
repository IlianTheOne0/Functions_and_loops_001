# https://stackoverflow.com/questions/5811151/why-do-we-check-up-to-the-square-root-of-a-number-to-determine-if-the-number-is


def main():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))

    a, b = is_the_biggest_check(a, b)

    print(f'Prime numbers from {a} to {b}: {is_prime_number(a, b)}')

def is_the_biggest_check(a, b):
    a, b = (b, a) if a > b else (a, b)
    return a, b

def is_prime_number(a, b):
    temp = str()

    for i in range(a, b + 1):
        if i > 1:
            is_non_prime = True
            for root in range(2, i):
                if i % root == 0:
                    is_non_prime = False
                    break

            if is_non_prime:
                temp += str(i) + ' '

    return temp