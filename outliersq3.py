# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:01:34 2017

@author: rameen
"""
import random
mylist=[random.randint(1,100) for index in range(0,10000)]
random.seed(2312)
print(mylist)
mylist.sort()
print(mylist)
def quart1(mylist):
    if len(mylist)%2==0:
       x=mylist[len(mylist)//4]
       return x
    else:
        x=(((mylist[len(mylist)//4] )+ (mylist[(len(mylist)//4)+1]))/2)
        return x
print("1st quartile is:",quart1(mylist))    
def quart3(mylist):
    if len(mylist)%2==0:
       x=mylist[3*(len(mylist))//4]
       return x
    else:
        x=(((mylist[3*(len(mylist))//4] )+ (mylist[(3*(len(mylist))//4)+1]))/2)
        return x
print("3rd quartile is:",quart3(mylist))  
iqr=  quart3(mylist)-quart1(mylist)
print("interquartile range is:\t",iqr)
def outliers(mylist):
  result=[]
  for index in range(0,len(mylist)):
     if mylist[index]>int(quart3(mylist)+1.5*(iqr)) or mylist[index]<int(quart1(mylist)-1.5*(iqr)):
            result=result+[mylist[index]]
  return result
print("outliers are",outliers(mylist))