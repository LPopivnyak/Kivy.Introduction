import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from MainWindow import MainWindow


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWindow())

        return sm

MyApp().run()