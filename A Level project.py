from kivy.app import App # Import the app to run the code and create window

from kivy.uix.button import Button # Import button to use the buttons in code

from kivy.config import Config # Import config to configure setting

Config.set('kivy', 'exit_on_escape', '1') # When exit key pressed then close the program
Config.set('graphics', 'fullscreen', 'auto') # Fulscreen is enabled and will be auto. So will be set to display res

class MyApp(App):
	def build(self):
		return Button(text = "button")

if __name__ == "__main__": # Check the name, if not a daughter program then run
	MyApp().run() # Run the class
