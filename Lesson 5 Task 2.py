a = input('+,-,*,/: ')
first_number = float(input('enter the first_number: '))
second_number = float(input('enter the second_number: '))
if a == '+':
    print(first_number+second_number)
elif a == '-':
    print(first_number-second_number)
elif a == '*':
    print(first_number*second_number)
elif a == '/':
    if second_number != 0:
        print(first_number/second_number)
    else:
        print('Деление на ноль невозможно ')




