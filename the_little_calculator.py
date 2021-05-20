

print('Welcome to "The little calculator". You can add and subtract.')


def take_input():

    number_first = get_integer_first()
    add_or_subtract = get_operator()
    number_second = get_integer_second()

    return number_first, add_or_subtract, number_second


def get_integer_first():

    number_first = input('Enter first number: ')
    while not str.isdecimal(number_first):
        number_first = input('Error input is not an integer. Enter first number: ')

    return number_first


def get_integer_second():

    number_second = input('Enter second number: ')
    while not str.isdecimal(number_second):
        number_second = input('Error input is not an integer. Enter second number: ')

    return number_second


def get_operator():

    add_or_subtract = input('Type "+" to add or "-" to subtract: ')
    while (add_or_subtract != '+') and (add_or_subtract != '-'):
        add_or_subtract = input('Error. Operator is not defined. Type "+" to add or "-" to subtract: ')

    return add_or_subtract


def subtract(number_first, number_second):

    return int(number_first) - int(number_second)


def add(number_first, number_second):

    return int(number_first) + int(number_second)


def main():

    number_first, add_or_subtract, number_second = take_input()

    if add_or_subtract == '+':
        result = add(number_first, number_second)
    else:
        result = subtract(number_first, number_second)

    print('\n' + number_first + add_or_subtract + number_second + '=' + str(result))


main()

