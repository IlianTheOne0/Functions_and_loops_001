def table_of_multiplication():
    a = 1
    b = 10
    first_space = 1
    second_space = 1

    for i in range(a, b + 1):
        for j in range(a, b + 1):
            if i * j < 10:
                first_space = second_space = 5
            elif 100 > i * j >= 10 and j == 10:
                first_space, second_space = 5, 5
            elif 100 > i * j >= 10 > i:
                first_space, second_space = 5, 4
            elif 100 > i * j >= 10:
                first_space = second_space = 4


            temp = '|' + ' ' * first_space + f'{i}*{j}={i * j}' + ' ' * second_space + '|'
            print(temp, end='')
        print()