# define the functions needed, add, sub, multiply and division 
# print options to the user 
# ask for values and call the functions 
# add a while loop to continue the program until the user want to exit

def add(a,b):
    ans = a+b
    print(f"{a} + {b} = {ans}")

def sub(a,b):
    ans = a-b
    print(f"{a} - {b} = {ans}")

def mul(a,b):
    ans = a*b
    print(f"{a} x {b} = {ans}")

def div(a,b):
    ans = a / b
    print(f"{a} / {b} = {ans}")



print ("/n A. Addition \n B. Subtraction \n C. Multiply \n D. Division \n E. Exit")

def inp():
    global a,b
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
# inp function to enter number and other functions for calculations
while True:
    choice = input("\n Enter your choice: ")

    # first we call the function to input the data and then to calculate it ! 
    if choice.lower() == "a":
        inp()  
        add(a,b)
    elif choice.lower() == "b":
        inp()
        sub(a,b)
    elif choice.lower() == "c":
        inp()
        mul(a,b)
    elif choice.lower() == "d":
        inp()
        div(a,b)
    elif choice.lower() == "e":
        quit()
    else:
        print("not specified ")
