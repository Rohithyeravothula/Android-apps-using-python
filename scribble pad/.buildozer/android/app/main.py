from kivy.app import App
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.textinput import TextInput
from kivy.config import Config
Config.set('kivy','window_icon','icon.png')
class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)



class MyPaintWidget(Widget):
    def __init__(self, **kwargs):
        super(MyPaintWidget, self).__init__(**kwargs)
        self.Pensilsize=4.5
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1.0,1.0,0)
            touch.ud['line'] = Line(points=(touch.x, touch.y),width=self.Pensilsize)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MainApp(App):
    icon='icon.png'
    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)
        with root.canvas.before:
            Color(0, 1, 0, 1)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        b1=Button(text="Clear",size_hint=(0.3,0.3),pos_hint={'x':0,'y':0})
        b2=Button(text="size+",size_hint=(.3,.3),pos_hint={'x':.3,'y':0})
        b3=Button(text="size-",size_hint=(.3,.3),pos_hint={'x':.6,'y':0})
        paintwidget=MyPaintWidget()
        root.add_widget(paintwidget)
        root.add_widget(b1)
        root.add_widget(b2)
        root.add_widget(b3)
        def clear_canvas(obj):
            paintwidget.canvas.clear()
        def sizeinc(obj):
            paintwidget.Pensilsize=paintwidget.Pensilsize+0.5
        def sizedec(obj):
            if paintwidget.Pensilsize>1:
                paintwidget.Pensilsize=paintwidget.Pensilsize-0.5
        b1.bind(on_release=clear_canvas)
        b2.bind(on_release=sizeinc)
        b3.bind(on_release=sizedec)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    def on_pause(self):
        return True
    def on_resume(self):
        pass

if __name__ == '__main__':
    MainApp().run()