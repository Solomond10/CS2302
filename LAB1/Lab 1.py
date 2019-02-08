#Course: CS2302 - Spring 2019
#Author: Solomon Davis
#Lab Number: 1
#Instructor: Olac Fuentes
#Last Modified: February 8, 2019
#Due Date: February 8, 2019
#Description: This code will draw figures using recursicve calls. For figure 1
#             ,the squares, the program will make 4 recursive calls. Each call 
#             places a square in a specific location on the base square. In 
#             figure 2 the first circle figure the draws circles inside simply
#             with one recursive call. In figure 3 the tree branch like is 
#             is programmed with 2 recursive calls that extends both sides of
#             each branch. In figure 4 ,the second circular figure, 5 circles 
#             are recursively inside tbe base circle. These circles rotate each
#             circle in the figure. 

import numpy as np
import matplotlib.pyplot as plt
import math 

def draw_squares(ax,n,p):
    if n>0:
        q = p*.50 - p[3:4]/4 -p[1:2]/4
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,q + p[0:1])
        draw_squares(ax,n-1,q + p[1:2])
        draw_squares(ax,n-1,q + p[2:3])
        draw_squares(ax,n-1,q + p[3:4])
        
orig_size = 100
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,2,p)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('figure 1 squares pic 1.png')

orig_size = 100
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,3,p)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('figure 1 squares pic 2.png')
 
orig_size = 100
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,4,p)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('figure 1 squares pic 3.png')

import matplotlib.pyplot as plt
import numpy as np
import math 

def figure_2_circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = figure_2_circle(center,radius)
        ax.plot(x,y,color='k')
        draw_circles(ax,n-1,[radius*w,center[1]],radius*w,w)
     
fig, ax = plt.subplots() 
draw_circles(ax,35,[100,0],100,.5)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('figure 2 circle pic 1.png')

fig, ax = plt.subplots() 
draw_circles(ax,50,[100,0],100,.85)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('figure 2 circle pic 2.png')

fig, ax = plt.subplots() 
draw_circles(ax,90,[100,0],100,.95)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('figure 2 circle pic 3.png')

import numpy as np
import matplotlib.pyplot as plt

def draw_trees(ax,n,p):
    if n>0:
        q = p/2 - p[1:2]/2
         
        ax.plot(p[:,0],p[:,1],color='k')
        draw_trees(ax,n-1,q + p[0:1])
        draw_trees(ax,n-1,q + p[2:])

orig_size = 100
p = np.array([[0,0],[5,25],[10,0]])
fig, ax = plt.subplots()
draw_trees(ax,3,p)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('figure 3 trees pic 1.png')

orig_size = 100
p = np.array([[0,0],[5,25],[10,0]])
fig, ax = plt.subplots()
draw_trees(ax,4,p)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('figure 3 trees pic 2.png')

orig_size = 100
p = np.array([[0,0],[5,25],[10,0]])
fig, ax = plt.subplots()
draw_trees(ax,7,p)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('figure 3 trees pic 3.png')

import matplotlib.pyplot as plt
import numpy as np
import math 

def figure_4_circle(c,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = c[0]+rad*np.sin(t)
    y = c[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,c,rad,w):
    r = 2/3*rad
    if n>0:
        x,y = figure_4_circle(c,rad)
        ax.plot(x,y,color='k')
        draw_circles(ax,n-1,[c[0],c[1]+r],rad*w,w)
        draw_circles(ax,n-1,[c[0],c[1]-r],rad*w,w)
        draw_circles(ax,n-1,[c[0],c[1]],rad*w,w)
        draw_circles(ax,n-1,[c[0]+r,c[1]],rad*w,w)
        draw_circles(ax,n-1,[c[0]-r,c[1]],rad*w,w)
     
fig, ax = plt.subplots() 
draw_circles(ax,5,[0,0],60,(1/3))
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('figure 4 circle pic 1.png')

fig, ax = plt.subplots() 
draw_circles(ax,4,[0,0],60,(1/3))
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('figure 4 circle pic 2.png')

fig, ax = plt.subplots() 
draw_circles(ax,3,[0,0],60,(1/3))
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('figure 4 circle pic 3.png')