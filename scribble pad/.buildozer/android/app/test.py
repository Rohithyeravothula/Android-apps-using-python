import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.factory import Factory

class BejotoApp(App):
    icon = 'icon.png'
    title = 'Bejoto Coffe System 0.1 beta'
    def build(self):
        return Factory.Widget()


if __name__ in ('__android__', '__main__'):
    BejotoApp().run()