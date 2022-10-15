from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
Window.size = (480, 853)

class Profile(Widget):
    pass

class ProfileApp(App):
    def build(self): 
        return Profile()

if __name__ == '__main__':
    ProfileApp().run()