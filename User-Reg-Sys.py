# ===== User Registration Script =====

# Input from user
name = input("Please enter your name: ")
email = input("Enter your Email: ")
password = input("Please enter your password: ")

# ===== Validation Functions =====

def check_name(name):
    """Check if the name is not empty"""
    if not name.strip():
        raise ValueError("User name could not be empty...")

def check_email(email):
    """Basic email validation: must contain '@' and '.' """
    if "@" not in email or "." not in email:
        raise ValueError("Please input a proper email address...")

def check_password(password):
    """Check if password contains at least one special character"""
    for ch in password:
        if not ch.isalnum():
            return True
    return False

# ===== Error Collection =====
errors = []

# Check Name
try:
    check_name(name)
except ValueError as e:
    errors.append(str(e))

# Check Email
try:
    check_email(email)
except ValueError as e:
    errors.append(str(e))

# Check Password
if not check_password(password):
    errors.append("Password must contain at least one special character")

# ===== Final Output =====
if errors:
    print("\nYou could not login due to these errors:")
    for err in errors:
        print("-", err)
else:
    print("\nYou have been logged in successfully!")




               





