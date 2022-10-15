from cgitb import text
from tkinter import CENTER, Grid
from typing import Text
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from kivy.config import Config
from kivy.core.window import Window
Window.size = (480, 853)

class Login(Widget):
    pass

class LoginApp(App):
    def build(self): 
        return Login()
        
if __name__ == '__main__':
    LoginApp().run()