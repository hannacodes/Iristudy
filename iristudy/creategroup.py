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
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
Window.size = (480/1.5, 853/1.5)


class CreateFormScreen(Screen):
    # get the username from profile data and then set it to name data
    groupName = ObjectProperty(None)
    subject = ObjectProperty(None)
    description = ObjectProperty(None)

    def popUp(self):
        show_popup()

    def spinner_clicked(self, value):
        self.subject = value;

    def submit(self):
        self.add_widget(Label(text=f'{self.groupName.text}, {self.description.text}'))
        self.groupName.text = ""
        self.description.text = ""


class Pop(FloatLayout):
    pass

def show_popup():
    show = Pop()

    popupWindow = Popup(title="Calendar", content=show, size_hint=(None, None), size=(300, 380))
    
    popupWindow.open()

class CreateApp(App):
    def build(self):
        return CreateFormScreen()

if __name__ == '__main__':
    CreateApp().run()