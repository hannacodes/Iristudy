
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
Window.size = (480, 853)

class Login(Screen):
    Builder.load_file("login.kv")
    def __init__(self, **kwargs): 
         
        super().__init__(**kwargs)

class LoginApp(App):
    def build(self): 
        return Login()
        
if __name__ == '__main__':
    LoginApp().run()