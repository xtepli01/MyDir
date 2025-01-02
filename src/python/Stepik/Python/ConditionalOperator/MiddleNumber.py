a = int(input("First number:")) 
b = int(input("Second number:"))
c = int(input("Third number:"))

if b > a > c or c > a > b:
    print(a)
elif (a > b > c) or (a < b < c):
    print(b)
else:
    print(c)
