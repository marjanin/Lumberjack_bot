import numpy as np
from PIL import ImageGrab, Image
import sys, time, pyautogui, random, os

def is_wood(color):
	tolerance = 10
	if (151-tolerance)<color[0]<(151+tolerance)  and (105-tolerance)<color[1]<(105+tolerance) and (49-tolerance)<color[2]<(49+tolerance):
		return True
	else:
		return False

left_image = Image.open('left.png')
right_image = Image.open('right.png')

desired_score = 330
current_score = 0
left_x = 1054
right_x = 1163
y = 673
time.sleep(5)
image = ImageGrab.grab()
while current_score < desired_score:
	#image.show()
	color_left = image.getpixel((left_x, y))
	if is_wood(color_left):
		pyautogui.press('right', 2)
	# color_right = image.getpixel((right_x, y))
	# if is_wood(color_right):
	else:
		pyautogui.press('left', 2)
	current_score += 2
	time.sleep(.025)
	image = ImageGrab.grab()
	
#left_image = ImageGrab.grab()
#I=right_image.load()
# for ii in range(x,x+50):
# 	for jj in range(y,y+50):
# 		I[ii,jj]=(0,0,0,0)
#left_image.show()
#color = right_image.getpixel((right_x, y))
#wood = is_wood(color)
#import pdb; pdb.set_trace()
#import pdb; pdb.set_trace()
