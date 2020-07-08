from turtle import *;
a=0;
fx=0;
pendown();
speed(100);
for x in range(20):
	goto(0,fx);
	pendown();
	circle(100-a)
	penup();
	fx+=5;
	a+=5
input();
