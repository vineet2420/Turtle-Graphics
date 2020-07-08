from turtle import *;

#draw a rectangle
def drawRect(x, height):
	penup()
	goto(x,0)
	pendown()
	setheading(0)
	fillcolor("black")
	begin_fill()
	for i in range(4):
		if i%2 == 0:
			forward(5);
		else:
			forward(height);
		left(90)
	end_fill()

#draw 20 bars
for x in range(20):
	drawRect(10*x,10*x)
input()
