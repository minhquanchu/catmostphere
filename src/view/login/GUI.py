from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from model.order import getInvoice, getMenu, updateLedger, updateReceipt
from model.user import User


class app(App):
    def build(self):
        Window.clearcolor = (237 / 255, 230 / 255, 219 / 255, 1)
        mane_chan = ScreenManager()
        mane_chan.add_widget(LoginScreen(name="login"))
        mane_chan.add_widget(MenuScreen(name="main"))
        mane_chan.add_widget(InvoiceScreen(name="invoice"))
        return mane_chan


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self._user = None
        float_layout = FloatLayout()
        float_layout.add_widget(
            Label(
                text="Username: ",
                color=(26 / 255, 60 / 255, 64 / 255, 1),
                font_size=35,
                pos_hint={
                    "x": 0.1,
                    "top": 0.75
                },
                font_name ='comic',
                size_hint=(0.3, 0.15)
            )
        )
        float_layout.add_widget(
            Label(
                text="WELCOME",
                color=(26 / 255, 60 / 255, 64 / 255, 1),
                font_size=50,
                pos_hint={
                    "x": 0.35,
                    "top": 0.95
                },
                font_name='comic',
                size_hint=(0.3, 0.15)
            )
        )
        self._username = TextInput(
            multiline=False,
            font_size=35,
            padding_y=26,
            pos_hint={
                "x": 0.45,
                "top": 0.75
            },
            font_name='comic',
            size_hint=(0.4, 0.15)
        )
        float_layout.add_widget(self._username)
        float_layout.add_widget(
            Label(
                text="Password: ",
                font_size=35,
                color=(26 / 255, 60 / 255, 64 / 255, 1),
                pos_hint={
                    "x": 0.1,
                    "top": 0.5
                },
                font_name='comic',
                size_hint=(0.3, 0.15)
            )
        )
        self._password = TextInput(
            multiline=False,
            password=True,
            font_size=35,
            padding_y=26,
            pos_hint={
                "x": 0.45,
                "top": 0.5
            },
            size_hint=(0.4, 0.15)
        )
        float_layout.add_widget(self._password)
        float_layout.add_widget(
            Button(
                pos_hint={
                    "x": 0.4,
                    "y": 0.2
                },
                size_hint=(0.3, 0.05),
                text="Login",
                on_release=self.LogBtn,
                font_name='comic',
                background_color=(121 / 255, 218 / 255, 232 / 255, 0.8)
            )
        )
        self.add_widget(float_layout)

    def LogBtn(self, *args):
        self._user = login(self._username.text, self._password.text)
        if login(self._username.text, self._password.text) is not None:
            self.manager.current = 'main'
        else:
            Popup(
                title="Invalid Login",
                content=Label(text="Invalid username or password."),
                size_hint=(None, None),
                size=(300, 200)
            ).open()
        self._username.text = ""
        self._password.text = ""


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self._selectedItems = list()
        self._pressCount = dict()

    def pressBack(self, instance: Button):
        logout(self.manager.get_screen('login')._user)
        self.manager.current = 'login'

    def pressProceed(self, instance: Button):
        self._receipt = getInvoice(self._user['name'], self._selectedItems, "")
        self._selectedItems.clear()
        self.manager.current = 'invoice'

    def clear(self, instance: Button) -> None:
        self._selectedItems.clear()
        for count in self._pressCount.keys():
            count = 0
        for child in self.children:
            for child1 in child.children:
                if isinstance(child1, GridLayout):
                    for button in child1.children:
                        if button.text.find(' |') != -1:
                            button.text = button.text[0:button.text.find(' |')]

    def selecItem(self, instance: Button) -> None:
        selectedItem = instance.text.split(':')[0]
        self._selectedItems.append(selectedItem)
        print(self._selectedItems)

    def on_pre_enter(self, *args):
        user = self.manager.get_screen('login')._user
        print(type(user))
        self._user = user.user
        menu = getMenu()

        boxContainer = BoxLayout(orientation="vertical", padding=(10, 10, 10, 10))

        topContainer = BoxLayout(orientation="horizontal", size_hint=(1, .1), padding=(5, 5, 5, 5))
        menuContainer = GridLayout(size_hint=(1, .9), cols=2)
        boxContainer.add_widget(topContainer)
        boxContainer.add_widget(menuContainer)

        backButton = Button(text="Log Out", size_hint=(.2, 1),background_color=(121 / 255, 218 / 255, 232 / 255, 0.8), font_name ='comic')
        backButton.bind(on_release=self.pressBack)
        cashierLabel = Label(text=self._user['name'], size_hint=(.6, 1), color=(26 / 255, 60 / 255, 64 / 255, 1), font_name ='comic')
        proceedButton = Button(text="Proceed", size_hint=(0.2, 1),background_color=(121 / 255, 218 / 255, 232 / 255, 0.8),font_name ='comic')
        proceedButton.bind(on_release=self.pressProceed)
        topContainer.add_widget(backButton)
        topContainer.add_widget(cashierLabel)
        topContainer.add_widget(proceedButton)

        name: str
        price: int
        for name, price in menu.items():
            itemButton = Button(text=f"{name}: ${price['price']}", background_color=(121 / 255, 218 / 255, 232 / 255, 0.8),font_name ='comic')
            menuContainer.add_widget(itemButton)
            itemButton.bind(on_press=self.selecItem)

        botRow = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        botRow.add_widget(Label(size_hint=(0.3, 1)))
        botRow.add_widget(
            Button(
                text='Clear',
                size_hint=(0.4, 1),
                on_release=self.clear,
                background_color=(121 / 255, 218 / 255, 232 / 255, 0.8),
                font_name='comic'
            )
        )
        botRow.add_widget(Label(size_hint=(0.3, 1)))
        boxContainer.add_widget(botRow)

        self.add_widget(boxContainer)


class InvoiceScreen(Screen):
    def on_pre_enter(self, *args):
        self._receipt = self.manager.get_screen('main')._receipt.copy()
        self.manager.get_screen('main')._receipt.clear()

        try:
            self.remove_widget(self.window)
        except:
            pass
        self.window = BoxLayout(orientation='vertical')
        top = BoxLayout(orientation='vertical')
        top.add_widget(
            Label(
                text=f"User: {self._receipt['cashier']}",
                color=(26 / 255, 60 / 255, 64 / 255, 1),
                font_size=35,
                font_name='comic'
            )
        )
        top.add_widget(
            Label(
                text="______________________________________________",
                font_size=35,
                color=(26 / 255, 60 / 255, 64 / 255, 1),
                outline_color=(121 / 255, 218 / 255, 232 / 255, 0.8),
                outline_width=3
            )
        )
        top_row = BoxLayout(orientation='horizontal')
        top_row.add_widget(
            Label(
                text="Item",
                color=(26 / 255, 60 / 255, 64 / 255, 1),
                font_name='comic',
                font_size=35
            )
        )
        top_row.add_widget(
            Label(
                text=" | ",
                color=(26 / 255, 60 / 255, 64 / 255, 1),
                font_name='comic',
                font_size=35
            )
        )
        top_row.add_widget(
            Label(
                text="Quantity",
                color=(26 / 255, 60 / 255, 64 / 255, 1),
                font_name='comic',
                font_size=35
            )
        )
        top_row.add_widget(
            Label(
                text="Price",
                color=(26 / 255, 60 / 255, 64 / 255, 1),
                font_name='comic',
                font_size=35
            )
        )
        top.add_widget(top_row)
        self.window.add_widget(top)

        scroll = ScrollView(do_scroll_y= True)
        box = BoxLayout(orientation='vertical')
        for item in self._receipt['items'].items():
            card = BoxLayout(orientation='horizontal')
            card.add_widget(
                Label(
                    text=item[0],
                    color=(26 / 255, 60 / 255, 64 / 255, 1),
                    font_name='comic',
                    font_size=25
                )
            )
            card.add_widget(
                Label(
                    text=" | ",
                    color=(26 / 255, 60 / 255, 64 / 255, 1),
                    font_name='comic',
                    font_size=25
                )
            )
            card.add_widget(
                Label(
                    text=str(item[1]['quantity']),
                    color=(26 / 255, 60 / 255, 64 / 255, 1),
                    font_name='comic',
                    font_size=25
                )
            )
            card.add_widget(
                Label(
                    text=str(item[1]['price']),
                    color=(26 / 255, 60 / 255, 64 / 255, 1),
                    font_name='comic',
                    font_size=25
                )
            )
            box.add_widget(card)
        bot_row = BoxLayout(orientation='horizontal')
        box.add_widget(Label(text=" "))
        bot_row.add_widget(
            Label(
                text=" "
            )
        )
        bot_row.add_widget(
            Label(
                text="Total",
                color=(26 / 255, 60 / 255, 64 / 255, 1),
                font_name='comic',
                font_size=25
            )
        )
        bot_row.add_widget(
            Label(
                text=" | "
            )
        )
        bot_row.add_widget(
            Label(
                text=str(self._receipt['total']),
                color=(26 / 255, 60 / 255, 64 / 255, 1),
                font_name='comic',
                font_size=25
            )
        )
        box.add_widget(bot_row)
        box.add_widget(Label(text=" "))
        scroll.add_widget(box)
        self.window.add_widget(scroll)

        buttons = BoxLayout(orientation='horizontal')
        buttons.add_widget(
            Button(
                text="Complete!",
                background_color=(121 / 255, 218 / 255, 232 / 255, 0.8),
                font_name='comic',
                on_release=self.forward
            )
        )
        buttons.add_widget(
            Button(
                text="Go Back",
                background_color=(121 / 255, 218 / 255, 232 / 255, 0.8),
                font_name='comic',
                on_release=self.back
            )
        )
        self.window.add_widget(buttons)

        self.add_widget(self.window)

    def __init__(self, **kwargs):
        super(InvoiceScreen, self).__init__(**kwargs)

    def back(self, *args):
        self._receipt.clear()
        self.manager.current = 'main'

    def forward(self, *args):
        updateReceipt(self._receipt)
        updateLedger(self._receipt)
        Popup(
            title="Completed",
            content=Label(text="Payment Successful"),
            size_hint=(0.5, 0.5)
        ).open()
        self.manager.current = 'main'
        self._receipt.clear()


def start_GUI():
    app().run()


def login(username: str, password: str) -> User:
    """Create an username using user's input. If the user exists, return User instance, else return None"""
    user: User = User(username, password=password)
    if user.verified:
        return user
    return None


def logout(accountInstance: User) -> None:
    del accountInstance
