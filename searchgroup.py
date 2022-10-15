"""
Search group screen
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

class SearchGroupScreen(Widget):
    pass

class SearchApp(App):
    def build(self):
        return SearchGroupScreen()

if __name__ == '__main__':
    SearchApp().run()