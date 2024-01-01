# collect email from user 
# split the email using the @, save the first part as username, the second part is gonna be domain 
# split domain using .

def main():
    print("Welcome to the email slicer ")
    print("")

    email_input = input("input the email address: ")
    
    (username, domain) = email_input.split("@")
    (domain,extension) = domain.split(".")

    print(f"Username: {username} \n Domain: {domain} \n extension: {extension}")
while True:
    main()