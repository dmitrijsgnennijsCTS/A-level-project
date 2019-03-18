# sudo pip(pip3) install matplotlib, numpy, opencv, kivy, pillow # Libraries required!!!

##############################################
##                v 1.0.3                    #
##############################################

from kivy.app import App # Import the app to run the code and create window
from kivy.uix.floatlayout import FloatLayout # Import the ability of putting widgets in any place on the window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition # Import the ability to create multiple screens and anything related
from kivy.lang import Builder # part of kivy that is responsable for linking the kv file with py
from kivy.config import Config # Import config to configure setting
from kivy.graphics.texture import Texture
import numpy as np # import the numpy array in order to manipulate the data from the camera
import cv2 # import the cv2 library which helps with analysing images
from kivy.clock import Clock # import a library that will be responsable for running a update sequence every time period
from sys import exit
from kivy.uix.image import Image


Config.set('kivy', 'exit_on_escape', '1') # When exit key pressed then close the program
Config.set('graphics', 'fullscreen', 'auto') # Fulscreen is enabled and will be auto. So will be set to display res
Config.set("graphics", "show_cursor", '1') # Allow the cursor to be shown on the display when the program is running.


from kivy.core.window import Window # Import Window to get window size

Window.clearcolor = ((.2*.75), (.72*.75) ,(.80*.75) ,1) # Colour of the window

global stopped 
stopped = False


class MainScreen(Screen, FloatLayout, Image):
	def __init__(self, **kwargs):
		super(MainScreen, self).__init__(**kwargs)
		self.capture = cv2.VideoCapture(0) # captures the data from the camera with index 0 (primary)
		if stopped == False:
			Clock.schedule_interval(self.update, 1.0 / 24) # <--- If fps change is required/ Also code used for updating the frame
		else:
			self.capture.release() # release the camera when program stopped. without this the app will not close
			print('Camera released\nQuitting')
			exit(0)

	def update(self, dt):
		ret, frame = self.capture.read() # reads the cv2 output from the camera
		height = int(Window.size[1] * 0.8) # work out the size of the frame that should be displayed relative to the window size
		aspectRatio = frame.shape[0]/frame.shape[1] # work out the aspect ratio of the frames received in order to work out the correct width of frames
		width = int(height / aspectRatio) # work out the correct relative width of the frame
		frame = cv2.resize(frame, (width, height)) # resize the received frames to the correct relative size to the window
		if ret: # if a camera is turned on and iscapturing for the current program then the current statement will be true
			checkFrame = frame.copy() # copy the array of the frame to the variable
			checkFrame.resize((1,1)) # resize the whole array/frame to a size 1*1
			buf1 = cv2.flip(frame, 0) # in order to display frames in kivy, they must be converteed to textures
			# this requires the frame array to be flipped
			buf = buf1.tostring() # the array has to be convrted into a string in order to be displayed in ther main window
			image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') # a texture (a space where graphics can be displayed) 
			# has to be created with the data of the frame, in order to have the frame being the correct size displayed
			image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte') # save the texture created to the buffer in order to use afterwards in the kv file
			# by saving texture in the buffer because the buffer is faster access memory in comparison to secondary memory
			self.texture = image_texture # assign the texture to the main window

			if checkFrame[0][0] >=2: # check if the frame received has a brightness of above the certain threshold 
				self.lbl_d.text = ("")

			else: # if the frame is too dark then display a warning message
				print("The frame received is black!")
				self.lbl_d.text = ("Too dark")
			
		else:
			self.texture = Image('img2.jpg').texture
					#### HAS TO BE UPDATED!!!!

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
	
	def on_stop(self):
		print('Quiting and releasing camera')
		global stopped 
		stopped = True
		MainScreen().run()


if __name__ == "__main__":
	MainApp().run() #run the app if not a daughter program
