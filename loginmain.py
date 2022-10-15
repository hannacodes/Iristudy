from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class LoginScreen(Screen):
    kv = Builder.load_file("login.kv")
    def __init__(self, **kwargs):  # defining an init method
        super().__init__(**kwargs)
        print("build initialized")

class AccountScreen(Screen): 
    kv = Builder.load_file("account.kv")
    def __init__(self, **kwargs):  # defining an init method
        super().__init__(**kwargs)

class WindowManager(ScreenManager):  
    pass


sm = WindowManager() 

screens = [LoginScreen(name="login"), AccountScreen(name="account")]  

for screen in screens:  
    print("widget added")
    sm.add_widget(screen) 

sm.current = "login"  

class LoginAppMain(App):
    def build(self): 
        Window.size = (480, 853)
        App.title = "test"
        return sm
        
if __name__ == '__main__':
    LoginAppMain().run()