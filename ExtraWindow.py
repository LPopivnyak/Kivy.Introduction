import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class ExtraWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        mainLine = BoxLayout()
        extraLine = BoxLayout(orientation='vertical')

        BtnLbl1 = Button(text='1')
        extraLine.add_widget(BtnLbl1)
        mainLine.add_widget(extraLine)

        self.add_widget(mainLine)