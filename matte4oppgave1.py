from sys import argv
import math

trapezoids = int(argv[1].strip())
lower_bound = -1.0
upper_bound = 1.0
interval_size = upper_bound-lower_bound
h = interval_size/trapezoids


def f(x):
    return math.e**(-x**2)

J = 0
J+=f(lower_bound)/2*h
J+=f(upper_bound)/2*h
for i in range( trapezoids - 2):
    J+=f(lower_bound+(1+i)*h)*h
print J
