from model import utils
from model.user import User
from model import order


def login() -> User:
    username = input('Please enter username: ')
    password = input('Please enter password: ')
    user: User = User(username, password = password)
    if user.verified:
        return user
    return None

if __name__ == '__main__':
    user = login()
    newOrder = order.getInvoice('test-user', ['item-1', 'item-2'])
    order.updateLedger(newOrder)
    print(order.getMenu())
