from model import utils
from model.user import User
from model import order
import tkinter as tk

def login() -> User:
    username = input('Please enter username: ')
    password = input('Please enter password: ')
    user: User = User(username, password = password)
    if user.verified:
        return user
    return None

if __name__ == '__main__':
    account = login()
    if account != None:
        account.name = input('Please enter new name: ')
        account.update()
        print(account.user)
    else:
        print('wrong password')
    
