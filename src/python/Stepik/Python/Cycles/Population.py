m, p, n = int(input("one ")), int(input("two ")), int(input("three "))
cur_population = float(m)

for i in range(n):
    cur_population = cur_population * (1 + p / 100)
    print(i + 1, cur_population)
    