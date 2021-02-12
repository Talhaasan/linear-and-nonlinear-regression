import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")
data = pd.read_csv("linear.csv")

x = data["size"]
y = data["price"]

x = np.array(x)
y= np.array(y)


b,c,d,e,f =  np.polyfit(x,y,4)

z = np.arange(150)

plt.scatter(x,y)

print (b,c,d,e,f)

plt.plot(z,b*(z**4)+c*(z**3)+d*(z**2)+e*z+f,color='red')
plt.show()


# a,b,c,d,e,f =  np.polyfit(x,y,5)

# z = np.arange(150)

# plt.scatter(x,y)

# print (a,b,c,d,e,f)

# plt.plot(z,a*(z**5)+b*(z**4)+c*(z**3)+d*(z**2)+e*z+f,color='red')
# plt.show()



# a,b,c,d,e,f,g =  np.polyfit(x,y,6)
# z = np.arange(150)

# plt.scatter(x,y)

# print (g,a,b,c,d,e,f)

# plt.plot(z,g*(z**6)+a*(z**5)+b*(z**4)+c*(z**3)+d*(z**2)+e*z+f,color='red')
# plt.show()





