import matplotlib.pyplot as plt

x0 = 1  #initial value, could be anything
a = 2   #number to find root of
x = x0
n = 0
xnlist = []
nlist = []
errlist = []


while n < 10:
    x = (1/2)*(x+a/x)
    n = n + 1
    xnlist.append(x)    #list of all x values in loop
    nlist.append(n)
    errlist.append(abs(((x*x)-a)/a)) #making a list of the relative error of xn^2


plt.scatter(nlist,xnlist)       #graph of x vs n
plt.title("Computed Value of √2 per Iteration")
plt.xlabel("Iteration Number n")
plt.ylabel("Root of %s" % a)
plt.show()

plt.scatter(nlist,errlist)      #graph of error in x^2 vs n
plt.title("Relative Error in x\u00b2 per Iteration")
plt.yscale('log')
plt.xlabel("Iteration Number n")
plt.ylabel("Relative Error of Root Squared")
plt.show()
print(x)