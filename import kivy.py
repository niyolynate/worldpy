import kivy
from kivy.ap import APP
from kivy.uix.gridlayout import gridlayout
from kivy.uix.textinput import textinput
from kivy.uix.button import Button
class childApp(GridLayout):
    def __init__self,**kwargs):
        super(childApp, self). __init__()

       self.add_widget(label(text_='Student Name'))
        self.s_name = TextInput_()
        self.add_widget_(self.s_name)

        self.add_widget(label(text_='Students Marks'))
        self.s_name = TextInput_()
        self.add_widget_(self.s_marks)

        self.add_widget(label(text_='Student Gender'))
        self.s_name = TextInput_()
        self.add_widget_(self.s_gender)

class parentApp(App):
    def build(self):
        return childApp()

        if__name__ == "__main_"

        )