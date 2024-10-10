#HW5
#Sam Murphy
#problem1

import numpy as np
#left
x = [1/3, 2/3]
y = [1/3, 2/3]

V = 80

n = 100

pi = np.pi

phi = lambda xi, yi: np.sin(i*pi*yi)*np.sinh(i*pi*(1-xi))/(i*np.sinh(i*pi)) 

phi_c = np.array(n)
phi1 = 0
for i in range(1,2*n, 2):
    phi1 = phi(x[0],y[0]) +phi1
phi1 = (4*V/pi)*phi1
phi2 = 0
for i in range(1,2*n, 2):
    phi2 = phi(x[1],y[0]) +phi2
phi2 = (4*V/pi)*phi2
phi3 = 0
for i in range(1,2*n, 2):
    phi3 = phi(x[0],y[1]) +phi3
phi3 = (4*V/pi)*phi3
phi4 = 0
for i in range(1,2*n, 2):
    phi4 = phi(x[1],y[1]) +phi4
phi4 = (4*V/pi)*phi4

print(phi1, phi2, phi3, phi4)

#right
V = 20

chi = lambda xi, yi: np.sin(i*pi*yi)*np.sinh(i*pi*(1-xi))/(i*np.sinh(i*pi)) 

chi4 = 0
for i in range(1,2*n, 2):
    an = (2*i-1)*pi
    chi4 = chi(x[0],y[0]) +chi4
chi4 = (4*V/pi)*chi4
chi3 = 0
for i in range(1,2*n, 2):
    an = (2*i-1)*pi
    chi3 = chi(x[1],y[0]) +chi3
chi3 = (4*V/pi)*chi3
chi2 = 0
for i in range(1,2*n, 2):
    an = (2*i-1)*pi
    chi2 = chi(x[0],y[1]) +chi2
chi2 = (4*V/pi)*chi2
chi1 = 0
for i in range(1,2*n, 2):
    an = (2*i-1)*pi
    chi1 = chi(x[1],y[1]) +chi1
chi1 = (4*V/pi)*chi1

print(chi1, chi2, chi3, chi4)

#Bottom
V = 60

dhi = lambda xi, yi: np.sin(i*pi*yi)*np.sinh(i*pi*(1-xi))/(i*np.sinh(i*pi)) 

dhi2 = 0
for i in range(1,2*n, 2):
    an = (2*i-1)*pi
    dhi2 = dhi(x[0],y[0]) +dhi2
dhi2 = (4*V/pi)*dhi2
dhi4 = 0
for i in range(1,2*n, 2):
    an = (2*i-1)*pi
    dhi4 = dhi(x[1],y[0]) +dhi4
dhi4 = (4*V/pi)*dhi4
dhi1 = 0
for i in range(1,2*n, 2):
    an = (2*i-1)*pi
    dhi1 = dhi(x[0],y[1]) +dhi1
dhi1 = (4*V/pi)*dhi1
dhi3 = 0
for i in range(1,2*n, 2):
    an = (2*i-1)*pi
    dhi3 = dhi(x[1],y[1]) +dhi3
dhi3 = (4*V/pi)*dhi3

print(dhi1, dhi2, dhi3, dhi4)
#top
V=100
mhi = lambda xi, yi: np.sin(i*pi*yi)*np.sinh(i*pi*(1-xi))/(i*np.sinh(i*pi)) 

mhi_c = np.array(n)
mhi3 = 0
for i in range(1,2*n, 2):
    mhi3 = mhi(x[0],y[0]) +mhi3
mhi3 = (4*V/pi)*mhi3
mhi1 = 0
for i in range(1,2*n, 2):
    mhi1 = mhi(x[1],y[0]) +mhi1
mhi1 = (4*V/pi)*mhi1
mhi4 = 0
for i in range(1,2*n, 2):
    mhi4 = mhi(x[0],y[1]) +mhi4
mhi4 = (4*V/pi)*mhi4
mhi2 = 0
for i in range(1,2*n, 2):
    mhi2 = mhi(x[1],y[1]) +mhi2
mhi2 = (4*V/pi)*mhi2

print(mhi1, mhi2, mhi3, mhi4)

sum1 = phi1+chi1+dhi1+mhi1
sum2 = phi2+chi2+dhi2+mhi2
sum3 = phi3+chi3+dhi3+mhi3
sum4 = phi4+chi4+dhi4+mhi4

print('Sum:', sum1, sum2, sum3, sum4)

exp = [65.4, 50.7, 75.2,60.5]

err = [(sum1-exp[0])/exp[0],(sum2-exp[1])/exp[1],(sum3-exp[2])/exp[2],(sum4-exp[3])/exp[3]]
print(err)