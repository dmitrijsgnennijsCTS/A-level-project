from kivy.app import App
from kivy.uix.label import Label


class MainApp(App):
    def build(self):
        return Label()
    
if __name__ == "__main__":
    MainApp().run()


##Button:
##	text: "Cruise Control : OFF"
##	size_hint: [.5, .1]
##	pos_hint: {'x': 0, 'center_y': .05}
##
##Button:
##	text: "Lane Assist : OFF"
##	size_hint: [.5, .1]
##	pos_hint: {'x': .5, 'center_y': .5}
