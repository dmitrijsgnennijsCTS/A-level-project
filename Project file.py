from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<ScreenOne>:
    FloatLayout:
        Button:
            text: "Go to screen 2"
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 1
                root.manager.current = "screen_two"
            size_hint: (.5, .5)

<ScreenTwo>:
    FloatLayout:
        Button:
            text: "Go to screen 1"
            on_press:
                root.manager.transition.direction = "right"
                root.manager.transition.duration = 1
                root.manager.current = "screen_one"
            size_hint: (.5, .5)
""")

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

screen_manager = ScreenManager()

screen_manager.add_widget(ScreenOne(name = "screen_one"))
screen_manager.add_widget(ScreenTwo(name = "screen_two"))

class KivyTut2app(App):

    def build(self):
        return screen_manager

if __name__ == "__main__":
    KivyTut2app().run()
