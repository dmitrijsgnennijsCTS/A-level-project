from kivy.app import App # Import the app to run the code and create window

from kivy.uix.button import Button # Import button to use the buttons in code
from kivy.uix.anchorlayout import AnchorLayout # Allows the use of anchor layout

from kivy.config import Config # Import config to configure setting

Config.set('kivy', 'exit_on_escape', '1') # When exit key pressed then close the program
Config.set('graphics', 'fullscreen', 'auto') # Fulscreen is enabled and will be auto. So will be set to display res

from kivy.core.window import Window # Import Window to get window size

class MyApp(App):
	def build(self):
		
		print(str(Window.size[1]), str(Window.size[0])) # Gets the size of the display in pixels
		return Button(text = "button1", size_hint = [.5,.1], pos = (int(Window.size[1]*.125), 0)) # Button that has relative size and position

if __name__ == "__main__": # Check the name, if not a daughter program then run
	MyApp().run() # Run the class
