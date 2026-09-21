# Numerical-Accuracy
Project to understand different forms of numerical accuracy and efficiency.
This project includes Heron's Root Finding method, Analysis of Overflow,Underflow,Machine Precision and Complex Machine Precision, and different derivative algorithms, Central Difference and Forward Difference.

Heron's Root Finding method is an incredibly efficient ancient iterative algorithm to find a square root from a random initial value. The formula is as follows:
X(n+1) = 1/2(Xn + S/Xn) where S is the number you want to find the root of.
For this project the initial value was 1 for simplicity, but any value will work.
The algorithm is ran for 10 iterations, and the error and relative error were recorded and displayed in a graph.
To find the root of 2, with a relative error of 2.22e-16, the algorithm only took 5 iterations.
This project shows how efficient this ancient algorithm is, so much that it could be computed by hand easily.

Overflow and Underflow are errors that occur when a number is too big or too small respectively for a computer to accurately represent. 
This is a result of the number taking up more memory than its maximum. 
To calculate these limits, 1 was multiplied or divided by 2 until the result was infinity or 0 respectively.
The value was taken just before this was the case, and the number of operations to reach that limit was noted.
The overflow occurs after 1024 operations, with the largest correct number being 8.988466e+307
The Underflow occurs after 1075 operations, with the smallest correct number being 5e-324
The machine precision and complex machine precision were also measured, seeing how small a float and a complex number had to be before being deemed negligible.
The values for Machine Precision and Complex Machine Precision ended up being identical, at 2.220446049250313e-16.

Forward Difference and Central Difference are two methods of finding derivatives. This project compares their efficiencies.
The formula for Forward Difference is:
f'(x) = (f(x+h) - f(x))/h
Essentially the first principles derivative equation.
The error in this formula is O(h), so if h decreases by 10, so will the error.
The formula for Central Difference is:
f'(x) = (f(x + h/2) - f(x - h/2))/h
It finds the derivative at a point by looking at two equidistant points around it. 
The error in this formula is O(h^2), so if h decreases by 10, the error decreases by 100.
I created formulas to find the relative errors for both methods, and ran a while loop until h reached the machine precision limit as found earlier, 2.220446049250313e-16
Two formulae were chosen to calculate their derivatives, e^x and cos(x). The relative errors were compared to their known derivatives, e^x and -sin(x).
The relative error for each method was saved alongside the h value, and a log log plot was made for each formula to show how each method evolved over time.
Immediately noticable is that there is a rough spiky line that increases the error as h decreases, which comes from rounding errors. 
This rounding error section of the graph seems to follow the formula relative error = 2.220446049250313e-16/h, which makes sense given the machine precision found earlier.
The Central Difference method has a larger slope, reaching lower error values at higher h values than the Forward Difference method. 
Another note is that the Central Difference method reaches a lower relative error value altogether, as the slope is cut off when it reaches the relative error = 2.220446049250313e-16/h line.
This means that the Central Difference method is not only faster and more efficient at reaching lower error values, it can reach relative error values 10^-4 times lower than the Forward Difference method possibly can.
