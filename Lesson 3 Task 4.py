a = int(input('Put number: '))
b = int(input('Put number: '))
c =  int(input('Put number: '))
number1 = a > 0
number2 = b > 0
number3 = c > 0
g = number1 + number2 + number3
number1n = a < 0
number2n = b < 0
number3n = c < 0
g1 = number1n + number2n + number3n
zero = 3 - g - g1
print(g,g1)