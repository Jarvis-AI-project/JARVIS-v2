from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

kv='''
    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height

        Label:
            markup: True
            font_size: 32
            text:"This is [color=#][b]Bold[/b] [font=times]Text[/font]"

        Label:
            markup: True
            font_size: 32
            text:"This is [size=150][i]Italics[/i][/size] Text"

        Button:
            markup: True
            font_size: 32
            text: "[u]Click[/u] Me"'''
class AwesomeApp(App):
	def build(self):
		return Builder.load_string(kv)

if __name__ == '__main__':
	AwesomeApp().run()
 
 