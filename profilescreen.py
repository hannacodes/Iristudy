from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
Window.size = (480/1.5, 853/1.5)

class Profile(Screen):
    Builder.load_file("profile.kv")
    def __init__(self, **kwargs):  
        super().__init__(**kwargs)


class ProfileApp(App):
    def build(self): 
        return Profile()

if __name__ == '__main__':
    ProfileApp().run()