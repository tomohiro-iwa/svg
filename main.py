import math
import SVG

from f import *


boxes = []
g = SVG.SVG(850,1300)
g.append(open("define.svg").read())

concat1 = Concat(  0, 400)
concat2 = Concat(100, 450)
boxes.append(concat1)
boxes.append(concat2)

for i in range(2):
	if i == 0:
		x = 200
		y = 900
	if i == 1:
		x = 200
		y = 500

	for i in range(3):
		boxes.append(LSTM(x+225*i,y))
	g.append(line(boxes[-1],boxes[-2],"r"))
	g.append(line(boxes[-2],boxes[-3],"r"))

	for i in range(3):
		boxes.append(LSTM(x+225*i,y+90))
	g.append(line(boxes[-1],boxes[-2],"r"))
	g.append(line(boxes[-2],boxes[-3],"r"))

	for i in range(3):
		boxes.append(Emb(x+225*i,y+180))

	for i in range(3):
		boxes.append(Hotvec(x-25+225*i,y+270))

	for i in range(3):
		g.append(line(boxes[-1-i],boxes[-4-i],"d"))
		g.append(line(boxes[-4-i],boxes[-7-i],"d"))
		g.append(line(boxes[-7-i],boxes[-10-i],"d"))


	g.append(line(boxes[-9],concat2, "d",
	relay=[(concat2.cx,boxes[-9].cy)]
	) )
	g.append(line(boxes[-12],concat1, "d",
	relay=[(concat1.cx,boxes[-12].cy)]
	) )

	for i in boxes:
		g.append(i.tostr())

x = 200
y = 0

for i in range(3):
	boxes.append(Hotvec(x-25+225*i,y))

for i in range(3):
	boxes.append(W(x+225*i,y+90))

for i in range(3):
	boxes.append(LSTM(x+225*i,y+180))

g.append(line(boxes[-2],boxes[-1],"l"))
g.append(line(boxes[-3],boxes[-2],"l"))

for i in range(3):
	boxes.append(LSTM(x+225*i,y+270))
g.append(line(boxes[-2],boxes[-1],"l"))
g.append(line(boxes[-3],boxes[-2],"l"))

for i in range(3):
	boxes.append(Emb(x+225*i,y+370))


for i in range(3):
	g.append(line(boxes[-1-i],boxes[-4-i],"d"))
	g.append(line(boxes[-4-i],boxes[-7-i],"d"))
	g.append(line(boxes[-7-i],boxes[-10-i],"d"))
	g.append(line(boxes[-10-i],boxes[-13-i],"d"))

for i in boxes:
	g.append(i.tostr())
print(g.tostr())
