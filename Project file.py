from kivy.app import App # Import the app to run the code and create window
from kivy.uix.floatlayout import FloatLayout # Import the ability of putting widgets in any place on the window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition # Import the ability to create multiple screens and anything related
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

from kivy.lang import Builder

from kivy.config import Config # Import config to configure setting
import numpy as np
import cv2
import PIL
from kivy.uix.image import Image
from kivy.clock import Clock

Config.set('kivy', 'exit_on_escape', '1') # When exit key pressed then close the program
Config.set('graphics', 'fullscreen', 'auto') # Fulscreen is enabled and will be auto. So will be set to display res
Config.set("graphics", "show_cursor", '1') # Allow the cursor to be shown on the display when the program is running.


from kivy.core.window import Window # Import Window to get window size

Window.clearcolor = ((.2*.75), (.72*.75) ,(.80*.75) ,1) # Colour of the window
source = ''

class MainScreen(Screen, FloatLayout, Image):
	def __init__(self, **kwargs):
		super(MainScreen, self).__init__(**kwargs)
		self.source = 'img.jpg' #Getting two images
	# def __init__(self, capture, fps, **kwargs): #Error whilst running here
	# 	print("here 2")
	# 	super(MainScreen, self).__init__(**kwargs)
	# 	self.capture = capture
	# 	Clock.schedule_interval(self.update, 1.0 / fps)

	# def update(self, dt):
	# 	ret, frame = self.capture.read()
	# 	#print(frame)
	# 	imag = PIL.Image.fromarray(frame)
	# 	imag.save('out.png')
	# 	self.source = 'img.jpg'

	def Cruise_Control_Button(self):
		if self.btn_c.text == "Cruise Control: Off":
			self.btn_c.text = ("Cruise Control: On")
		else:
			self.btn_c.text = ("Cruise Control: Off")

	def Lane_Assist_Button(self):
		if self.btn_l.text == "Lane Assist : Off":
			self.btn_l.text = ("Lane Assist : On")
		else:
			self.btn_l.text = ("Lane Assist : Off")
	pass

class SettingsScreen(Screen, FloatLayout):
    
    def Speed_Units(self):
        
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


class ScreenManagement(ScreenManager):
	pass

# class MyWidget(Widget):
#     pass

#class CameraCapture(Image):
 #   def __init__(self, capture, fps, **kwargs):
  #  	super(CameraCapture, self).__init__(**kwargs)
   # 	self.capture = capture
    #	Clock.schedule_interval(self.update, 1.0 / fps)

#    def update(self, dt):
 #   	ret, frame = self.capture.read()
  #  	#print(frame)
   # 	imag = PIL.Image.fromarray(frame)
    #	imag.save('out.png')
    #	self.source = 'img.jpg'


gui = Builder.load_file('projectfile.kv')

class MainApp(App):
    def build(self):
    	#self.capture = cv2.VideoCapture(0)
    	return gui

    # def on_stop(self):
    #     self.capture.release()

if __name__ == "__main__":
	MainApp().run()
