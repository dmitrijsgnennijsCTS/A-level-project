# sudo pip(pip3) install matplotlib, numpy, opencv, kivy, pillow # Libraries required!!!

##############################################
##                v 1.1.1                    #
##############################################

from kivy.app import App # Import the app to run the code and create window
from kivy.uix.floatlayout import FloatLayout # Import the ability of putting widgets in any place on the window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition # Import the ability to create multiple screens and anything related
from kivy.lang import Builder # part of kivy that is responsable for linking the kv file with py
from kivy.config import Config # Import config to configure setting
from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
import numpy as np # import the numpy array in order to manipulate the data from the camera
import cv2 # import the cv2 library which helps with analysing images
from kivy.clock import Clock # import a library that will be responsable for running a update sequence every time period
from sys import exit
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image as image_pil
from utils import label_map_util
from utils import visualization_utils as vis_util



Config.set('kivy', 'exit_on_escape', '1') # When exit key pressed then close the program
Config.set('graphics', 'fullscreen', 'auto') # Fulscreen is enabled and will be auto. So will be set to display res
Config.set("graphics", "show_cursor", '1') # Allow the cursor to be shown on the display when the program is running.


from kivy.core.window import Window # Import Window to get window size

Window.clearcolor = ((.2*.75), (.72*.75) ,(.80*.75) ,1) # Colour of the window

global stopped, MODEL_NAME, MODEL_FILE, DOWNLOAD_BASE, PATH_TO_CKPT, PATH_TO_LABELS, NUM_CLASSES, label_map, categories, category_index
stopped = False

global vehicle_close
vehicle_close = False

sys.path.append("..")
MODEL_NAME = 'ssd_mobilenet_v1_coco_11_06_2017'
MODEL_FILE = MODEL_NAME + '.tar.gz'
DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'
PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt')
NUM_CLASSES = 90

detection_graph = tf.Graph()
with detection_graph.as_default():
	od_graph_def = tf.GraphDef()
	with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
		serialized_graph = fid.read()
		od_graph_def.ParseFromString(serialized_graph)
		tf.import_graph_def(od_graph_def, name='')

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

with detection_graph.as_default():
	with tf.Session(graph=detection_graph) as sess:

		class MainScreen(Screen, FloatLayout, Image):
			def __init__(self, **kwargs):
				super(MainScreen, self).__init__(**kwargs)
				self.capture = cv2.VideoCapture(0) # captures the data from the camera with index 0 (primary)
				if stopped == False:
					Clock.schedule_interval(self.update, 1.0 / 60) # <--- If fps change is required/ Also code used for updating the frame
				else:
					self.capture.release() # release the camera when program stopped. without this the app will not close
					print('Camera released\nQuitting')
					exit(0)

			def load_image_into_numpy_array(image):
				(im_width, im_height) = image.size
				return np.array(image.getdata()).reshape(
					(im_height, im_width, 3)).astype(np.uint8)

			def StopSignIdentification(gFrame):
				frame = gFrame
				haar_cascade = cv2.CascadeClassifier("C:/Users/Dmitrijs/Documents/GitHub/A-level-project/stop/classifier/cascade.xml")
				gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				signs = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)
				for (x,y,w,h) in signs:
					cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
				return frame

			def Vehicle_detection(image):
				global vehicle_close
				image_np = image
				image_np_expanded = np.expand_dims(image_np, axis=0)
				image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
				# Each box represents a part of the image where a particular object was detected.
				boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
				# Each score represent how level of confidence for each of the objects.
				# Score is shown on the result image, together with the class label.
				scores = detection_graph.get_tensor_by_name('detection_scores:0')
				classes = detection_graph.get_tensor_by_name('detection_classes:0')
				num_detections = detection_graph.get_tensor_by_name('num_detections:0')
				# Actual detection.
				(boxes, scores, classes, num_detections) = sess.run(
					[boxes, scores, classes, num_detections],
					feed_dict={image_tensor: image_np_expanded})
					# Visualization of the results of a detection.
				vis_util.visualize_boxes_and_labels_on_image_array(
					image_np,
					np.squeeze(boxes),
					np.squeeze(classes).astype(np.int32),
					np.squeeze(scores),
					category_index,
					use_normalized_coordinates=True,
					line_thickness=8)
				for i,b in enumerate(boxes[0]):
				#                 car                    bus                  truck
					if classes[0][i] == 3 or classes[0][i] == 6 or classes[0][i] == 8:
						if scores[0][i] >= 0.5:
							mid_x = (boxes[0][i][1]+boxes[0][i][3])/2
							mid_y = (boxes[0][i][0]+boxes[0][i][2])/2
							apx_distance = float("{0:.2f}".format(boxes[0][i][3] - boxes[0][i][1]))
							cv2.putText(image_np, '{}'.format(apx_distance), (int(mid_x*800),int(mid_y*450)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)

							if apx_distance >=0.5:
								if mid_x > 0.35 and mid_x < 0.65:
									vehicle_close = True
								else:
									vehicle_close = False
				return image_np

			def update(self, dt):
				checkSize = 10 # the size inpixels of width and height of brightness img
				# decrease  ^ to increase performance or increase to improve the accuracy
				ret, frame = self.capture.read() # reads the cv2 output from the camera
				if ret: # if a camera is turned on and iscapturing for the current program then the current statement will be true
					checkFrame = frame.copy()
					frame = MainScreen.Vehicle_detection(frame)
					#frame = MainScreen.StopSignIdentification(frame)
					height = int(Window.size[1] * 0.75) # work out the size of the frame that should be displayed relative to the window size
					aspectRatio = frame.shape[0]/frame.shape[1] # work out the aspect ratio of the frames received in order to work out the correct width of frames
					width = int(height / aspectRatio) # work out the correct relative width of the frame
					frame = cv2.resize(frame, (width, height)) # resize the received frames to the correct relative size to the window
					#checkFrame = frame.copy() # copy the array of the frame to the variable
					calc = 0
					total = 0
					checkFrame = cv2.resize(checkFrame, (checkSize, checkSize)) # resizes the brightness image to increase performance
					buf1 = cv2.flip(frame, 0) # in order to display frames in kivy, they must be converteed to textures
					# this requires the frame array to be flipped
					buf = buf1.tostring() # the array has to be convrted into a string in order to be displayed in ther main window
					image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') # a texture (a space where graphics can be displayed) 
					# has to be created with the data of the frame, in order to have the frame being the correct size displayed
					image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte') # save the texture created to the buffer in order to use afterwards in the kv file
					# by saving texture in the buffer because the buffer is faster access memory in comparison to secondary memory
					self.texture = image_texture # assign the texture to the main window
					for row in range(len(checkFrame)):
						for column in range(len(checkFrame[row])):
							for pixel in range(len(checkFrame[row][column])):
								calc += checkFrame[row][column][pixel]

					global vehicle_close

					if int(calc/((checkSize**2)*3)) >=20 and vehicle_close == False: # check if the frame received has a brightness of above the certain threshold 
						self.lbl_d.text = ("")
						self.lbl_d.background_color = ((.2*.75),(.72*.75),(.8*.75), 1)

					elif vehicle_close == True:
						self.lbl_d.text = ("Warning: vehicle ahead")
						self.lbl_d.background_color = (1, 0, 0 ,1)
						vehicle_close = False

					else: # if the frame is too dark then display a warning message
						self.lbl_d.text = ("Too dark")
						self.lbl_d.background_color = (1, 0, 0 ,1)
					
				else:
					self.texture = CoreImage("C:/Users/Dmitrijs/Documents/GitHub/A-level-project/img2.jpg").texture
					self.lbl_d.text = ("Connection to camera lost!")
					self.lbl_d.background_color = (1, 0, 0 ,1)

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
