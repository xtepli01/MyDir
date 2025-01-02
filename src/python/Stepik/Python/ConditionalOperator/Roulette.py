#Roulette is a game of chance.

num = int(input("Select a number: "))

if num == 0:
    print('зеленый')

elif 1 <= num <= 10 and num % 2 == 0:
    print('черный')
elif 1 <= num <= 10 and num % 2 != 0:
    print('красный')

elif 11 <= num <= 18 and num % 2 == 0:
    print('красный')
elif 11 <= num <= 18 and num % 2 != 0:
    print('черный')

elif 19 <= num <= 28 and num % 2 == 0:
    print('черный')
elif 19 <= num <= 28 and num % 2 != 0:
    print('красный')

elif 29 <= num <= 36 and num % 2 == 0:
    print('красный')
elif 29 <= num <= 36 and num % 2 != 0:
    print('черный')

elif num > 36 or num < 0:
    print("ошибка ввода")




