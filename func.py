def is_the_biggest_check(a, b): # The unit-test of this functions in the functions/hm/ex_1 branch
    a, b = (b, a) if a > b else (a, b)
    return a, b

def table_of_multiplication(a, b):
    border = 1

    for i in range(a, b + 1):
        for j in range(1, 11):
            if i * j < 10:
                first_space = second_space = 5
            elif 10 > i:
                first_space, second_space = 5, 4
            elif 1000 > i * j >= 100:
                if i >= 100:
                    first_space, second_space = 3, 3
                else:
                    first_space, second_space = 3, 4
            elif i * j >= 1000:
                first_space, second_space = 3, 2
            else:
                first_space = second_space = 4

            if i >= 1000:
                border = 0

            temp = '|' * border + ' ' * first_space\
                    + f'{i}*{j}={i * j}'\
                    + ' ' * second_space + '|' * border
            print(temp, end='')
        print()