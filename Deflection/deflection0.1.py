# Simulation deflecting rays.
from __future__ import division
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import array, dot, linalg
from pylab import show, savefig
from math import sqrt, tan, asin
from time import time
import create
import psyco


def mag2(vec):
    return float(dot(vec,vec))

def mag(vec):
    return float(linalg.norm(vec))

def norm(vec):
    return vec/mag(vec)

def read(x0, pic):                   #Eats an array and returns the correspondient pixel
    x=round(x0[0])
    y=round(x0[1])
    if x<0: return (0,0,1)
    elif y<0: return (1,0,0)
    elif x>=m: return (0,1,0)
    elif y>=n: return (1,0,1)
    else: return pic[x][y]

def dist(a,b):
#    if len(a)!=len(b): raise 'TypeError: should be list of the same length'     #We can assume that, for the shake of perfomance.
    d=0
    for i in xrange(len(a)):
       d+=(a[i]-b[i])**2
    return sqrt(d)


# Setup:
psyco.full()
t0=time()
img=mpimg.imread('galaxy.png')

m=len(img)
n=len(img[0])

imgf=create.white(m, n)


# Parameters:


lenses=[[2,[301,314]]]   # [Schwarchild radius, (vector position, R^2)]
distance=3000                 # Distance from 
bes=[]

#Iterating:
for i in xrange(m):
    for j in xrange (n):
        ob=array([i,j])
        readable=True
        for lens in lenses:
            b=dist([i,j],lens[1])
            if b<=lens[0]:
                imgf[i][j]=(1,1,0)  # Ray eaten.
                readable=False
                break
            else:
                sa=lens[0]/b
                a=tan(asin(sa))
#                a=sa/sqrt(1-sa**2)
                bes.append(a)
                vdir=norm(array(lens[1])-array([i, j]))                      #Director vector.
                ob+=a*distance*vdir
                #print vdir,a, ob
        if readable==True: imgf[i][j]=read(ob,img)



# Results

plt.imshow(imgf).set_interpolation('nearest')
print time()-t0

show()