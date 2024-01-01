# ask the user if they want to gen pwd
# if yes => ask pwd len and gen pwed
# print pwd 
# if initial response is no exit program

import string
import random

characters = list(string.ascii_letters  + string.digits + "!@#$%^&*()" )

def generate_password():
    password_lenth = int(input("How long would you like your password to be? "))

    random.shuffle(characters)

    password = []
    for x in range(password_lenth):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)

option = input("Do you want to generate passowrd (y/n): ")
if option.lower() == "y":

    generate_password()
else :
    print("program ended")
    quit()