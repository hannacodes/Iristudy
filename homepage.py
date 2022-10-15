import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 
from kivy.uix.widget import Widget 

class homepage(Widget): 
    pass 

class homeApp(App):
    def build(self):
        return homepage()
    
homeApp().run()