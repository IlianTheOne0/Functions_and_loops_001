def main():
    is_input = True
    is_minus = False

    while True:
        if is_input:
            number = number_input()

        try:
            number = int(number)
        except ValueError as e:
            print(f'Error: {e}')
            continue

        if int(number) < 0:
            number = int(number) - int(number) * 2
            is_minus = True

        is_input = False

        option = menu()

        if option == 1:
            print('=' * 50 + f'\nNumber of digits in the {number if not is_minus else f"-{number}"}: {first(number)}\n' + '=' * 50)
        elif option == 2:
            print('=' * 50 + f'\nSum of the digits in the {number if not is_minus else f"-{number}"}: {second(number)}\n' + '=' * 50)
        elif option == 3:
            print('=' * 50 + f'\nArithmetic mean of the digits in the {number if not is_minus else f"-{number}"}: {third(number)}\n' + '=' * 50)
        elif option == 4:
            print('=' * 50 + f'\nNumber of zeros in the {number if not is_minus else f"-{number}"}: {fourth(number)}\n' + '=' * 50)
        elif option == 5:
            is_input = True
            continue
        else:
            break

def number_input():
    return input('Enter the number: ')

def menu():
    print('\n1. Number of digits in the number\n' \
          '2. Sum of the digits in the number\n' \
          '3. Arithmetic mean of the digits in the number\n' \
          '4. Number of zeros in the number', '\n' * 2 + \
          '5. Enter another number\n' \
          '6. Exit\n')

    while True:
        try:
            return int(input('Option: '))
        except ValueError as e:
            print(f'Error: {e}')

def breaker(number):
    temp = []

    for i in str(number):
        temp.append(i)

    return temp

def first(number):
    return len(breaker(number))

def second(number):
    temp = breaker(number)
    result = 0

    for i in temp:
        if i == '-':
            continue

        result += int(i)

    return result

def third(number):
    temp = breaker(number)
    second_function_result = second(number)

    result = round(second_function_result / len(temp), 3)

    return int(result) if result.is_integer() else result

def fourth(number):
    temp = breaker(number)
    result = 0

    # result = temp.count(str(0)) - with using the built-in python function

    for i in temp: # - without using the built-in python function
        if i == str(0):
            result += 1

    return result