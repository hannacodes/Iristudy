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
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.effects.scroll import ScrollEffect
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import *
from kivy.utils import *
from kivy.core.window import Window
Window.size = (480/1.5, 853/1.5)

class Scroll(ScrollView):
    def __init__(self,  **kwargs):
        super(Scroll, self).__init__(**kwargs)
        layout = GridLayout(cols=1, spacing=1, pos_hint ={'x':0, 'y': 0}, size_hint_y = None, height = "0.7")
        layout.bind(minimum_height=layout.setter('height'))
        # Make sure the height is such that there is something to scroll.
        for i in range(15):
            SkillStat = BoxLayout(spacing = 2, height = 150, orientation = "vertical", size_hint_y = None)
            SkillStat.add_widget(Label(text = "Name", color = (0,0,0,1), size_hint = (None, None), size = (80, 20), pos_hint = {"center_x":.5, "top":0}, font_name = 'assets/fonts/static/Fredoka/Fredoka-regular'))
            SkillStat.add_widget(Label(text = "Subject", color = (0,0,0,1), size_hint = (None, None), size = (80, 20), pos_hint = {"center_x":.5, "top":0}, font_name = 'assets/fonts/static/Fredoka/Fredoka-regular'))
            SkillStat.add_widget(Label(text = "Admin", color = (0,0,0,1), size_hint = (None, None), size = (80, 20), pos_hint = {"center_x":.5, "top":0}, font_name = 'assets/fonts/static/Fredoka/Fredoka-regular'))
            flaylout = FloatLayout(size_hint = (1, 1))
            flaylout.add_widget(Button(text = "more info", size_hint = (0.3, 0.4), pos_hint = {"center_x": .5, "top": 0.9}, font_name = 'assets/fonts/static/Fredoka/Fredoka-regular', background_color = get_color_from_hex('#BF98D1'), background_normal = ''))
            SkillStat.add_widget(flaylout)
            layout.add_widget(SkillStat)

        self.add_widget(layout)       

class SearchGroupScreen(Widget):
    pass

class SearchApp(App):
    def build(self):
        return SearchGroupScreen()

if __name__ == '__main__':
    SearchApp().run()