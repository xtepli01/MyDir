age_dog = float(input())


if age_dog == 1 or age_dog == 2:
    age_dog = age_dog*10.5
    print(age_dog)
elif age_dog > 2:
    age_dog = (age_dog- 2)*4+21
    print(age_dog)