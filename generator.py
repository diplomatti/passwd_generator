import secrets
import string
# import os

running = True
ready = True

print()
print("--------------------------")
print("~ passwd_generator v0.2.2~")
print("--------------------------")
print()

passwd_length = 15

# Clear the terminal screen
# os.system('cls' if os.name == 'nt' else 'clear')

while running:
    # Empty list for password
    password = []
    pwd = ""

    # Input from user wether to generate new password or exit program
    choice = (int(input("What you want to do?\n1. Generate password\n2. Exit program\n")))
    print()

    # If new password
    if choice == 1:
        print("Choose password content from these:\n1. Letters\n2. Digits\n3. Special characters\n4. Continue")
        
        while ready:
            pw_contents = int(input())
            if pw_contents == 1:
                pwd += string.ascii_letters
            elif pw_contents == 2:
                pwd += string.digits
            elif pw_contents == 3:
                pwd += string.punctuation
            elif pw_contents == 4:
                break
            else:
                print("Please pick a valid option")
            
        for i in range(passwd_length):
            randomchar = secrets.choice(pwd)
            password.append(randomchar)

        print("-------------------------------------------------")
        print("Your super secret password is: " + "".join(password))
        print("-------------------------------------------------")
        print()

        continue

    # If exiting the program
    elif choice == 2:
        running = False

print()
print("Thank you for using passwd_generator!")

