
import kivy

from kivy.core.window import Window
Window.size = (480/1.5, 853/1.5)

from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen
from kivy.graphics import *

class MyRelativeLayout(RelativeLayout):
    def adjust_size(self, *args):
        self.rect.size = self.size  # set the size of the Rectangle




class Scroll(ScrollView):
    def __init__(self,  **kwargs):
        super(Scroll, self).__init__(**kwargs)
        layout = GridLayout(cols=1, spacing=1, pos_hint ={'x':0, 'y': 0}, size_hint_y = None, height = "0.7")
        layout.bind(minimum_height=layout.setter('height'))
        # Make sure the height is such that there is something to scroll.
        for i in range(15):
            #SkillStats = BoxLayout(size_hint_y = None, orientation = "vertical")
            SkillStat = BoxLayout(spacing = 2, height = 150, orientation = "vertical", size_hint_y = None)
            SkillStat.add_widget(Label(text = "Name\nSubject\nAdmin", color = (0,0,0,1), size_hint = (None, None), size = (80, 50), pos_hint = {"center_x":.5, "top":0}))
            flaylout = FloatLayout(size_hint = (1, 1))
            flaylout.add_widget(Button(text = "more info", size_hint = (0.3, 0.4), pos_hint = {"center_x": .5, "top": 0.9}))
            SkillStat.add_widget(flaylout)
            layout.add_widget(SkillStat)

        self.add_widget(layout)

class scrollingtest(BoxLayout):
    pass
            

class mygroups(Screen): 
    pass 

class mygrpApp(App):
    def build(self):
        return mygroups()
    
mygrpApp().run()