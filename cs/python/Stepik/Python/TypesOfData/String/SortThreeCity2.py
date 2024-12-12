first_city = input()
second_city = input()
third_city = input()

# ищем минимальную длину среди всех городов
min_city_len = min(len(first_city), len(second_city), len(third_city))
# ищем максимальную длину среди всех городов
max_city_len = max(len(first_city), len(second_city), len(third_city))

# длину каждого города сравниваем с минимальной длиной
if len(first_city) == min_city_len:
    print(first_city)
elif len(second_city) == min_city_len:
    print(second_city)
else:
    print(third_city)

# длину каждого города сравниваем с максимальной длиной
if len(first_city) == max_city_len:
    print(first_city)
elif len(second_city) == max_city_len:
    print(second_city)
else:
    print(third_city)