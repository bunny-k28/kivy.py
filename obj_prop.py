# all the imports
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

# function for making grids (main grid)
class MyGrid(Widget):

    # declaring the properties
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    # function for setting up a button
    def btn(self):

        # prints the inputs
        print('Name:', self.name.text, '||', 'Email:', self.email.text)

        # code to clear up the input boxes
        self.name.text = ''
        self.email.text = ''

# second button function
def btn(instance):
    print('Run!')

# main class for running the app run
class MyApp(App):
    def build(self):
        return MyGrid()

# the program runner
if __name__ == '__main__':
    MyApp().run()