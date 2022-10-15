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
from kivy.properties import ObjectProperty
from kivy.core.window import Window
Window.size = (480/1.5, 853/1.5)

class CreateFormLayout(Widget):
    name = ObjectProperty(None)
    groupName = ObjectProperty(None)
    subject = ObjectProperty(None)
    description = ObjectProperty(None)

    def submit(self):
        self.add_widget(Label(text=f'{self.name.text}, {self.groupName.text}, {self.description.text}'))
        self.name.text = ""
        self.groupName.text = ""
        self.description.text = ""

    pass

class CreateApp(App):
    def build(self):
        return CreateFormLayout()

if __name__ == '__main__':
    CreateApp().run()