password = 'qwerty'

while True:
    username = input("Enter the username: ")
    input_password = input("Enter the password: ")

    if input_password == password:
        print(f"Password for user: {username} is correct")
        break
    else:
        print(f"Password for user: {username} is incorrect")
        print("Please try again...")
