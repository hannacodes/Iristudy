"""
Create group screen
form like with subject, set a random group id,
ask for group name..
"""

# import kivy (not an added module)
from kivy.app import App
from kivy.uix.label import Label # writing
from kivy.uix.gridlayout import GridLayout # table
from kivy.uix.textinput import TextInput # input text
from kivy.uix.button import Button # button component

class MyGridLayout(GridLayout):
    # will initialize keywords
    def __init__(self, **kwargs):
        # call the grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # set the columns of the grid
        self.cols = 2

        # Name Widget
        self.add_widget(Label(text="Name: "))
        # add input box
        self.name = TextInput(multiline=True)
        self.add_widget(self.name)

        # copy above to add as many widgets as you want 

        # add Subject widget
        self.add_widget(Label(text="Subject: "))
        # add input box
        self.subject = TextInput(multiline=False)
        self.add_widget(self.subject)


        self.submit = Button(text="Submit", font_size=32)
        self.submit.bind(on_press=self.press) # could be any function
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        subject = self.subject.text
        # for more widgets

        # error check if they didn't submit something for all widgets
        self.add_widget(Label(text=f'Name: {name}, your subject is {subject}'))

        # clear input boxes after submitting
        name = self.name.text = ""
        subject = self.subject.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()