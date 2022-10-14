"""
Create group screen
form like with subject, set a random group id,
ask for group name..
"""

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Create group")

if __name__ == "__main__":
    MyApp().run()