from model import utils
from model.user import User
from model import order


def getDBPath(dir: str) -> str:
    return f'../data/{dir}'

def login() -> User:
    username = input('Please enter username: ')
    password = input('Please enter password: ')
    user: User = User(username, password = password, dir = getDBPath('users'))
    if user.verified:
        return user
    return None

if __name__ == '__main__':
    if login() != None:
        print('')
        invoice = order.getInvoice(getDBPath('order'), 'test-user', ['item-1','item-2','item-2','item-3'], 'this is a note')
        order.updateLedger(getDBPath('order'), invoice)
        
    