# base Class of your App inherits from the App class.
import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.app import App
# GridLayout arranges children in a matrix.
from kivy.uix.gridlayout import GridLayout
# Label is used to label something
from kivy.uix.label import Label
# used to take input from users
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):
	def __init__(self, **var_args):

                  super(LoginScreen, self).__init__(**var_args)
                  # super function can be used to gain access
                  # to inherited methods from a parent or sibling class
                  # that has been overwritten in a class object.
                  self.cols = 2	 # You can change it accordingly
                  self.add_widget(Label(text='User Name'))
                  self.username = TextInput(multiline=True)

                  # multiline is used to take
                  # multiline input if it is true
                  self.add_widget(self.username)
                  self.add_widget(Label(text='password'))
                  self.password = TextInput(password=True, multiline=False)

                  # password true is used to hide it
                  # by * self.add_widget(self.password)
                  self.add_widget(Label(text='Comfirm password'))
                  self.password = TextInput(password=True, multiline=False)
                  self.add_widget(self.password)


# the Base Class of our Kivy App
class MyApp(App):
	def build(self):
		# return a LoginScreen() as a root widget
	        return LoginScreen()


if __name__ == '__main__':
        MyApp().run()


# create kivy popup
# https://www.youtube.com/watch?v=PpLuyOzCKTQ
# config
# from kivy.config import Config
# Config.set('kivy', 'keyboard_mode', 'systemandmulti')

# from kivy.app import App
# from kivy.uix.popup import Popup
# from kivy.uix.label import Label

# popup = Popup(title='Test popup', content=Label(text='Hello world'),
#               auto_dismiss=False)
# popup.open()


kivy.require('1.0.5')


class Controller(FloatLayout):
    '''Create a controller that receives a custom widget from the kv lang file.

    Add an action to be called from the kv lang file.
    '''
    label_wid = ObjectProperty()
    info = StringProperty()

    def do_action(self):
        self.label_wid.text = 'My label after button press'
        self.info = 'New info text'


class ControllerApp(App):

    def build(self):
        return Controller(info='Hello world')


if __name__ == '__main__':
    ControllerApp().run()
