import func

if __name__ == '__main__':
    try:
        number = func.number_input()

        while True:
            option = func.menu()

            if option == 1:
                print('=' * 50, f'\nNumber of digits in the number: {func.first(number)}\n', '=' * 50)
            elif option == 2:
                print('=' * 50, f'\nSum of the digits in the number: {func.second(number)}\n', '=' * 50)
            elif option == 3:
                print('=' * 50, f'\nArithmetic mean of the digits in the number: {func.third(number)}\n', '=' * 50)
            elif option == 4:
                print('=' * 50, f'\nNumber of zeros in the number: {func.fourth(number)}\n', '=' * 50)
            elif option == 5:
                number = func.number_input()
            else:
                break
    except Exception as e:
        print(f'Error: {e}')