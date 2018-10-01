from kivy.app import App # Import the app to run the code and create window

from kivy.uix.button import Button # Import button to use the buttons in code
from kivy.uix.floatlayout import FloatLayout

from kivy.config import Config # Import config to configure setting

Config.set('kivy', 'exit_on_escape', '1') # When exit key pressed then close the program
Config.set('graphics', 'fullscreen', 'auto') # Fulscreen is enabled and will be auto. So will be set to display res
Config.set("graphics", "show_cursor", '1')


from kivy.core.window import Window # Import Window to get window size

Window.clearcolor = ((.2*.75), (.72*.75) ,(.80*.75) ,1) # Colour of the window


class MyApp(App):
	def build(self):
		fl = FloatLayout()

		fl.add_widget( Button(text = "Settings",
		 	size_hint = [(1/3),.1], # Hint for the butttons size
		 	on_press = self.Settings_Button,
		 	background_color = [.5, 0, 0, 1], #Colour of the button in percentage of RGB
			background_normal = '',
		 	pos_hint = {'x': (2/3), 'center_y': .95})) # Relative position of the button in any resolution

		#fl.add_widget(Button (text = 'test', size_hint = (.100, .100), pos_hint = {'x': .5, 'center_y': .5})) #Test button

		fl.add_widget( Button(text = "Cruise Control : OFF",
		 	size_hint = [.5,.1],
		 	on_press = self.Cruise_Control_Button,
		 	background_color = [.5, 0, 0, 1],
			background_normal = '',
		 	pos_hint = {'x': 0, 'center_y': .05}))

		fl.add_widget( Button(text = "Lane Assist : OFF",
			size_hint = [.5,.1],
			on_press = self.Lane_Assist_Button,
			background_color = [.5, 0, 0, 1],
			background_normal = '',
		  	pos_hint = {'x': .5, 'center_y': .05}))

		return fl

	def Settings_Button(self, instance):
		print("Settings pressed")

	def Cruise_Control_Button(self, instance):
		print("Cruise Control pressed")
		if instance.text == "Cruise Control : OFF":
			instance.text = "Cruise Control : ON"
		else:
			instance.text = "Cruise Control : OFF"

	def Lane_Assist_Button(self, instance):
		print("Lane Assist pressed")
		if instance.text == "Lane Assist : OFF": # Check text of button
			instance.text = "Lane Assist : ON" # Change text of a button
		else:
			instance.text = "Lane Assist : OFF"


if __name__ == "__main__": # Check the name, if not a daughter program then run
	MyApp().run() # Run the class


