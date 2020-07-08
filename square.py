from turtle import *;

side = 10;
pendown()
speed(100);
for x in range(20):

	for z in range (4):
		left(90);
		forward(side);

	side += 10	 #increase the distance moving each side by 10
	goto(0,0)	 #after above tasks run through, do again but only                            difference is the side is +10 so the square will             		  appear bigger for the next square
input();
