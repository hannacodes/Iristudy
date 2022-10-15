import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
Window.size = (480/1.5, 853/1.5)

from kivy.app import App 
from kivy.uix.widget import Widget 

class homepage(Screen):
    kv = Builder.load_file("home.kv")
    def __init__(self, **kwargs):  
        super().__init__(**kwargs)

class homeApp(App):
    def build(self):
        return homepage()
    
homeApp().run()