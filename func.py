def number_input():
    return input('Enter the number: ')

def menu():
    print('\n1. Number of digits in the number\n' \
          '2. Sum of the digits in the number\n' \
          '3. Arithmetic mean of the digits in the number\n' \
          '4. Number of zeros in the number', '\n' * 2 + \
          '5. Enter another number\n' \
          '6. Exit\n')

    return int(input('Option: '))

def breaker(number):
    temp = list()

    for i in number:
        temp.append(i)

    return temp

def first(number):
    return len(breaker(number))

def second(number):
    temp = breaker(number)
    result = int()

    for i in temp:
        result += int(i)

    return result

def third(number):
    temp = breaker(number)
    second_function_result = second(number)

    result = round(second_function_result / len(temp), 3)

    return int(result) if result.is_integer() else result

def fourth(number):
    temp = breaker(number)
    result = int()

    # result = temp.count(str(0)) - with using the built-in python function

    for i in temp: # - without using the built-in python function
        if i == str(0):
            result += 1

    return result