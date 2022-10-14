"""
Create group screen
form like with subject, set a random group id,
ask for group name..
"""

# import kivy (not an added module)
from kivy.app import App
from kivy.uix.label import Label # writing
from kivy.uix.gridlayout import GridLayout # table
from kivy.uix.testinput import TextInput # input text
from kivy.uix.button import Button # button component

class MyGridLayout(GridLayout):
    # will initialize keywords
    def __init__(self, **kwargs):
        # call the grid layout constructor
        super(myGridLayout, self).__init__(**kwargs)

        # set the columns of the grid
        self.cols = 2

        # Name Widget
        self.add_widget(Label(text="Name: "))
        # add input box
        self.name = TextInput(multiline=True)
        self.add_widget(self.name)

        # copy above to add as many widgets as you want ^
        
        # add the widgets
        self.add_widget(Label(text="Subject: "))
        # add input box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

class MyApp(App):
    def build(self):
        return Label(text="Create group")

if __name__ == "__main__":
    MyApp().run()