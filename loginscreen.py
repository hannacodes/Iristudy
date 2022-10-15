
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.core.window import Window
Window.size = (480, 853)

class Login(Widget):
    pass

class LoginApp(App):
    def build(self): 
        return Login()
        
if __name__ == '__main__':
    LoginApp().run()