#                  Initialize Variables

under = 1.0
over = 1.0
emp  = 1.0
cmp = complex(0,1)
N = 1
No = 1


#                       Underflow

while under/2 != 0:
    under = under/2
    N += 1


#                       Overflow

while over*2 != float("inf"):
    over = over*2
    No +=1




#                   Machine Precision

while 1.0 + emp/2 > 1.0:
    emp = emp/2


#               Complex Machine Precision

while complex(0.0, 1.0) + cmp/2 != complex(0,1):
    cmp = cmp/2


#                     Print Results

print("Underflow occurs after %s operations" % N) 
print("Overflow occurs after %s operations" % No)
print("Smallest correct number: %s" % under) 
print("Largest correct number: %s" % "{:e}".format(over)) 
print("Machine Precision is %s" % emp)
print("Complex Machine Precision is %s" % cmp)