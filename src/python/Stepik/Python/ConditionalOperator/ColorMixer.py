color1 = input("What's your's first color? ")
color2 = input("What's your's second color? ")


if color1 == 'красный' and color2 == 'красный':
    print(color1)

elif color1 == 'синий' and color2 == 'синий':
    print(color1)

elif color1 == 'желтый' and color2 == 'желтый':
    print(color1)
    
elif color1 == 'красный' and color2 == "синий" or color1 == "синий" and color2 == "красный":
    print("фиолетовый")
    
elif color1 == 'красный' and color2 == "желтый" or color1 == "желтый" and color2 == "красный":
    print("оранжевый")

elif color1 == 'синий' and color2 == "желтый" or color1 == "желтый" and color2 == "синий":
    print("зеленый")

else:
    print('ошибка цвета')
