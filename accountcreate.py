from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
Window.size = (480, 853)

class Account(Widget):
    pass

class AccountApp(App):
    def build(self): 
        return Account()

if __name__ == '__main__':
    AccountApp().run()