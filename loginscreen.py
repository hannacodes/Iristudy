from cgitb import text
from tkinter import CENTER, Grid
from typing import Text
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        alayout = AnchorLayout(anchor_x = 'center', anchor_y = 'center')
        
        glayout = GridLayout(cols = 1)
        glayout.add_widget(Label(text='User Name'))
        glayout.username = TextInput(multiline = False)
        glayout.add_widget(glayout.username)
        glayout.add_widget(Label(text='Password'))
        glayout.password = TextInput(password=True, multiline=False)
        glayout.add_widget(glayout.password)
        alayout.add_widget(glayout)
        self.add_widget(alayout)


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()