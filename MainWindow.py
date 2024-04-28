import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class MainWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        mainLine = BoxLayout()
        extraLine = BoxLayout(orientation='vertical')

        TxtLbl = Label(text='Вибери екран')
        mainLine.add_widget(TxtLbl)

        BtnLbl1 = Button(text='1', on_press=self.on_second_window)
        BtnLbl2 = Button(text='2')
        BtnLbl3 = Button(text='3')
        BtnLbl4 = Button(text='4')
        extraLine.add_widget(BtnLbl1)
        extraLine.add_widget(BtnLbl2)
        extraLine.add_widget(BtnLbl3)
        extraLine.add_widget(BtnLbl4)
        mainLine.add_widget(extraLine)

        self.add_widget(mainLine)

    def on_second_window(self, *args):
        self.manager.current = "second"