x1 = int(input("Set on column 1 : "))
y1 = int(input("Set on string 1 : "))
x2 = int(input("Set on column 2 : "))
y2 = int(input("Set on string 2 : "))

# Проверяем возможность хода ферзем
if x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 - y1):
    print("YES")
else:
    print("NO")