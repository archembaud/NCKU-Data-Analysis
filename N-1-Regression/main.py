import numpy as np
import matplotlib.pyplot as plt

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 4, 6])

# A @ c = y -> Rewrite equation as y = mx + c
# Create a matrix A with a column of x and a column of ones
A = np.vstack([x, np.ones(len(x))]).T

# Use the least-squares solver
# rcond=None uses machine precision automatically
slope, intercept = np.linalg.lstsq(A, y, rcond=None)[0]

print(f"Slope: {slope:.4f}")
print(f"Intercept: {intercept:.4f}")

# Show with a line
X = np.linspace(0, 5, num=20)
Y = slope*X + intercept
plt.scatter(x,y,c='b',marker='o')
plt.plot(X,Y,c='r')
plt.show() 
