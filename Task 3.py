import func

if __name__ == '__main__':
    try:
        # a = int(input('Enter the first number: '))
        # b = int(input('Enter the second number: '))
        a, b = 3, 5
        a, b = func.is_the_biggest_check(a, b)

        func.table_of_multiplication(a, b)
    except Exception as e:
        print(f'Error: {e}')