import random   # random module import to generate random numbers

otp = ""        # empty string to store OTP
attempts = 3   # total allowed attempts

# Generate 5-digit OTP
for i in range(5):
    otp += str(random.randint(1, 9))  # add random digit to OTP

print("Your OTP is:", otp)  # display generated OTP (for testing)

# Loop for OTP verification
while attempts > 0:
    inp = input("Enter OTP: ")  # take OTP input from user

    # Check if entered OTP matches generated OTP
    if otp == inp:
        print("Logged in successfully...")
        break  # exit loop if OTP is correct
    else:
        print("Wrong OTP, please re-enter OTP")
        attempts -= 1  # decrease attempts on wrong input
        print(f"{attempts} attempts left...")

# If all attempts are used
if attempts == 0:
    print("Account Blocked...")

