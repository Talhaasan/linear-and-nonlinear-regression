import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-whitegrid")

data = pd.read_csv("linear.csv")

x = data["size"]
y = data["price"]

c,d,e,f =  np.polyfit(x,y,3)

L = 0.00001  # The learning Rate
repeat = 1  # The number of iterations to perform gradient descent

n = float(len(x)) # Number of elements in X

# Performing Gradient Descent 
for i in range(repeat): 
    y_pred = c*(x**3)+d*(x**2)+ e*x+ f  # The current predicted value of Y
   
    
    D_c = (-2/n) * sum(x * (y - y_pred))  # Derivative wrt c
    D_d = (-2/n) * sum(x * (y - y_pred))  # Derivative wrt f
    D_e = (-2/n) * sum(x * (y - y_pred))  # Derivative wrt e
    D_f = (-2/n) * sum(y - y_pred)  # Derivative wrt f
    
   
    c = c - L * D_c  # Update c
    d = d - L * D_d  # Update c
    e = e - L * D_e  # Update e
    f = f - L * D_f  # Update f
   
    print (c,d,e,f)

# Making predictions
y_pred = c*(x**3)+ d*(x**2)+ e*x+ f

z = np.arange(150)
plt.scatter(x,y)

plt.plot(z,c*(z**3) +d*(z**2)+ e*z +f,color='red')

plt.show()

# b,c,d,e,f =  np.polyfit(x,y,4)

# L = 0.00001  # The learning Rate
# repeat = 20  # The number of iterations to perform gradient descent

# n = float(len(x)) # Number of elements in X

# # Performing Gradient Descent 
# for i in range(repeat): 
#     y_pred = b*(x**4) +c*(x**3) +d*(x**2)+ e*x+ f  # The current predicted value of Y
   
#     D_b = (-2/n) * sum(x * (y - y_pred))  # Derivative wrt b
#     D_c = (-2/n) * sum(x * (y - y_pred))  # Derivative wrt c
#     D_d = (-2/n) * sum(x * (y - y_pred))  # Derivative wrt f
#     D_e = (-2/n) * sum(x * (y - y_pred))  # Derivative wrt e
#     D_f = (-2/n) * sum(y - y_pred)  # Derivative wrt f
    
#     b = b - L * D_b  # Update b
#     c = c - L * D_c  # Update c
#     d = d - L * D_d  # Update c
#     e = e - L * D_e  # Update e
#     f = f - L * D_f  # Update f
   
#     print (b,c,d,e,f)

# # Making predictions
# y_pred = b*(x**4) +c*(x**3) +d*(x**2) +e*x+ f

# z = np.arange(150)
# plt.scatter(x,y)

# plt.plot(z,b*(z**4)+ c*(z**3) +d*(z**2) +e*z+ f,color='red')

# plt.show()

# a,b,c,d,e,f =  np.polyfit(x,y,5)

# L = 0.00001  # The learning Rate
# repeat = 20  # The number of iterations to perform gradient descent

# n = float(len(x)) # Number of elements in X

# # Performing Gradient Descent 

# for i in range(repeat): 
#     y_pred = a*(x**5)+ b*(x**4) +c*(x**3)+ d*(x**2) + e*x+ f  # The current predicted value of Y
   
#     D_a = (-2/n) * sum(x * (y - y_pred))  # Derivative wrt a
#     D_b = (-2/n) * sum(x * (y - y_pred))  # Derivative wrt b
#     D_c = (-2/n) * sum(x * (y - y_pred))  # Derivative wrt c
#     D_d = (-2/n) * sum(x * (y - y_pred))  # Derivative wrt f
#     D_e = (-2/n) * sum(x * (y - y_pred))  # Derivative wrt e
#     D_f = (-2/n) * sum(y - y_pred)  # Derivative wrt f
    
#     a = a - L * D_a  # Update a
#     b = b - L * D_b  # Update b
#     c = c - L * D_c  # Update c
#     d = d - L * D_d  # Update c
#     e = e - L * D_e  # Update e
#     f = f - L * D_f  # Update f
   
#     print (a,b,c,d,e,f)

# # Making predictions
# y_pred = a*(x**5)+ b*(x**4)+ c*(x**3)+ d*(x**2)+ e*x+ f

# z = np.arange(150)
# plt.scatter(x,y)

# plt.plot(z,a*(z**5)+ b*(z**4)+ c*(z**3) +d*(z**2) +e*z+ f,color='red')

# plt.show()



















