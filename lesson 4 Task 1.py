# numbers=[i**1 for i in range (2, 3 )]
# numbers2=[i**2 for i in range (2, 3 )]
# numbers3=[i**3 for i in range (2, 3 )]
# numbers4=[i**4 for i in range (2, 3 )]
# numbers5=[i**5 for i in range (2, 3 )]
# numbers6=numbers+numbers2+numbers3+numbers4+numbers5
# print(numbers6)
p = int(input("Показатель степени: "))
n = int(input("Предел: "))

i = 2
while i ** p <= n:
    print(i ** p, end=' ')
    i += 1

print("\nПоследнее число,"
      " возведенное в степень:", i - 1)
