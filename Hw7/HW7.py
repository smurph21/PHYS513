#HW7

# Something went wrong with your RK implementation. I suggest using scipy.integrate.RK45 rather than writing your own implementation (or do both and compare).

import numpy as np
import matplotlib.pyplot as plt

#inputs
q = 1
Re = 6.356*10**6
x0 = 2*Re
v0 = 10**7
B0 = 3*10**-5
KE = 10*10*6
m = 2*KE/v0**2
print(m)
#time
t = 100
h = 0.1
stp = (100-0)/h
#IC
pos = np.array([x0,0,0])
v = np.array([v0,0,0])

stor = np.zeros([int(stp),3])

#FE
for i in range(int(stp)):
    #plotting
    stor[i] = pos
    #r/B
    r = (pos[0]**2+pos[1]**2)**0.5
    B = np.array([0,0,-B0/(r/Re)**3])
    #update position
    pos[0] = pos[0]+v[0]*h
    pos[1]=pos[1]+v[1]*h

    #solve v
    cross = np.cross(v, B)
    v = (q*h/m)*cross+v

    print(v)
    print(0.5*m*r**2)

    
plt.figure()
plt.plot(stor[:,0],stor[:,1], 'rs')
plt.xlabel('xpos')
plt.ylabel('ypos')
plt.title('Proton position')
plt.show()


#RK
for i in range(int(stp)):
    #plotting
    stor[i] = pos
    #r/B
    r = (pos[0]**2+pos[1]**2)**0.5
    B = np.array([0,0,-B0/(r/Re)**3])
    #update position
    k1 = pos
    r1 = (k1[0]**2+k1[1]**2)**0.5
    B1 = np.array([0,0,-B0/(r1/Re)**3])
    
    k2 = pos+h/2*k1
    r2 = (k2[0]**2+k2[1]**2)**0.5
    B2 = np.array([0,0,-B0/(r2/Re)**3])

    k3 = pos+h/2*k2
    r3 = (k2[0]**2+k2[1]**2)**0.5
    B3 = np.array([0,0,-B0/(r3/Re)**3])

    k4 = pos+h*k3
    r4 = (k3[0]**2+k3[1]**2)**0.5
    B4 = np.array([0,0,-B0/(r4/Re)**3])

    pos = pos+h/6*(k1+2*k2+2*k3+k4)
    
    k1 = v
    k2 = (q*h/m)*np.cross(k1, B1)+h/2*k1
    k3 = (q*h/m)*np.cross(k2, B2)+h/2*k2
    k4 = (q*h/m)*np.cross(k3, B3)+h*k3

    #solve v
    v = v+h/6*(k1+2*k2+2*k3+k4)

    print(v)
    print(0.5*m*r**2)

plt.figure()
plt.plot(stor[:,0],stor[:,1], 'rs')
plt.xlabel('xpos')
plt.ylabel('ypos')
plt.title('Proton position')
plt.show()
