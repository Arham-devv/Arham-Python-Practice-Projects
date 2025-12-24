#This code will analyze a password and tell you weather it's a strong pass or not ...
#Taking Password from user..
Password=input("Enter Password : ")
print("Your password is : ",Password)
print("length of your password is : ",len(Password))
#Made function to check weather the input has special chaacters or not...
def has_special_ch(Password):
    for ch in Password:
        if not ch.isalnum():
            return True
    return False

special_ch=has_special_ch(Password)
#now with conditional statments we will analyze the password and give result ...!
if len(Password)<=6:
    print("You Entered a weak password...!")
elif Password.isdigit():
    print("Medium password..Includes just numbers..!")
elif Password.isalnum():
    print("Much better But you should include special characters...!")
elif special_ch and len(Password)>6:
    print("Perfect Password...!")
else:
    print("Re Run the program and enter a strong password ...!")



