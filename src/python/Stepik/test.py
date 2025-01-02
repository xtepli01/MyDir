age = int(input("What's your's age?"))

d1 = age // 1000
d2 = age // 100 % 10
d3 = age % 100 // 10
d4 = age % 10

print(d1, d2, d3, d4)