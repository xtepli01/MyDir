x1 = int(input("Set on column 1 : "))
y1 = int(input("Set on string 1 : "))
x2 = int(input("Set on column 2 : "))
y2 = int(input("Set on string 2 : "))

# Проверка, ходит ли слон по диагонали
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')