a = int(input("Type number 1: "))
b = int(input("Type number 2: "))
c = input("Type the operation: ")


if c == '/' and b == 0:
    print('На ноль делить нельзя!')
elif c == "/":
    print(a / b)
elif c == "*":
    print(a * b)
elif c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
else:
    print('Неверная операция')