# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:06:32 2017

@author: rameen
"""

import random
random.seed(0000)
mylist=[random.randint(1,100) for index in range(0,10000)]
print(mylist)
def mean(mylist):
  n=0
  for i in mylist:
      n= n+i
  return n/len(mylist)
print("the mean value is:\t",mean(mylist))

mylist.sort()
print(mylist)
n=len(mylist)
def median(mylist):
    if len(mylist) % 2!=0:
         return mylist[n//2]
    else:
           return (((mylist[n//2] )+ (mylist[(n//2)-1]))/2)
print("the mean value is:\t",mean(mylist))        
print("median is:\t",median(mylist))
def quart1(mylist):
    if len(mylist)%2==0:
       x=mylist[len(mylist)//4]
       return x
    else:
        x=(((mylist[len(mylist)//4] )+ (mylist[(len(mylist)//4)+1]))/2)
        return x
print("1st quart is:\t",quart1(mylist))    
def quart3(mylist):
    if len(mylist)%2==0:
       x=mylist[3*(len(mylist))//4]
       return x
    else:
        x=(((mylist[3*(len(mylist))//4] )+ (mylist[(3*(len(mylist))//4)+1]))/2)
        return x
print("3rd quart is:\t",quart3(mylist))  

def variance(mylist):    
    sum2=0
    for items in range(len(mylist)):
           sum2=sum2+((items-mean(mylist))**2)
    return sum2//len(mylist)
print("variance is:\t",variance(mylist))

def sd(mylist):
    return (variance(mylist)**0.5)
print("sd is:\t",sd(mylist))

