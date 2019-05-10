#Course: CS2302 - Spring 2019

#Author: Solomon Davis
#Lab Number: 8
#Instructor: Olac Fuentes
#Last Modified: May 9, 2019
#Due Date: May 9, 2019
#Description: This Lab will create determine whether an equation from the list 
# eaual to other equations on the list. This lab will also decide if a list is
# a subset of a bigger set using backtracking.
import random
import numpy as np
import math
from math import *
import time
    
def Backtracking(S,S1,S2):
    #Decides if two different sets are a subset of a bigger set. 
    count = 0
    count2 = 0
    for i in range(len(S1)):
        for j in range(len(S)):
            if S1[i] == S[j]:
                count +=1
                
    for i in range(len(S2)):
        for j in range(len(S)):    
            if S2[i] == S[j]:
                count2 +=1
 
    if count == len(S1) and count2 == len(S2):
        print("Partitions",S1,"and",S2," exist")
    else:
        print("Partitions don't exist")

def equal(f1, f2,tries=1000,tolerance=0.0001):
    for i in range(tries):
        #t = random.random()
        t = random.uniform(-math.pi,math.pi)
        y1 = eval(f1)
        y2 = eval(f2)
        if np.abs(y1-y2)>tolerance:
            return False
    return True

def CheckingForTrigIdentities():
    sec = '1/cos(t)'
    List = ['sin(t)','cos(t)','tan(t)',sec,'-sin(t)','-cos(t)', '-tan(t)','sin(-t)','cos(-t)','tan(-t)','sin(t)/cos(t)','2*sin(t/2)*cos(t/2)','sin(t)**2','1-(cos(t)**2)','1-cos(2*t)/2','1/cos(t)']
    List2 = ['sin(t)','cos(t)','tan(t)',sec,'-sin(t)','-cos(t)', '-tan(t)','sin(-t)','cos(-t)','tan(-t)','sin(t)/cos(t)','2*sin(t/2)*cos(t/2)','sin(t)**2','1-(cos(t)**2)','1-cos(2*t)/2','1/cos(t)']


    for i in range(len(List)):
        f1 = List[i]
        for j in range(len(List2)):
            f2  = List2[j]
            if equal(f1,f2) == True:
                print(f1, 'is equal to', f2)
    

startimeProgram = time.time()

S = [1,2,3,4,5]
S1 = [1,2,4]
S2 = [3,5]
CheckingForTrigIdentities()
print('')
Backtracking(S,S1,S2)
endtimeProgram = time.time()
runningtimeProgram = endtimeProgram - startimeProgram
print('')
print('Running Time of Program: ',runningtimeProgram)

