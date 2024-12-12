a, b ,c = input(), input(), input()

if b > a > c or a > b > c:
    print(a)
elif a < b < c or c > b > a:
    print(b)
else:
    print(c)
