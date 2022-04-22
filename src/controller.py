from model.order import getInvoice, updateLedger, updateReceipt
from model.user import User

def login() -> User:
    username = input('Please enter username: ')
    password = input('Please enter password: ')
    user: User = User(username, password = password)
    if user.verified:
        return user
    return None

def chooseOptions() -> None:
    pass

def order() -> None:
    pass

def logout(accountInstance: User) -> None:
    del accountInstance

if __name__ == '__main__':
    accountInstance = login()
    print('')
    if accountInstance != None:
        invoice = getInvoice(accountInstance.name, ['item-1', 'item-2', 'item-4'])
        updateLedger(invoice)
        updateReceipt(invoice)
    