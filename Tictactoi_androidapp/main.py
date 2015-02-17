from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
class RootWidget(FloatLayout):
	def __init__(self,**kwargs):
		super(RootWidget,self).__init__(**kwargs)


class Mainapp(App):

    def build(self):
    	#icon='mainicon.jpg'
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)
        with root.canvas.before:
            Color(255,255,0,0)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        sizeofbutton_x=.33
        sizeofbutton_y=.3
        b1=Button(background_color=(244,244,0,0.8),text='1',size_hint=(sizeofbutton_x,sizeofbutton_y),pos_hint={'x':0, 'y': .7})
        b2=Button(background_color=(244,244,0,0.8),text='2',size_hint=(sizeofbutton_x,sizeofbutton_y),pos_hint={'x':0, 'y': .4})
        b2=Button(background_color=(244,244,0,0.8),text='2',size_hint=(sizeofbutton_x,sizeofbutton_y),pos_hint={'x':0, 'y': .4})
        b3=Button(background_color=(244,244,0,0.8),text='3',size_hint=(sizeofbutton_x,sizeofbutton_y),pos_hint={'x':0, 'y': .1})
        b4=Button(background_color=(244,244,0,0.8),text='4',size_hint=(sizeofbutton_x,sizeofbutton_y),pos_hint={'x':.33, 'y': .7})
        b5=Button(background_color=(244,244,0,0.8),text='5',size_hint=(sizeofbutton_x,sizeofbutton_y),pos_hint={'x':.33, 'y': .4})
        b6=Button(background_color=(244,244,0,0.8),text='6',size_hint=(sizeofbutton_x,sizeofbutton_y),pos_hint={'x':.33, 'y': .1})
        b7=Button(background_color=(244,244,0,0.8),text='7',size_hint=(sizeofbutton_x,sizeofbutton_y),pos_hint={'x':.66, 'y': .7})
        b8=Button(background_color=(244,244,0,0.8),text='8',size_hint=(sizeofbutton_x,sizeofbutton_y),pos_hint={'x':.66, 'y': .4})
        b9=Button(background_color=(244,244,0,0.8),text='9',size_hint=(sizeofbutton_x,sizeofbutton_y),pos_hint={'x':.66, 'y': .1})
        gamebutton=Button(text="scores",size_hint=(1,.1),pos_hint={'x':0,'y':0})
        root.add_widget(b1)
        root.add_widget(b2)
        root.add_widget(b3)
        root.add_widget(b4)
        root.add_widget(b5)
        root.add_widget(b6)
        root.add_widget(b7)
        root.add_widget(b8)
        root.add_widget(b9)
        root.add_widget(gamebutton)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__=='__main__':
	Mainapp().run()
