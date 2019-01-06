import math
import SVG

from f import *


boxes = []
g = SVG.SVG(850,1400)
g.append(open("define.svg").read())

concat = [None,None]
concat[0] = Concat( 10, 490)
concat[1] = Concat(90, 540)

x = 190
y = 30


boxes = [[] for i in range(3)]

boxes[0] = [[None for j in range(3)] for i in range(6)]

for i in range(3):
	boxes[0][0][i] = (Word(x+220*i,y))
boxes[0][0][0].setword("Fix")
boxes[0][0][1].setword("XTest")
boxes[0][0][2].setword("option")

for i in range(3):
	boxes[0][1][i] = (Hotvec(x-15+220*i,y+50))
boxes[0][1][0].one = 0
boxes[0][1][1].one = 2
boxes[0][1][2].one = 3

for i in range(3):
	boxes[0][2][i] = (W(x+220*i,y+140))

for i in range(3):
	boxes[0][3][i] = (LSTM(x+220*i,y+230))

for i in range(3):
	boxes[0][4][i] = (LSTM(x+220*i,y+320))

for i in range(3):
	boxes[0][5][i] = (Emb(x+220*i,y+410))

wave = [[None for j in range(2)] for i in range(3)]
for i in range(2):
	box = boxes[0][3+i][2]
	wave[0][i] = Wave(box.r+30,box.y)
	g.append(line(box,wave[0][i],"l"))
	g.append(wave[0][i].tostr())
#line
for j in range(5,1,-1):
	for k in range(3):
		a = boxes[0][j][k]
		b = boxes[0][j-1][k]
		g.append(line(a,b,"d"))

for j in [3,4]:
	for k in [0,1]:
		a = boxes[0][j][k]
		b = boxes[0][j][k+1]
		g.append(line(a,b,"l"))
for i in [0,1]:
		a = boxes[0][1][i]
		b = boxes[0][5][i+1]
		relay = [
			(a.x+200,a.cy),
			(a.x+200,b.cy)
		]
		avoid = [
			(a.x+200,boxes[0][3][i].cy),
			(a.x+200,boxes[0][4][i].cy)
		]
		g.append(line(a,b,"l",relay=relay,avoid=avoid))

for j in [3,4]:
	a = concat[j-3]
	b = boxes[0][j][0]
	relay=[(a.cx,b.cy)]
	g.append(line(a,b,"l",relay=relay))

g.append(concat[0].tostr())
g.append(concat[1].tostr())

boxes[1] = [[None for j in range(3)] for i in range(5)]
boxes[2] = [[None for j in range(3)] for i in range(5)]
for i in range(1,3):
	if i == 1:
		x = 190
		y = 600
	if i == 2:
		x = 190
		y = 1000

	for j in range(3):
		boxes[i][0][j] = (LSTM(x+220*j,y))

	for j in range(3):
		boxes[i][1][j] = (LSTM(x+220*j,y+80))

	for j in range(3):
		boxes[i][2][j] = (Emb(x+220*j,y+160))

	for j in range(3):
		boxes[i][3][j] = (Hotvec(x-15+220*j,y+240))

	for j in range(3):
		boxes[i][4][j] = (Word(x+220*j,y+320))

	for j in range(2):
		box = boxes[i][j][2]
		wave[i][j] = Wave(box.r+30,box.y)
		g.append(line(wave[i][j],box,"r"))
		g.append(wave[i][j].tostr())

	#line
	for j in range(3,0,-1):
		for k in range(3):
			a = boxes[i][j][k]
			b = boxes[i][j-1][k]
			g.append(line(a,b,"d"))
	for j in [0,1]:
		for k in [2,1]:
			a = boxes[i][j][k]
			b = boxes[i][j][k-1]
			g.append(line(a,b,"r"))
		
boxes[1][3][0].one = 0
boxes[1][3][1].one = 1
boxes[1][3][2].one = 4
boxes[2][3][0].one = 1
boxes[2][3][1].one = 2
boxes[2][3][2].one = 0

boxes[1][4][0].setword("---")
boxes[1][4][1].setword("option")
boxes[1][4][2].setword("INSTALL")
boxes[2][4][0].setword("XTest")
boxes[2][4][1].setword("falls")
boxes[2][4][2].setword("with")

a = boxes[1][0][0]
b = concat[0]
relay=[(b.cx,a.cy)]
avoid=[(concat[1].cx,a.cy)]
g.append(line(a,b,"d",relay=relay,avoid=avoid))

a = boxes[1][1][0]
b = concat[1]
relay=[(b.cx,a.cy)]
g.append(line(a,b,"d",relay=relay))

a = boxes[2][0][0]
b = concat[0]
relay=[(b.cx,a.cy)]
avoid=[(concat[1].cx,a.cy)]
g.append(line(a,b,"d",relay=relay,avoid=avoid))

a = boxes[2][1][0]
b = concat[1]
relay=[(b.cx,a.cy)]
g.append(line(a,b,"d",relay=relay))


for i in boxes:
	for j in i:
		for k in j:
			g.append(k.tostr())

#	g.append(line(boxes[-9],concat2, "d",
#	relay=[(concat2.cx,boxes[-9].cy)]
#	) )
#	g.append(line(boxes[-12],concat1, "d",
#	relay=[(concat1.cx,boxes[-12].cy)]
#	) )

print(g.tostr())
