from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
class Container(BoxLayout):
    def get_text(self):
        texty = ObjectProperty()
        labely = ObjectProperty()
        self.labely.text = str(int(self.texty.text)/2)
        

class myApp(App):
    def build(self):
        return Container()
    
if __name__ == "__main__":
    myApp().run()