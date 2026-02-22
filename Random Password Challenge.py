import random

# characters to use
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

# combine all characters
all_chars = lower + upper + numbers

# ask user for password length
length = int(input("Enter password length: "))

# create password list
password = []

# pick random characters
for i in range(length):
    password.append(random.choice(all_chars))

# shuffle the password
random.shuffle(password)

# join list into string
final_password = "".join(password)

print("Generated Password:", final_password)