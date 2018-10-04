from kivy.app import App # Import the app to run the code and create window

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.lang import Builder

from kivy.config import Config # Import config to configure setting

Config.set('kivy', 'exit_on_escape', '1') # When exit key pressed then close the program
Config.set('graphics', 'fullscreen', 'auto') # Fulscreen is enabled and will be auto. So will be set to display res
Config.set("graphics", "show_cursor", '1')


from kivy.core.window import Window # Import Window to get window size

Window.clearcolor = ((.2*.75), (.72*.75) ,(.80*.75) ,1) # Colour of the window

class MainScreen(Screen, FloatLayout):

	def Settings_Button(self):
		print("Settings pressed")


	def Cruise_Control_Button(self):
		print("Cruise Control pressed")
		self.lbl.text = "Works"



	def Lane_Assist_Button(self):
		print("Lane Assist pressed")

	pass

class SettingsScreen(Screen):
	pass

class ScreenManagement(ScreenManager):
	pass

gui = Builder.load_file('projectfile.kv')

class MainApp(App):
	def build(self):
		return gui

if __name__ == "__main__":
	MainApp().run()