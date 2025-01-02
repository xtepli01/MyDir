x1 = int(input("Set on column 1 : "))
y1 = int(input("Set on string 1 : "))
x2 = int(input("Set on column 2 : "))
y2 = int(input("Set on string 2 : "))


if (x1 + y1) % 2 == 0 and (x2+ y2 )% 2 == 0:
    print('YES')
elif (x1 + y1) % 2 != 0 and (x2 + y2) % 2 != 0:
    print('YES')
else:
    print('NO')
