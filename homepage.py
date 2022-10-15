import kivy

from kivy.core.window import Window
Window.size = (480/1.5, 853/1.5)

from kivy.app import App 
from kivy.uix.widget import Widget 

class homepage(Widget): 
    pass 

class homeApp(App):
    def build(self):
        return homepage()
    
homeApp().run()