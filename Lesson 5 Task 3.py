n = int(input('n: ' ))
for i in range(2, n + 1, 10):
     for j in range(i, i+9, 2):
         if j <= n:
             print(j, end=' ')
         else:
             break
     print()

