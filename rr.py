# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x1=2
x2=5
y1=3
y2=7
a=0
def dist(a):
    result=(((x2-x1)**2)+((y2-y1)**2))**0.5
    return result
print("distance is",dist(a))

w=6
l=9
r=0
def parameter(r):
    result= (2*l)+(2*w)
    return result
print("parameter of rectangle is",parameter(r))

a=1
b=-2
c=1
result=(-b+((b**2)-4*a*c)**0.5)/(2*a)
result2=(-b-((b**2)-4*a*c)**0.5)/(2*a)

print("roots of equation are:",result,"and",result2)

