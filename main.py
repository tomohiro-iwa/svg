import math

import SVG

class Box:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.w = 100
		self.h = 50
		return txt

	def get(self,direction):
		if direction=="u":
			return ( self.x+(self.w/2.0), self.y )
		if direction=="d":
			return ( self.x+(self.w/2.0), self.y+self.h )
		if direction=="l":
			return ( self.x, self.y+(self.h/2.0) )
		if direction=="r":
			return ( self.x+, self.y+(self.h/2.0) )
	def tostr(self):
		return '<use href="#lstm" transform="translate(100,100)"></use>' % (self.x,self.y)

boxes = []

for i in range(6)
	boxes.append(Box())


g = SVG.SVG(800,1200)
g.append(LSTM(0,0))
print(g.tostr())
