# a=int(input('vvedite chislo: '))
# if a % 5 and a > 24 :
#     print(a)
# else: print('err')

n = int(input('n: '))
m = int(input('m: '))
k = int(input('k: '))
numbers = []
while len(numbers) < n:
    if not k % m:
         numbers.append(k)
    k += 1
print(numbers)