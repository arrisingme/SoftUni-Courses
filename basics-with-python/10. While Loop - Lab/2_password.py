username = input()
password = input()

new_password = 0

while new_password != password:
    new_password = input()

print(f"Welcome {username}!")