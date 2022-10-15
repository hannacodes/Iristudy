from kivy.app import App
from kivy.uix.widget import Widget

class Profile(Widget):
    pass

class ProfileApp(App):
    def build(self): 
        return Profile()

if __name__ == '__main__':
    ProfileApp().run()