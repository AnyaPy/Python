users = {"Anya":{"password": "test@", "likes": [], "DiseLikes": [], "coment": [] }, "Arina": {"password": "12345", "likes": [], "DiseLikes": [], "coment": []}}
user = {}

def give_like(user):
    liked_user = input("Введіть користувача якому ви ставите лайк:  ")
    try:
        liked_user = users[liked_user]
        likes = liked_user["likes"]
        likes.append(user)
        print(f"Лайки користувача:  ")
        print(likes)
    except:

        print("Такого юзера не існує")

def registration(username,password):
    strength = check_password_strength(password)
    if strength is None:
        print("Password weak")
        return
    users[username]= {
        "password": password,
        "likes": [],
        "DiseLikes": [],
        "coment": []
    }

    return"Ви зареєстровані"

def login(username,password):
    if users[username]["password"] != password:
        print("Неправильний пароль")
        return
    return "Bи увійшли у аккаунт"

def check_password_strength(password):
    with open("common", "r", encoding="utf-8") as file:
        common = file.read().split()
        if password in common:
            return None
        else:
            return True

def give_DiseLike(user):
    DiseLike_user = input("Введіть користувача якому ви ставите ДизЛайк:  ")
    try:
        DiseLike_user = users[DiseLike_user]
        DiseLikes = DiseLike_user["DiseLikes"]
        DiseLikes.append(user)
        print(f"ДизЛайки користувача:  ")
        print(DiseLikes)
    except:
        print("Такого юзера не існує")

def coment(user):
    coment_user = input("Введіть користувача якому ви пишите коментар:  ")
    try:
        coment_user = users[coment_user]
        coment = coment_user["coment"]
        coment.append(user)
        print(f"Коментарі користувача:  ")
        print(coment)
    except Exeption as e:
        print(e)
        print("Такого юзера не існує")

def main():
    username = "Alex"
    while True:
        password = input("Твій пароль:  ")
        if username not in users:
            result = registration(username,password)
        else:
            result = login(username,password)
        if result:
            print(result)
            break

if __name__ == "__main__":
    main()