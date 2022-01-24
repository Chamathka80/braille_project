# import the necessary files & libraries
import cv2
import numpy as np

def preprocess_img():

	# importing the image
	image = cv2.imread('D://Educational Files//RUSL//Group Project//System//final_system//braille_project//assets//test_images//7.jpg')

	# creating dimensions to resize the image
	scale_percent = 20 # percent of original size
	width = int(image.shape[1] * scale_percent / 100)
	height = int(image.shape[0] * scale_percent / 100)
	dim = (width, height)

	# resizing the image to the given scale percentage
	image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

	# converting the image into gray scale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	#   kernal 
	kernel = np.ones((1,1), np.uint8)

	# dialation and erosion
	img_dilation = cv2.dilate(gray, kernel, iterations=1)
	img_erosion = cv2.erode(img_dilation, kernel, iterations=1)

	# thresholding the image
	th, im_th = cv2.threshold(img_erosion, 130, 255, cv2.THRESH_BINARY_INV)

	# Find Canny edges
	edged = cv2.Canny(im_th, 0, 255)

	# Finding Contours
	contours, hierarchy = cv2.findContours(edged,
		cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

	# Draw the contours on the original image
	cv2.drawContours(image, contours, -1, (0, 0, 255), 1)

	cv2.imshow('contoured image', image)
	cv2.imshow('gray', gray)
	cv2.imshow('thresholded image', im_th)
	cv2.imshow('edged', edged)
	print(contours)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


preprocess_img()
