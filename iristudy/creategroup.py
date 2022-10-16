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
from kivy.utils import *
Window.size = (480/1.5, 853/1.5)


class CreateFormScreen(Screen):
    # get the username from profile data and then set it to name data
    groupName = ObjectProperty(None)
    subject = ObjectProperty(None)
    # get the time
    description = ObjectProperty(None)

    def popUp(self):
        show_popup()

    def spinner_clicked(self, value):
        self.subject.text = value

    def submit(self):
        # self.add_widget(Label(text=f'{self.groupName.text}, {self.description.text}'))
        # check if invalid input
        # call a function that will send information to group page?
        self.groupName.text = ""
        self.subject.text = "Select subject"
        self.description.text = ""

class Pop(FloatLayout):
    def __init__(self, **kwargs):
        super(FloatLayout, self).__init__(**kwargs)
        glay = GridLayout(cols=7, size_hint = (0.5, 0.5))
        for __ in range(56): 
            glay.add_widget(Button(text="t", background_color= (0,0,0,0.5)))
        self.add_widget(glay)

class NewBtn(Button):
    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)

    def changebg(a,b): 
        a.background_color = (0,1,0,.4)

def show_popup():
    popupWindow = Popup(title="Potential Meeting Times", size_hint=(None, None), size=(300, 380), title_size="20sp", title_font='assets/fonts/static/Fredoka/Fredoka-medium', background = '', background_color= (0.91, 0.82, 0.94, 1), separator_color=get_color_from_hex("#a46bbe"), title_color=(0,0,0,1))
    glay = GridLayout(cols=8, size_hint = (1, 1), spacing=2)
    arr = ["S", "M", "Tu", "W", "Th", "F", "S"]
    glay.add_widget(Label())
    for i in range(7): 
        glay.add_widget(Label(text=arr[i], font_name='assets/fonts/static/Fredoka/Fredoka-regular', color=(0,0,0,1)))

    arr2 = ["9:00am", "10:00am", "11:00am", "12:00pm", "1:00pm", "2:00pm", "3:00pm"]
    for x in range(7): 
        lbl = Label(text=arr2[x], font_size="10sp", font_name='assets/fonts/static/Fredoka/Fredoka-regular', color=(0,0,0,1))
        glay.add_widget(lbl)
        for x in range(7):
            btn = NewBtn(text="", background_color= get_color_from_hex("#D8B3E9"), background_normal='', size_hint=(1,1))
            btn.bind(on_press = btn.changebg)
            glay.add_widget(btn)
    popupWindow.add_widget(glay)

    popupWindow.open()

class CreateApp(App):
    def build(self):
        return CreateFormScreen()

if __name__ == '__main__':
    CreateApp().run()