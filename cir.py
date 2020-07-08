from turtle import *
yInc=0;
radiusDec=0;
speed(0)
for x in range (1,21):
	penup()
	goto(0,yInc)
	pendown()
	circle(100-radiusDec)
	radiusDec += 5
	yInc +=5 

	
input()
