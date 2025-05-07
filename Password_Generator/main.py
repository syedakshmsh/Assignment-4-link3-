import random
import string

def password_Generator(length):
    generate = string.ascii_letters + string.digits + string.punctuation
    pasword = " ".join(random.choice(generate) for _ in range(length))
    return pasword

length = int(input("enter a desired password length: "))

if __name__ == "__main__":
    print(password_Generator(length))
