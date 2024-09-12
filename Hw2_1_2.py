#Hw2
#cylinder
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,100,1000)

f = 1/(x**2+1)**0.5


plt.figure()
plt.plot(x,f)
plt.title('Ring of Charge')
plt.xlabel('z/R')
plt.ylabel('Ez/Eo')
plt.show()

