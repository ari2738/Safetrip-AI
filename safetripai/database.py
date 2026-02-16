def save_user(name, blood_group, contact):

    with open("users.txt", "a") as file:
        file.write(f"{name}, {blood_group}, {contact}\n")
