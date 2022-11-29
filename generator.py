import secrets
import string
from pyfiglet import Figlet

f = Figlet(font='cybermedium')
print(f.renderText("password\ngenerator"))
print("-------------------------------------------")
print()
print("Pick from number 1 to 3 what you want to include in your passwrd")
print("After selecting proceed to print the password with number 4.")
print()
print("1 = Letters")
print("2 = Digits")
print("3 = Characters")
print()
print("4 = CONTINUE")
print()
print()
print()
letters = string.ascii_letters
digits = string.digits
characters = string.punctuation

alphabet = letters + digits + characters



passwd_length = 15


pwd = ''

while True:
    choice = int(input("Pick a number:\n"))
    if choice == 1:
        pwd += string.ascii_letters
    elif choice == 2:
        pwd += string.digits
    elif choice == 3:
        pwd += string.punctuation
    elif choice == 4:
        break
    else:
        print("Please pic a valid option")

password = []

for i in range(passwd_length):
    randomchar = secrets.choice(pwd)
    password.append(randomchar)

print("The random password is: " + "".join(password))
