from sign_in import username
from sign_in import passcode
username_login = input("Enter username:")
passcode_login = input("Enter passcode:")
if username_login == username and passcode_login == passcode:
    print("Welcome back")
else:
    print("Wrong username or passcode")