# all the imports
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

# main class for running the app run
class MyApp(App):
    def build(self):
        return FloatLayout()

# the program runner
if __name__ == '__main__':
    MyApp().run()