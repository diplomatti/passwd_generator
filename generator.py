import secrets
import string

running = True

print()
print("--------------------------")
print("~ passwd_generator v0.2.1~")
print("--------------------------")
print()

# Assigining letters digits and characters to variable
alphabet = string.ascii_letters + string.digits + string.punctuation
pwd = alphabet

passwd_length = 15

while running:
    # Empty list for password
    password = []
    
    # Input from user wether to generate new password or exit program
    choice = (int(input("What you want to do?\n1. Generate password\n2. Exit program\n")))
    print()

    # If new password
    if choice == 1:
        for i in range(passwd_length):
            randomchar = secrets.choice(pwd)
            password.append(randomchar)
            
        print("Your super secret password is: " + "".join(password))
        print("-------------------------------------------------")
        print()
        continue

    # If exiting the program
    elif choice == 2:
        running = False

print()
print("Thank you for using passwd_generator!")

