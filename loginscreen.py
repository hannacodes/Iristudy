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

class LoginScreen(Widget):
    pass

class LoginScreenApp(GridLayout):
    def build(self): 
        return LoginScreen()
    '''def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        a = FloatLayout()
        
        a.glayout = GridLayout(cols = 1, size_hint=(.3, .2),
                pos_hint={'x':.35, 'y':.4})
        a.glayout.username = TextInput(text = 'Username', multiline = False)
        a.glayout.add_widget(a.glayout.username)
        a.glayout.password = TextInput(text = 'Password', password=True, multiline=False)
        a.glayout.add_widget(a.glayout.password)
        a.add_widget(a.glayout)
        self.add_widget(a)'''
        




if __name__ == '__main__':
    LoginScreenApp().run()