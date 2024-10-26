def main():
    while True:
        size = input('Enter the cell size: ')

        try:
            size = int(size)
            break
        except ValueError as e:
            print(f'Error: {e}')
            continue
    print()

    while True:
        try:
            first_symbol, second_symbol = map(str, input('Enter the first and second characters that will make up the board, separated by a space: ').split(' '))
        except Exception as e:
            print(f'Error: {e}')
            continue
        else:
            break

    print('\n' * 10)

    width = 8
    height = 8

    """
    size = 3
    first_symbol = '*'
    second_symbol = '-'
    """

    painter(size, width, height, first_symbol, second_symbol)

def is_even(number):
    return True if number % 2 == 0 else False

def painter(size, width, height, first_symbol, second_symbol):
    print('=' * (size * width + 6))

    for i in range(1, int(height / 2 + 1)):
        print('|| ', end='')
        for j in range(1, int(width / 2 + 1)):
            print(f'{first_symbol * size}{second_symbol * size}', sep='', end='')
        print(' ||', sep='')

        print('|| ', end='')
        for j in range(1, int(width / 2 + 1)):
            print(f'{second_symbol * size}{first_symbol * size}', end='')
        print(' ||', sep='')

    print('=' * (size * width + 6))