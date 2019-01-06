import math

class Node:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def update(self):
		margin = 5
		self.u = self.y +margin
		self.d = self.y+self.h +margin
		self.l = self.x -margin
		self.r =  self.x+self.w +margin
		self.cx = self.x+(self.w/2.0)
		self.cy = self.y+(self.h/2.0)


	def get(self,direction):
		margin = 5
		if direction=="u":
			return ( self.x+(self.w/2.0), self.y -margin )
		if direction=="d":
			return ( self.x+(self.w/2.0), self.y+self.h +margin )
		if direction=="l":
			return ( self.x -margin, self.y+(self.h/2.0) )
		if direction=="r":
			return ( self.x+self.w +margin, self.y+(self.h/2.0) )
		if direction=="c":
			return ( self.x+(self.w/2.0), self.y+(self.h/2.0) )

	def tostr(self):
		return '<use xlink:href="#lstm" transform="translate(%d,%d)"></use>\n' % (self.x,self.y)


class LSTM(Node):
	def __init__(self,x,y):
		super().__init__(x,y)
		self.w = 150
		self.h = 50
		self.update()
	
	def tostr(self):
		return '<use xlink:href="#lstm" transform="translate(%d,%d)"></use>\n' % (self.x,self.y)

class W(Node):
	def __init__(self,x,y):
		super().__init__(x,y)
		self.w = 150
		self.h = 50
		self.update()
	
	def tostr(self):
		return '<use xlink:href="#w" transform="translate(%d,%d)"></use>\n' % (self.x,self.y)

class Wave(Node):
	def __init__(self,x,y):
		super().__init__(x,y)
		self.w = 30
		self.h = 50
		self.update()
	
	def get(self,direction):
		margin = -5
		if direction=="u":
			return ( self.x+(self.w/2.0), self.y -margin )
		if direction=="d":
			return ( self.x+(self.w/2.0), self.y+self.h +margin )
		if direction=="l":
			return ( self.x -margin, self.y+(self.h/2.0) )
		if direction=="r":
			return ( self.x+self.w +margin, self.y+(self.h/2.0) )
		if direction=="c":
			return ( self.x+(self.w/2.0), self.y+(self.h/2.0) )
		
	def tostr(self):
		return '<use xlink:href="#wave" transform="translate(%d,%d)"></use>\n' % (self.x,self.y)

class Word(Node):
	def __init__(self,x,y):
		super().__init__(x,y)
		self.w = 150
		self.h = 50
		self.word = "word"
		self.update()
	
	def tostr(self):
		txt  = '<g transform="translate(%d,%d)">' % (self.x,self.y) 
		txt += '<text x="75" y="20" text-anchor="middle"'
		txt += ' fill="#000000" stroke="#000000" style="font-size:50px">%s</text>' % self.word
		txt += '</g> \n'
		return txt
	
	def setword(self,word):
		self.word = word

class Hotvec(Node):
	def __init__(self,x,y):
		super().__init__(x,y)
		self.w = 180
		self.h = 50
		self.update()
		self.one = 0
	
	def tostr(self):
		txt  = '<g transform="translate(%d,%d)">' % (self.x, self.y)
		txt += '<rect x="0" y="0" width="180" height="50" '
		txt += 'stroke-width="4" stroke-dasharray="8 8" fill="#ffffff" stroke="#000000"/>'
		
		tmp = '<circle cx="%d" cy="25" r="15" fill="%s" stroke="black" stroke-width="2" />'
		for i in range(5):
			if i == self.one:
				color = "#000000"
			else:
				color = "#ffffff"
			txt += tmp % (20+35*i,color)
		txt += '</g>'
		return txt

class Concat(Node):
	def __init__(self,x,y):
		super().__init__(x,y)
		self.w = 140
		self.h = 60
		self.update()
	
	def tostr(self):
		return '<use xlink:href="#concat" transform="translate(%d,%d)"></use>\n' % (self.x,self.y)

class Emb(Node):
	def __init__(self,x,y):
		super().__init__(x,y)
		self.w = 150
		self.h = 50
		self.update()

	def tostr(self):
		return '<use xlink:href="#emb" transform="translate(%d,%d)"></use>\n' % (self.x,self.y)

r=10.0
def between(a,b,avoid):
	if a[0] == b[0] and a[0] == avoid[0]:
		if a[1] < avoid[1]:
			return "u"
		else:
			return "d"
	if a[1] == b[1] and a[1]== avoid[1]:
		if a[0] < avoid[0]:
			return "l"
		else:
			return "r"
	return None

def curve(c,start):
	if start == "u":
		s = 1.5
	if start == "d":
		s= 0.5
	if start == "r":
		s = 0.0
	if start == "l":
		s = 1.0
	
	result = []
	for i in range(11):
		theta = (s+i*0.1)*math.pi
		result.append( (c[0]+math.cos(theta)*r,c[1]+math.sin(theta)*r) )
	return result

def line(start, end, point="l", relay=[],avoid=[]):
	ps = []
	ps.append(start.get("c"))
	for i in relay:
		ps.append(i)
	ps.append(end.get(point))

	points = []
	for i in range(len(ps)-1):
		points.append(ps[i])
		for j in avoid:
			direction = between(ps[i],ps[i+1],j)
			if direction != None:
				orbit = curve(j,direction)
				points.extend(orbit)

	points.append(ps[-1])

	txt = "<polyline points=\""
	for i in points:
		txt += "%d,%d " % i
	txt += "\" fill=\"none\" stroke=\"black\" stroke-width=\"4\" marker-end=\"url(#arrow)\" />\n"
	return txt
