from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config # Import config to configure setting

Config.set('graphics', 'fullscreen', 'auto') # Fulscreen is enabled and will be auto. So will be set to display res

class MainApp(App):
	def build(self):
		return Label(text = "Full Screen")


if __name__ == "__main__":
	MainApp().run()