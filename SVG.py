def rect(x,y,w,h):
	txt = """
	<rect x="%s" y="%s" width="%s" height="%s" fill="#ffffff" stroke="#000000"/>
	"""
	return txt % (x,y,w,h)

def text(x,y,text):
	txt = """
	<rect x="%s" y="%s" width="%s" height="%s" />
	"""
	return txt % (x,y,text)

class SVG:
	def __init__(self,w,h):
		self.w = w
		self.h = h
		self.node = []

	def tostr(self):
		txt = """
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="%s" height="%s" style="font-size:16px">
%s
</svg>
		"""
		nodes = ""
		for i in self.node:
			nodes+= i
		return txt % (self.w, self.h, nodes)
	
	def append(self,graph):
		self.node.append(graph)
