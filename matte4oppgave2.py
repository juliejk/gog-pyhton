import numpy
import scipy
import matplotlib.pyplot as plt
import math

f_array = [-14.1014,-0.931597,0.0000000,0.931597,14.1014]
x_array = [-1.5,-0.75,0.0,0.75,1.5]

def l(n,x,x_array):
    holder = x_array[n]
    x_array[n] = x-1
    l = 1.0
    for i in range(len(x_array)):
        l*=x-x_array[i]
    x_array[n] = holder
    return l

def p(x,x_array,f_array):
    p = 0.0
    for k in range(len(x_array)):
        p+=f_array[k]*l(k,x,x_array)/l(k,x_array[k],x_array)
    return p

points = 100
start = -2.0
stop = 2.0
step = (stop-start)/points
x_plot = numpy.linspace(start,stop,points)
y_plot = []
for i in range(points):
    y_plot.append(p(start+step*i,x_array,f_array))
tan = []
for i in range(points):
    tan.append(math.tan(x_plot[i]))

plt.plot(x_plot, y_plot, 'o')
plt.plot(x_plot, tan, '+')
plt.plot(x_array,f_array, 'x')
plt.ylim([-15.0,15.0])
plt.xlim([-math.pi/2.0,math.pi/2.0])
plt.show()


