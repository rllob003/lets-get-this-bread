import numpy as np
import imutils
import cv2

class SingleMotionDetector:
	def __init__(self, accumWeight=0.5):
		# storing the accumulated weight factor
		self.accumWeight = accumWeight

		# initializing the bg model
		self.bg = None

	def update(self, image):
		# initializes if bg model is set to none 
		if self.bg is None:
			self.bg = image.copy().astype("float")
			return

		# update the background model by accumulating the weighted
		# average
		cv2.accumulateWeighted(image, self.bg, self.accumWeight)

	def detect(self, image, tVal=25):
		# takes the absolute difference between the bg model
		# and the current image, then threshold the delta image
		delta = cv2.absdiff(self.bg.astype("uint8"), image)
		thresh = cv2.threshold(delta, tVal, 255, cv2.THRESH_BINARY)[1]

		# removes noise and/or false positives
		thresh = cv2.erode(thresh, None, iterations=2)
		thresh = cv2.dilate(thresh, None, iterations=2)

		# applies contour detection and extracts motion region
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		(minX, minY) = (np.inf, np.inf)
		(maxX, maxY) = (-np.inf, -np.inf)

		# ignore if no contours were found
		if len(cnts) == 0:
			return None

		# otherwise, loop over the contours
		for c in cnts:
			# compute the bounding box of the contour and use it to
			# update the minimum and maximum bounding box regions
			(x, y, w, h) = cv2.boundingRect(c)
			(minX, minY) = (min(minX, x), min(minY, y))
			(maxX, maxY) = (max(maxX, x + w), max(maxY, y + h))

		# otherwise, return a tuple of the thresholded image along
		# with bounding box
		return (thresh, (minX, minY, maxX, maxY))