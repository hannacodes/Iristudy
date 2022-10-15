"""
Create group screen
form like with subject, set a random group id,
ask for group name..
"""

import kivy
from kivy.app import App
from kivy.uix.label import Label # writing
from kivy.uix.gridlayout import GridLayout # table
from kivy.uix.textinput import TextInput # input text
from kivy.uix.button import Button # button component
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown

class CreateFormLayout(Widget):
    pass

class CreateApp(App):
    def build(self):
        return CreateFormLayout()

if __name__ == '__main__':
    CreateApp().run()