from model.order import getInvoice, updateLedger, updateReceipt
from model.user import User
import view.login
from kivy.uix.screenmanager import Screen, ScreenManager

class Login:
    def Verifying(self, username, password) -> User:
        """Create a username using user's input. If the user exists, return User instance, else return None"""
        user: User = User(username, password)
        if user.verified:
            return user
        return None

    def Login(self, user):
        if user is not None:
            view.login.sm.current = "main"
        else:
            view.login.invalidLogin()

    def logout(accountInstance: User) -> None:
        del accountInstance


class Menu():
    def chooseOptions(self) -> None:
        pass

    def order(self) -> None:
        pass


if __name__ == '__main__':
    screens = [view.login.LoginScreen(name="login"), view.login.MainScreen(name="main")]
    for screen in screens:
        view.login.sm.add_widget(screen)
    view.login.sm.current = "login"
    view.login.MyMainApp().run()
    accountInstance = view.login.LoginScreen.LogBtn(view.login.LoginScreen)
    print('')
    if accountInstance is not None:
        invoice = getInvoice(accountInstance.name, ['item-1', 'item-2', 'item-4'])
        print(invoice)
        updateLedger(invoice)
        updateReceipt(invoice)
    