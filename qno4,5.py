# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:49:19 2017

@author: rameen
"""

import random
mylist=random.sample(range(0,100),50)
random.seed(0000)
print("sample list:",mylist)
print("length of my list is",len(mylist))
def sum_list(mylist):
  n=0
  for i in mylist:
      n= n+i
  return n/len(mylist)
print("the mean value is:\t\t",sum_list(mylist))


mylist.sort()
print(mylist)
n=len(mylist)
def median(mylist):
    if len(mylist) % 2!=0:
         return mylist[n//2]
    else:
           return (((mylist[n//2] )+ (mylist[(n//2)-1]))/2)
print("the mean value is:\t",sum_list(mylist))
print("median is:\t\t",median(mylist))


def quart1(mylist):
    if len(mylist)%2==0:
       x=mylist[len(mylist)//4]
       return x
    else:
        x=(((mylist[len(mylist)//4] )+ (mylist[(len(mylist)//4)+1]))/2)
        return x
print("1st quartile is:\t",quart1(mylist))  

  
def quart3(mylist):
    if len(mylist)%2==0:
       x=mylist[3*(len(mylist))//4]
       return x
    else:
        x=(((mylist[3*(len(mylist))//4] )+ (mylist[(3*(len(mylist))//4)+1]))/2)
        return x
print("3rd quartile is:\t",quart3(mylist))


def variance(mylist):    
    sum2=0
    for items in range(len(mylist)):
           sum2=sum2+((items-sum_list(mylist))**2)
    return sum2//len(mylist)-1
print("variance is:\t",variance(mylist))

def sd(mylist):
    return variance(mylist)**0.5
print("standard daviation is:\t",sd(mylist))

def ci_pos(mylist):
    x=(sum_list(mylist)+(1.645*sd(mylist)))/(3*0.5)
    return x
print("confidence intervall for 90% is:\t\t\t\t",ci_pos(mylist))
def ci_neg(mylist):
    x=(sum_list(mylist))-(1.645*sd(mylist))/(3*0.5)
    return x
print("confidence intervall for 90% is:\t\t\t\t",ci_neg(mylist))

print("confidence interval ranging from:\t\t\t\t",ci_pos(mylist),"to",ci_neg(mylist))
def conf_interval(mylist):
    for items in mylist:
        if items>ci_neg(mylist) or items<ci_pos(mylist):
            
          return items
print("the values lie within confidence interval range are:\t\t",conf_interval(mylist))
print("the percentage of values within confidence interval range are:\t",(conf_interval(mylist)/len(mylist))*100)
            
