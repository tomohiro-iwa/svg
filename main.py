import math

import SVG

def LSTM(x,y):
	txt = SVG.rect(x,y,100,20)
	return txt



g = SVG.SVG(800,1200)
g.append(LSTM(0,0))
print(g.tostr())
