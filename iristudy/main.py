from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
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
class CreateFormScreen(Screen):
    kv = Builder.load_file("create.kv")
    # get the username from profile data and then set it to name data
    groupName = ObjectProperty(None)
    subject = ObjectProperty(None)
    description = ObjectProperty(None)

    def submit(self):
        self.add_widget(Label(text=f'{self.groupName.text}, {self.description.text}'))
        self.groupName.text = ""
        self.description.text = ""

class SearchGroupScreen(Screen):
    kv = Builder.load_file("search.kv")
    def __init__(self, **kwargs):  
        super().__init__(**kwargs)

sm = WindowManager() 

screens = [Login(name="login"), Account(name="AccountApp"), Homepage(name="home"), Profile(name="profile"), CreateFormScreen(name='create'), SearchGroupScreen(name='search')]  

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