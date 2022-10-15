from turtle import Screen
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
Window.size = (480/1.5, 853/1.5)

class Account(Screen):
    kv = Builder.load_file("account.kv")
    def __init__(self, **kwargs):  
        super().__init__(**kwargs)

class AccountApp(App):
    def build(self): 
        App.title = "AccountApp"
        return Account()

if __name__ == '__main__':
    AccountApp().run()