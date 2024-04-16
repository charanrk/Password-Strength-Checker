import re

def password_strength(password):
    if len(password) < 8:
        return ("weak", "Password length should be at least 8 characters.")
    elif not re.search(r"[A-Z]", password):
        return ("okey", "Password should contain at least one uppercase letter.")
    elif not re.search(r"[a-z]", password):
        return ("okey", "Password should contain at least one lowercase letter.")
    elif not re.search(r"\d", password):
        return ("okey", "Password should contain at least one digit.")
    elif not re.search(r"[!@#$%^&*()_+\-=[\]{};:'\"|,.<>?/]", password):
        return ("okey", "Password should contain at least one special character.")

    return ("strong", "Password meets complexity requirements.")

def main():
    password = input("Enter Your Password:")
    strength, message = password_strength(password)
    if strength == "weak":
        print("Weak: ", "The Password Should Contain Minimum Requirements....!!")
    elif strength == "okey":
        print("Okay: ", "Password Is Acceptable But Not Strong....!!")
    elif strength == "strong":
        print("Strong: ", "Great... Your Password Is Strong")
    else:
        print("Unknown Password")

if __name__ == "__main__":
    main()
