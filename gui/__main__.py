# create a kivy window without title bar
# https://stackoverflow.com/questions/31481041/create-a-kivy-window-without-title-bar


#https://youtu.be/zVMwbarvDu8 -- window without tital bar

from kivy.config import Config
Config.set('graphics', 'fullscreen', 1)
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')
# Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'borderless', 0)
# Config.set('graphics', 'position', 'custom')
# Config.set('graphics', 'left', 0)
# Config.set('graphics', 'top', 0)
Config.set('graphics', 'show_cursor', 1)
# Config.set('graphics', 'multisamples', 0)
# Config.set('graphics', 'minimum_width', 0)
# Config.set('graphics', 'minimum_height', 0)
# Config.set('graphics', 'maximum_width', 0)


from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
class MainApp(MDApp):
    def build(self):
        Window.borderless = True
        # Window.size = (720, 1000)

        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('main.kv')

MainApp().run()