def b(n):
    s = ''
    while n > 0:
        s = str(n%2) + s
        n //= 2
    return s

while 1:
    n = int(input())
    if n != 0:
        print(b(n))
    else:
        break
