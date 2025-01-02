x1 = int(input("Set on column 1 : "))
y1 = int(input("Set on string 1 : "))
x2 = int(input("Set on column 2 : "))
y2 = int(input("Set on string 2 : "))

# Проверяем возможность хода конем
if (abs(x2 - x1) == 2 and abs(y2 - y1) == 1) or (abs(x2 - x1) == 1 and abs(y2 - y1) == 2):
    print("YES")
else:
    print("NO")