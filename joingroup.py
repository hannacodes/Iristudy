"""
Join group screen when people click onto a group while searching
group or clicking on recommended groups.
"""

import kivy
from kivy.app import App
from kivy.uix.label import Label # writing
from kivy.uix.gridlayout import GridLayout # table
from kivy.uix.textinput import TextInput # input text
from kivy.uix.button import Button # button component
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.properties import ObjectProperty
from kivy.core.window import Window
Window.size = (480/1.5, 853/1.5)

class JoinGroupScreen(Widget):
    pass

class JoinApp(App):
    def build(self):
        return JoinGroupScreen()

if __name__ == '__main__':
    JoinApp().run()