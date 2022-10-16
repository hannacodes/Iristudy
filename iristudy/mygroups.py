
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

import first_db
import mysql.connector

class moreInfoWindow(Popup):
    pass

class mygroups(Screen): 
    def popUp(self):
        show_popup()

def show_popup(self): 
        #popupWindow = Popup(title="Popup Win",  size_hint=(None, None), size=(300, 380))
        #flay = P()
        #popupWindow.add_widget(flay)
        popupWindow = moreInfoWindow()
        popupWindow.open() 

class infoBtn(Button):
    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)


def addLabel(layout, mydb):
    my_cursor = mydb.cursor()

    my_cursor.execute("SELECT * FROM users")

    for x in my_cursor:
        name = x[0]
        subject = x[1]
        admin = x[2]
        
    layout.add_widget(Label(text = name, color = (0,0,0,1), size_hint = (None, None), size = (80, 20), pos_hint = {"center_x":.5, "top":0}, font_name = 'assets/fonts/static/Fredoka/Fredoka-regular'))
    layout.add_widget(Label(text = subject, color = (0,0,0,1), size_hint = (None, None), size = (80, 20), pos_hint = {"center_x":.5, "top":0}, font_name = 'assets/fonts/static/Fredoka/Fredoka-regular'))
    layout.add_widget(Label(text = admin, color = (0,0,0,1), size_hint = (None, None), size = (80, 20), pos_hint = {"center_x":.5, "top":0}, font_name = 'assets/fonts/static/Fredoka/Fredoka-regular'))
    
class Scroll(ScrollView):

    def __init__(self,  **kwargs):
        super(Scroll, self).__init__(**kwargs)
        layout = GridLayout(cols=1, spacing=1, pos_hint ={'x':0, 'y': 0}, size_hint_y = None, height = "0.7")
        layout.bind(minimum_height=layout.setter('height'))
        # Make sure the height is such that there is something to scroll.
        for i in range(15):
            SkillStat = BoxLayout(spacing = 2, height = 150, orientation = "vertical", size_hint_y = None)
            addLabel(SkillStat, first_db.getMyDB())
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