#!/usr/bin/python

class Mirror():
	def __init__(self, horizontalAngle, verticalAngle):
		self.horizontalAngle = horizontalAngle
		self.verticalAngle = verticalAngle

	def boundsHorizontal(self,increment, startAngle):
		if self.horizontalAngle == 360:
			newIncrement = (startAngle + increment) - 360
			for i in range(newIncrement):
				self.horizontalAngle -= 1
		else:
			for i in range(increment):
				self.horizontalAngle += 1

	def rotateHorizontal(self, increment):
		start = self.horizontalAngle
		for i in range(increment):
			#self.horizontalAngle += 1
			self.boundsHorizontal(increment, start)
			#self.boundsHorizontal(increment)
			#print("horizontal angle = %s\tveritcal Angle = %s" % (self.horizontalAngle, self.verticalAngle))
			if self.horizontalAngle >= 360:
				self.horizontalAngle = 0

	def rotateVertical(self, increment):
		for i in range(increment):
			self.verticalAngle += 1
			print("horitonzal angle = %s\tvertical angle = %s" % (self.horizontalAngle, self.verticalAngle))
			if self.verticalAngle >= 360:
				self.verticalAngle = 0

	'''def boundsHorizontal(self,increment):
		if self.horizontal == 360:
			newIncrement = (startAngle + increment) - 360
			for i in range(newIncrement):
				self.horizontalAngle -= 1
		else:
			for i in range(increment):
				self.horizontalAngle += 1
	'''
myMirror = Mirror(120,90)
myMirror.rotateHorizontal(15)
print("############################")
otherMirror = Mirror(355, 340)
otherMirror.rotateHorizontal(30)
