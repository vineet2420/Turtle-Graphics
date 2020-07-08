from turtle import *;
#1. draw 8 rows:
speed(0);
for row in range(8):
	#draw a row of 8 cells:
	for col in range(8):
		#draw the cell at (row,col):
		x=10*col;
		y=10*row;
		if (row+col)%2==0:
			fColor="black";
		else:
			fColor="white";
		penup();
		goto(x,y);
		pendown();
		fillcolor(fColor);
		begin_fill();
		for i in range(4):
			forward(10);
			left(90)
		end_fill();
input()
