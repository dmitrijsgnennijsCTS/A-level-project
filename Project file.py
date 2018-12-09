# sudo pip(pip3) install matplotlib, numpy, opencv, pillow, kivy # Libraries required!!!

##############################################
##                v 1.0.1                    #
##############################################

from kivy.app import App # Import the app to run the code and create window
from kivy.uix.floatlayout import FloatLayout # Import the ability of putting widgets in any place on the window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition # Import the ability to create multiple screens and anything related
#from kivy.properties import StringProperty #dont seem to do anything
from kivy.lang import Builder # part of kivy that is responsable for linking the kv file with py
from kivy.config import Config # Import config to configure setting
import numpy as np # import the numpy array in order to manipulate the data from the camera
import cv2 # import the cv2 library which helps with analysing images
from kivy.clock import Clock # import a library that will be responsable for running a update sequence every time period


Config.set('kivy', 'exit_on_escape', '1') # When exit key pressed then close the program
Config.set('graphics', 'fullscreen', 'auto') # Fulscreen is enabled and will be auto. So will be set to display res
Config.set("graphics", "show_cursor", '1') # Allow the cursor to be shown on the display when the program is running.


from kivy.core.window import Window # Import Window to get window size

Window.clearcolor = ((.2*.75), (.72*.75) ,(.80*.75) ,1) # Colour of the window

class MainScreen(Screen, FloatLayout):
	def __init__(self, **kwargs):
		super(MainScreen, self).__init__(**kwargs)
		self.capture = cv2.VideoCapture(0) # captures the data from the camera with index 0 (primary)
		Clock.schedule_interval(self.update, 1.0 / 30) # <--- If fps change is required/ Also code used for updating the frame

	def update(self, dt):
		ret, frame = self.capture.read() # reads the cv2 output from the camera
		if ret:
			cv2.imwrite('frame.jpg', frame) # save the image using the cv2 library
			self.ids.img.reload() # Updates the actual image
		else:
			self.ids.img.source = 'img2.jpg' # If the camera is not reachable then an image is displayed which indicates
											 # that the camera is not accessible

	def on_stop(self):
		self.capture.release() # release the camera when program stopped. without this the app will not close

	def Cruise_Control_Button(self): # function of the cruise button
		if self.btn_c.text == "Cruise Control: Off":
			self.btn_c.text = ("Cruise Control: On")
		else:
			self.btn_c.text = ("Cruise Control: Off")

	def Lane_Assist_Button(self): # function of the lane assist button
		if self.btn_l.text == "Lane Assist : Off":
			self.btn_l.text = ("Lane Assist : On")
		else:
			self.btn_l.text = ("Lane Assist : Off")
	pass

class SettingsScreen(Screen, FloatLayout): # a class responsible for the settings screen and all the functions within it
	
	def Speed_Units(self): # function of the speed unit button
		
		if self.speedUnit.text == "Mph":
			 self.speedUnit.text = ("Kph")
		else:
			self.speedUnit.text = ("Mph")
		
	def Pedestrians(self):
		
		if self.pedestrians.text == "Off":
			 self.pedestrians.text = ("On")
		else:
			self.pedestrians.text = ("Off")
		
	def Distance_Units(self):
		
		if self.distanceUnit.text == "Meters":
			 self.distanceUnit.text = ("Yards")
		elif self.distanceUnit.text == "Yards":
			self.distanceUnit.text = ("Feet")
		else:
			self.distanceUnit.text = ("Meters")
		
	def Distance_ToCar(self):
		
		if self.carDistance.text == "Off":
			 self.carDistance.text = ("On")
		else:
			self.carDistance.text = ("Off")
		
	def Car_Speed(self):
		
		if self.carSpeed.text == "Off":
			 self.carSpeed.text = ("On")
		else:
			self.carSpeed.text = ("Off")
		
	pass


class ScreenManagement(ScreenManager): # a class responsible for the management of the screens
	pass


gui = Builder.load_file('projectfile.kv') # a link between the kv ffile and the py file. 

class MainApp(App):
	def build(self):
		return gui #displays the gui form of the program

if __name__ == "__main__":
	MainApp().run() #run the app if not a daughter program
