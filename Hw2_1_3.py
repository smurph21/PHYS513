#Hw2
#cylinder
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,100,1000)

phi = 1
f = (1/(x**2-phi*x+phi**2+1)**0.5-1/(x**2+phi*x+phi**2+1))*1/phi

phi = 5
f1 = (1/(x**2-phi*x+phi**2+1)**0.5-1/(x**2+phi*x+phi**2+1))*1/phi

phi = 100
f2 = (1/(x**2-phi*x+phi**2+1)**0.5-1/(x**2+phi*x+phi**2+1))*1/phi



plt.figure()
plt.plot(x,f)
plt.plot(x,f1)
plt.plot(x,f2)
plt.legend(['phi = 1', 'phi = 5', 'phi = 100'])
plt.title('Cylinder')
plt.xlabel('z/R')
plt.ylabel('Ez/Eo')
plt.show()

