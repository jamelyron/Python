

def userdata(user, **data):
    print(f"Имя пользователя: {user}")
    for state, param in data.items():
        print(f"{state}: {param},", end=" ")


userdata(input("Имя"), surname=input("Фамилия"), ear=input("Год рождения"), city=input("Город"), email=input("email"), phone=input("Телефон"))