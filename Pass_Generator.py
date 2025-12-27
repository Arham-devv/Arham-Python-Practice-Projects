import random
import string

lent = int(input("Enter length of your password that you want to generate: "))
password = ""

all_characters = string.ascii_letters + string.digits + string.punctuation

for ch in range(lent):
    password += random.choice(all_characters)

print("Your generated password is:", password)

def check_digit(password):
    for ch in password:
        if ch.isdigit():
            print("Yes the password contains digit")
            return True
    return False

def check_special(password):
    for ch in password:
        if not ch.isalnum():
            return True
    return False

if check_digit(password) and check_special(password):
    print("Yes it is a strong password ✅")
else:
    print("It is not a strong password ❌ please retry")
