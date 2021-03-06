import kivy
kivy.require('1.5.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class kivyentrywidget(GridLayout):

    def __init__(self, **kwargs):
        super(kivyentrywidget, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='What do you want to print?'))
        self.text_input = TextInput(multiline=False)
        self.add_widget(self.text_input)
        self.printbutton = Button(text='Print')
        self.printbutton.bind(on_press=self.callback)
        self.add_widget(self.printbutton)

    def callback(self,evt=None):
        return Label(text=self.text_input.text)



class Firstapp(App):
    def build(self):
        return kivyentrywidget()

if __name__ == '__main__':
    Firstapp().run()