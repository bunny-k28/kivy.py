# all the imports
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line

# class for the touch function
class Touch(Widget):

    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        # statement for making a canvas on a window
        with self.canvas:

            # code to draw line
            self.line = Line()

            # code for making a colorful rectangle
            Color(1, 0, 0, 0.5, mode='rgba')
            self.rect = Rectangle(pos=(0, 0), size=(50, 50))


    # functions defined for the touch function
    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print('Mouse Down', touch)

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print('Mouse move', touch)


# main class for running the app run
class MyApp(App):
    def build(self):
        return Touch()

# the program runner
if __name__ == '__main__':
    MyApp().run()