
import kivy

from kivy.core.window import Window
Window.size = (480/1.5, 853/1.5)

from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.graphics import *
from kivy.utils import *

class P(FloatLayout):
    def __init__(self, **kwargs):
        super(FloatLayout, self).__init__(**kwargs)
        test = Label(text="button pressed", size_hint=(0.6, 0.2), pos_hint = {"x":0.2, "top":1})
        self.add_widget(test)

class mygroups(Screen): 
    def popUp(self):
        show_popup()

def show_popup(self): 
        show = P()
        popupWindow = Popup(title="Popup Win", content = show, size_hint=(None, None), size=(300, 380))
        popupWindow.open() 

class infoBtn(Button):
    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)

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
            infoButton = infoBtn(text = "more info", size_hint = (0.3, 0.4), pos_hint = {"center_x": .5, "top": 0.9}, font_name = 'assets/fonts/static/Fredoka/Fredoka-regular', background_color = get_color_from_hex('#BF98D1'), background_normal = '')
            infoButton.bind(on_release=show_popup)
            flaylout.add_widget(infoButton)
            SkillStat.add_widget(flaylout)
            layout.add_widget(SkillStat)

        self.add_widget(layout) 


class mygrpApp(App):
    def build(self):
        return mygroups()
    
mygrpApp().run()