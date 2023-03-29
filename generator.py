import secrets
import string

running = True

print()
print("------------------------")
print("~ passwd_generator v0.2~")
print("------------------------")
print()


while running:


    letters = string.ascii_letters
    digits = string.digits
    characters = string.punctuation

    passwd_length = 15
    alphabet = letters + digits + characters
    pwd = alphabet

    password = []
    
    choice = (int(input("What you want to do?\n1. Generate password\n2. Exit program\n")))
    print()

    if choice == 1:
        for i in range(passwd_length):
            randomchar = secrets.choice(pwd)
            password.append(randomchar)
            
        print("Your super secret password is: " + "".join(password))
        print("-------------------------------------------------")
        print()
        continue

    elif choice == 2:
        running = False

print()
print("Thank you for using passwd_generator")

