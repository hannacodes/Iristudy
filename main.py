from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class WindowManager(ScreenManager):  
    pass

class Homepage(Screen):
    kv = Builder.load_file("home.kv")
    def __init__(self, **kwargs):  
        super().__init__(**kwargs)

class Login(Screen):
    kv = Builder.load_file("login.kv")
    def __init__(self, **kwargs):  
        super().__init__(**kwargs)

class Account(Screen):
    kv = Builder.load_file("account.kv")
    def __init__(self, **kwargs):  
        super().__init__(**kwargs)

class mygroups(Screen):
    kv = Builder.load_file("mygrp.kv")
    def __init__(self, **kwargs):  
        super().__init__(**kwargs)

class Profile(Screen):
    kv = Builder.load_file("profile.kv")
    def __init__(self, **kwargs):  
        super().__init__(**kwargs)
        
#still need to add create group, search group
        


sm = WindowManager() 

screens = [Login(name="login"), Account(name="AccountApp"), Homepage(name="home"), Profile(name="profile")]  

for screen in screens:  
    print("widget added")
    sm.add_widget(screen) 

sm.current = "login"  

class LoginAppMain(App):
    def build(self): 
        Window.size = (480/1.5, 853/1.5)
        App.title = "IRISTUDY"
        return sm
        
if __name__ == '__main__':
    LoginAppMain().run()