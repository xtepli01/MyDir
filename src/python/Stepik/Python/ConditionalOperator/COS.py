#1

a1 = int(input("What's first point?"))
b1 = int(input("What's second point?"))
a2 = int(input("What's third point?"))
b2 = int(input("What's fourth point?"))

if a1 and b1 < a2 and b2:
    print("пустое множество")
elif a2 and b2 < a1 and b1:
    print("пустое множество")
elif (a1 == a2 and b1 < b2) or (a1 > a2 and b1 < b2) or (a1 > a2 and b1 == b2):
    print(a1, b1)
elif (a2 == a1 and b2 < b1) or (a2 > a1 and b2 < b1) or (a2 > a1 and b2 == b1):
    print(a2, b2)
elif (a1 < b1 == a2 < b2):
    print(b1)
elif (a2 < b2 == a1 < b2):
    print(b2)
elif a1 < a2 < b1 < b2:
    print(a2, b1)
elif a2 < a1 < b2 < b1:
    print(a1, b2)
elif a1 == a2 and b1 == b2:
    print(a1,b1)