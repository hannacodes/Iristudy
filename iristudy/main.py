from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import *
from creategroup import show_popup
from kivy.utils import * 
from kivy.graphics import *
import time

import first_db
import mysql.connector

#from mygroups import mygroups



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
    def popUp(self):
        show_popupinfo()

class moreInfoWindow(Popup):
    pass

def show_popupinfo(self): 
        popupWindow = moreInfoWindow()
        popupWindow.open() 

class infoBtn(Button):
    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)

    
class GroupLayout(BoxLayout): 
    def __init__(self, name, subject, admin, **kwargs):
        super().__init__(**kwargs)    
        self.add_widget(Label(text = name, color = (0,0,0,1), size_hint = (None, None), size = (80, 20), pos_hint = {"center_x":.5, "top":0}, font_name = 'assets/fonts/static/Fredoka/Fredoka-regular'))
        self.add_widget(Label(text = subject, color = (0,0,0,1), size_hint = (None, None), size = (80, 20), pos_hint = {"center_x":.5, "top":0}, font_name = 'assets/fonts/static/Fredoka/Fredoka-regular'))
        self.add_widget(Label(text = admin, color = (0,0,0,1), size_hint = (None, None), size = (80, 20), pos_hint = {"center_x":.5, "top":0}, font_name = 'assets/fonts/static/Fredoka/Fredoka-regular'))
        flaylout = FloatLayout(size_hint = (1, 1))
        infoButton = infoBtn(text = "more info", size_hint = (0.3, 0.4), pos_hint = {"center_x": .5, "top": 0.9}, font_name = 'assets/fonts/static/Fredoka/Fredoka-regular', background_color = get_color_from_hex('#BF98D1'), background_normal = '')
        infoButton.bind(on_release=show_popupinfo)
        flaylout.add_widget(infoButton)
        self.add_widget(flaylout)

class Scroll(ScrollView):
    def __init__(self,  **kwargs):
        super(Scroll, self).__init__(**kwargs)
        layout = GridLayout(cols=1, spacing=-1, pos_hint ={'x':0, 'y': 0}, size_hint_y = None, height = "0.8") 

        layout.bind(minimum_height=layout.setter('height'))
        # Make sure the height is such that there is something to scroll.
        my_cursor = first_db.getMyDB().cursor()

        my_cursor.execute("SELECT * FROM users ORDER BY group_ID DESC")

        for x in my_cursor:
            rlayout = RelativeLayout(height=140, size_hint_y=None, size_hint_x=self.width)
            with rlayout.canvas.before: 
                Color(0.9, 0.8, 0.94, 1)
                print( 0.125*Window.size[0], 0.56*Window.size[1], self.width+0.43*(Window.size[0]), 0.21 * (Window.size[1]))
                Rectangle(pos=(self.pos[0] + 0.125*Window.size[0], self.pos[1]+0.056*Window.size[1]), size=(self.width+0.4375*(Window.size[0]), 0.21 * (Window.size[1])))

            group = GroupLayout(x[0], x[1], x[2], spacing = 1, height = 140, orientation = "vertical", size_hint_y = None)
            rlayout.add_widget(group)
            layout.add_widget(rlayout)

        self.add_widget(layout)

    def refresh(self):
        # self.clear_widgets()
        layout = GridLayout(cols=1, spacing=-1, pos_hint ={'x':0, 'y': 0}, size_hint_y = None, height = "0.8") 

        layout.bind(minimum_height=layout.setter('height'))
        # Make sure the height is such that there is something to scroll.
        my_cursor = first_db.getMyDB().cursor()

        my_cursor.execute("SELECT * FROM users ORDER BY group_ID DESC")

        for x in my_cursor:
            rlayout = RelativeLayout(height=140, size_hint_y=None, size_hint_x=self.width)
            with rlayout.canvas.before: 
                Color(0.9, 0.8, 0.94, 1)
                print( 0.125*Window.size[0], 0.56*Window.size[1], self.width+0.43*(Window.size[0]), 0.21 * (Window.size[1]))
                Rectangle(pos=(self.pos[0] + 0.125*Window.size[0], self.pos[1]+0.056*Window.size[1]), size=(self.width+0.4375*(Window.size[0]), 0.21 * (Window.size[1])))

            group = GroupLayout(x[0], x[1], x[2], spacing = 1, height = 140, orientation = "vertical", size_hint_y = None)
            rlayout.add_widget(group)
            layout.add_widget(rlayout)

        self.add_widget(layout)



class Profile(Screen):
    kv = Builder.load_file("profile.kv")
    def __init__(self, **kwargs):  
        super().__init__(**kwargs)

def commitToDB(groupName, subject, description, mydb):
        record = (groupName, subject, description)
        
        my_cursor = mydb.cursor()
        my_cursor.execute(first_db.getSQLInfo(), record);
        
        mydb.commit()
    

#still need to add create group, search group
class CreateFormScreen(Screen):
    kv = Builder.load_file("create.kv")
    # get the username from profile data and then set it to name data
    groupName = ObjectProperty(None)
    subject = ObjectProperty(None)
    description = ObjectProperty(None)

    def popUp(self):
        show_popup()

    def spinner_clicked(self, value):
        self.subject = value

    def submit(self):
        commitToDB(self.groupName.text, self.subject, self.description.text, first_db.getMyDB())
        self.groupName.text = ""
        self.description.text = ""
        self.subject = "Select subject"

class SearchGroupScreen(Screen):
    kv = Builder.load_file("search.kv")
    def __init__(self, **kwargs):  
        super().__init__(**kwargs)


class WindowManager(ScreenManager): 
    val = 0
    def ref(self):
        self.add_widget(Homepage(name="refreshed"+str(self.val)))
        self.current = 'refreshed'+str(self.val)
        self.val+=1 
        
        print("entered ref")
        time.sleep(0.2) 


sm = WindowManager(transition=NoTransition()) 

screens = [Login(name="login"), Account(name="AccountApp"), Homepage(name="home"), Profile(name="profile"), CreateFormScreen(name='create'), SearchGroupScreen(name='search'), mygroups(name="mygroups")]  

for screen in screens:  
    print("widget added")
    sm.add_widget(screen) 

sm.current = "login"  

def ref():
    screens.append(Homepage(name="refreshed"))
    sm.add_widget(Homepage(name="refreshed"))
    print("entered ref")
    time.sleep(0.2)



class LoginAppMain(App):
    def build(self): 
        Window.size = (480/1.5, 853/1.5)
        App.title = "IRISTUDY"
        return sm
        
if __name__ == '__main__':
    LoginAppMain().run()