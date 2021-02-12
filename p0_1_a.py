import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression as lr
import matplotlib.pyplot as plt

plt.style.use("seaborn-whitegrid")

data = pd.read_csv("linear.csv")

x = data["size"]
y = data["price"]

plt.scatter(x,y)
plt.show()   

x = x.values.reshape(11,1)
y = y.values.reshape(11,1)



lineerregresyon = lr() 

lineerregresyon.fit(x,y) 

lineerregresyon.predict(x) 


m = lineerregresyon.coef_ 
                         
b= lineerregresyon.intercept_ 
                              
                              
a = np.arange(150)

plt.scatter(x,y) 
plt.scatter(a,m*a+b, c="red",linestyle="-", linewidth=0.1)
plt.show()                              
                              
print('Eğim: ', lineerregresyon.coef_)
print('Y de kesiştiği yer: ', lineerregresyon.intercept_)


print("Denklem")
print("y=",m,"x+",b)
