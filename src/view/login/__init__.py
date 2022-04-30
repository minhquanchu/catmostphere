from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
import src.controller


class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def reset(self):
        self.username.text = ""
        self.password.text = ""


    def LogBtn(self):
        user = src.controller.Login.Verifying(src.controller.Login, self.username.text, self.password.text)
        src.controller.Login.Login(src.controller.Login, user)
        LoginScreen.reset(self)
        return user

class MainScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password.'),
                size_hint=(None, None), size=(300, 200))
    pop.open()


kv = Builder.load_string('''
<LoginScreen>
    name: "first"

    username: username
    password: password

    FloatLayout:

        Label:
            text: "Username: "
            font_size: (root.width **2 + root.height**2)/ 13**4
            pos_hint: {"x": 0.1, "top": 0.75}
            size_hint: 0.3, 0.15

        TextInput:
            id: username
            font_size: (root.width **2 + root.height**2)/ 13**4
            multiline: False
            pos_hint: {"x": 0.45, "top": 0.75}
            size_hint: 0.4, 0.15

        Label:
            text: "Password: "
            font_size: (root.width **2 + root.height**2)/ 13**4
            pos_hint: {"x": 0.1, "top": 0.5}
            size_hint: 0.3, 0.15

        TextInput:
            id: password
            font_size: (root.width **2 + root.height**2)/ 13**4
            multiline: False
            password: True
            pos_hint: {"x": 0.45, "top": 0.5}
            size_hint: 0.4, 0.15

        Button:
            pos_hint:{"x":0.4, "y":0.2}
            size_hint:0.3, 0.05
            font_size: (root.width **2 + root.height**2)/ 13**4
            text:"Login"
            on_release:
                root.LogBtn()

<MainScreen>
    name: "main"

    GridLayout:
        cols : 1
        Label:
            text: "haha"
''')
sm = WindowManager()

screens = [LoginScreen(name="first"), MainScreen(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "first"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
