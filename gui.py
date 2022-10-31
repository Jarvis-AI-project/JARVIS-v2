from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivy.lang import Builder


Builder.load_string("""
<Main>:
    BoxLayout:
        orientation: "vertical"

        Button:
            text: 'Click'
            on_press: root.callit()

        Label:
            id: age_lab
            size_hint_y: 0.1
            text: root.str_age

<OpenDialog>:
    title: 'InputDialog'
    size_hint: None, None
    size: 400, 120
    auto_dismiss: False
    text: input.text
    lb_error: er

    BoxLayout:
        orientation: 'vertical'
        pos: self.pos
        size: root.size

        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'Enter Value'

            TextInput:
                id: input
                multiline: False
                hint_text:'Age'
                input_filter: 'int'
                on_text: root.error = ''

        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: 'Enter'
                background_color: 255,0,0,0.9
                on_press: root._enter()

            Button:
                text: 'Cancel'
                background_color: 0,1,255,0.7
                on_press: root._cancel()

        Label:
            id: er
            foreground_color: 1, 250, 100, 1
            color: 1, 0.67, 0, 1
            size_hint_y: None
            height: 0
            text: root.error


""")


class Main(BoxLayout):
    age = NumericProperty()
    str_age = StringProperty("None")

    def callit(self):
        obj = OpenDialog(self)
        obj.open()

    def on_age(self, *args):
        self.str_age = "Age: {}".format(self.age)


class OpenDialog(Popup):

    _age = NumericProperty()
    error = StringProperty()

    def __init__(self, parent, *args):
        super(OpenDialog, self).__init__(*args)
        self.parent = parent
        self.bind(_age=self.parent.setter('age'))

    def on_error(self, inst, text):
        if text:
            self.lb_error.size_hint_y = 1
            self.size = (400, 150)
        else:
            self.lb_error.size_hint_y = None
            self.lb_error.height = 0
            self.size = (400, 120)

    def _enter(self):
        if not self.text:
            self.error = "Error: enter age"
        else:
            self._age = int(self.text)
            self.dismiss()

    def _cancel(self):
        self.dismiss()


class SriPop(App):
    def build(self):
        return Main()


if __name__ == '__main__':
    SriPop().run()
