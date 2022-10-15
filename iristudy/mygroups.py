
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
from kivy.uix.scrollview import ScrollView
from kivy.graphics import *

class MyRelativeLayout(RelativeLayout):
    def adjust_size(self, *args):
        self.rect.size = self.size  # set the size of the Rectangle

class Scroll(ScrollView):
    def __init__(self,  **kwargs):
        super(Scroll, self).__init__(**kwargs)
        layout = GridLayout(cols=1, spacing=20, pos_hint ={'x':0, 'y': 0.5},
        size_hint_y = None)
        layout.bind(minimum_height=layout.setter('height'))
        # Make sure the height is such that there is something to scroll.
        for i in range(15):
            SkillStat = BoxLayout(height = 80, size_hint_y = None, orientation = "vertical")
            SkillStat.add_widget(Label(text = "Name\nSubject\nAdmin\n", size_hint_y = None, pos_hint = {"x": -0.3, "top":0}))
            SkillStat.add_widget(Button(text = "more info", size_hint = (.4, .3), pos_hint = {"center_x": .7, }))
            layout.add_widget(SkillStat)
        self.add_widget(layout)

class scrollingtest(BoxLayout):
    pass
            

class mygroups(Widget): 
    pass 

class mygrpApp(App):
    def build(self):
        return mygroups()
    
mygrpApp().run()