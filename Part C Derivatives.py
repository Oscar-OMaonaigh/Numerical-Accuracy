import matplotlib.pyplot as plt
import numpy as np


#h = 2.220446049250313e-16
h = 1
def yc(t):
    return np.cos(t)

def ye(t):
    return np.exp(t)

#                           Forward Difference

def FDc(t):
    return (yc(t + h) - yc(t))/h 

def FDe(t):
    return (ye(t + h) - ye(t))/h 

#                           Central Difference

def CDc(t):
    return (yc(t + h/2) - yc(t - h/2))/h

def CDe(t):
    return (ye(t + h/2) - ye(t - h/2))/h

#                            Relative Errors

def Fce(t):
    return abs((FDc(t) - (-np.sin(t)))/-np.sin(t))

def Fee(t):
    return abs(FDe(t) - (np.e**t))/np.e**t

def Cce(t):
    return abs((CDc(t) - (-np.sin(t)))/-np.sin(t))

def Cee(t):
    return abs(CDe(t) - (np.e**t))/np.e**t

hlist = []

Fcerr = []
Feerr = []
Ccerr = []
Ceerr = []

#print out derivative and its error as a function of h
t = 0.1
while h > 2.220446049250313e-16:
    hlist.append(h)
    
    Fcerr.append(Fce(t))
    Feerr.append(Fee(t))
    Ccerr.append(Cce(t))
    Ceerr.append(Cee(t))
    h = h*0.95


#                         Cos(x) Plot

plt.loglog(hlist,Ccerr,label = "Central Difference",lw = 1,color = "firebrick")
plt.loglog(hlist,Fcerr,label = "Forward Difference",lw = 1, color = "dodgerblue")
plt.title("y(t) = cos(t)")
plt.xlabel("Size of h")
plt.ylabel("Relative Error")
plt.legend()
plt.show()

#                           e^x Plot

plt.loglog(hlist,Ceerr,label = "Central Difference",lw = 1,color = "firebrick")
plt.loglog(hlist,Feerr,label = "Forward Difference",lw = 1,color = "dodgerblue")
plt.title("y(t) = e\u1D57")
plt.xlabel("Size of h")
plt.ylabel("Relative Error")
plt.legend()
plt.show()

