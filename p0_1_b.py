import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('linear.csv')

x = data["size"]
y = data["price"]

plt.scatter(x, y)

m = 0
b = 0

L = 0.0001  # The learning Rate
repeat = 1000  # The number of iterations to perform gradient descent

n = float(len(x)) # Number of elements in X

# Performing Gradient Descent 
for i in range(repeat): 
    y_pred = m*x + b  # The current predicted value of Y
    D_m = (-2/n) * sum(x * (y - y_pred))  # Derivative wrt m
    D_b = (-2/n) * sum(y - y_pred)  # Derivative wrt b
    m = m - L * D_m  # Update m
    b = b - L * D_b  # Update b
    
print (m, b)

# Making predictions
y_pred = m*x + b

plt.plot([min(x), max(x)], [min(y_pred), max(y_pred)], color='red') # predicted
plt.show()
