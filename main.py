# all the imports
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# function for making grids (main grid)
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        # code for widget adding in a window (sub grid)

        self.inside.add_widget(Label(text='First Name: ', font_size=40))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text='Last Name: ', font_size=40))
        self.LastName = TextInput(multiline=False)
        self.inside.add_widget(self.LastName)

        self.inside.add_widget(Label(text='Email: ', font_size=40))
        self.Email = TextInput(multiline=False)
        self.inside.add_widget(self.Email)

        self.inside.add_widget(Label(text='Password: ', font_size=40))
        self.Password = TextInput(multiline=False)
        self.inside.add_widget(self.Password)

        self.add_widget(self.inside)

        # code for button adding in a window
        self.submit = Button(text='Submit', font_size=100)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    # function to save all the inputs
    def pressed(self, instance):
        '''print('Submitted')'''
        name = self.name.text
        last = self.LastName.text
        email = self.Email.text
        password = self.Password.text

        # this will print your input details
        print('Name:', name, '||', 'Last Name:', last, '||', 'Email:', email)

        # code to clear the input box after submitting
        self.name.text = ''
        self.LastName.text = ''
        self.Email.text = ''
        self.Password.text = ''

# main class for running the app run
class MyApp(App):
    def build(self):
        return MyGrid()

# the program runner
if __name__ == '__main__':
    MyApp().run()