
import kivy

from kivy.core.window import Window
Window.size = (480/1.5, 853/1.5)

from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.graphics import *
from kivy.utils import *

class moreInfoWindow(Popup):
    pass

class mygroups(Screen): 
    name = ObjectProperty(None)
    subject = ObjectProperty(None)
    admin = ObjectProperty(None)
    
    def popUp(self):
        show_popupinfo()

def show_popupinfo(self): 
        popupWindow = moreInfoWindow()
        popupWindow.open() 

class infoBtn(Button):
    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)

class GroupLayout(BoxLayout): 
    def __init__(self, name, subject, admin, **kwargs):
        super().__init__(**kwargs)    
        self.add_widget(Label(text = name, color = (0,0,0,1), size_hint = (None, None), size = (80, 20), pos_hint = {"center_x":.5, "top":0}, font_name = 'assets/fonts/static/Fredoka/Fredoka-regular'))
        self.add_widget(Label(text = subject, color = (0,0,0,1), size_hint = (None, None), size = (80, 20), pos_hint = {"center_x":.5, "top":0}, font_name = 'assets/fonts/static/Fredoka/Fredoka-regular'))
        self.add_widget(Label(text = admin, color = (0,0,0,1), size_hint = (None, None), size = (80, 20), pos_hint = {"center_x":.5, "top":0}, font_name = 'assets/fonts/static/Fredoka/Fredoka-regular'))
        flaylout = FloatLayout(size_hint = (1, 1))
        #flaylout.add_widget(Button(text = "more info", size_hint = (0.3, 0.4), pos_hint = {"center_x": .5, "top": 0.9}, font_name = 'assets/fonts/static/Fredoka/Fredoka-regular', background_color = get_color_from_hex('#BF98D1'), background_normal = ''))
        infoButton = infoBtn(text = "more info", size_hint = (0.3, 0.4), pos_hint = {"center_x": .5, "top": 0.9}, font_name = 'assets/fonts/static/Fredoka/Fredoka-regular', background_color = get_color_from_hex('#BF98D1'), background_normal = '')
        infoButton.bind(on_release=show_popupinfo)
        flaylout.add_widget(infoButton)
        self.add_widget(flaylout)

class Scroll(ScrollView):
    def __init__(self,  **kwargs):
        super(Scroll, self).__init__(**kwargs)
        layout = GridLayout(cols=1, spacing=-1, pos_hint ={'x':0, 'y': 0}, size_hint_y = None, height = "0.8") 

        layout.bind(minimum_height=layout.setter('height'))
        # Make sure the height is such that there is something to scroll.
        for i in range(6):
            rlayout = RelativeLayout(height=140, size_hint_y=None, size_hint_x=self.width)
            with rlayout.canvas.before: 
                Color(0.9, 0.8, 0.94, 1)
                print( 0.125*Window.size[0], 0.56*Window.size[1], self.width+0.43*(Window.size[0]), 0.21 * (Window.size[1]))
                Rectangle(pos=(self.pos[0] + 0.125*Window.size[0], self.pos[1]+0.056*Window.size[1]), size=(self.width+0.4375*(Window.size[0]), 0.21 * (Window.size[1])))

            group = GroupLayout("name", "subject", "admin", spacing = 1, height = 140, orientation = "vertical", size_hint_y = None)
            rlayout.add_widget(group)
            layout.add_widget(rlayout)

        self.add_widget(layout)


class mygrpApp(App):
    def build(self):
        return mygroups()
    
mygrpApp().run()