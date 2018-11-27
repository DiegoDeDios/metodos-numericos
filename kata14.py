
import numpy as np
import math
import matplotlib.pyplot as plt
n = 40
a = 0
b = 5  # Este es propuesto
h = 0.1
h2  = 0.05
x = np.linspace(a,b,n)
y0 = 1.5

def fprima(x,y):
    return 2*x*y

def EDO(h,x,y0):
    y = []
    y.append(y0)
    for i in range(1,len(x)):
        y.append(y[i-1] + h*fprima(x[i-1],y[i-1]))
    return y

y = EDO(h,x,y0)
y2 = EDO(h2,x,y0)

plt.plot(x,y,'b')
plt.plot(x,[math.exp(xi) for xi in x],'r')
