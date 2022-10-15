
import kivy

from kivy.core.window import Window
Window.size = (480/1.5, 853/1.5)

from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class scrollingtest(BoxLayout):
    pass
            

class mygroups(Widget): 
    pass 

class mygrpApp(App):
    def build(self):
        return mygroups()
    
mygrpApp().run()