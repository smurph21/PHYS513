#HW12

import matplotlib.pyplot as plt
import numpy as np
pi = np.pi
i = 1j
N = 1000

Z = np.ndarray(N, dtype=np.complex128)
I = np.ndarray(N, dtype=np.complex128)
V = np.ndarray(N, dtype=np.complex128)
#part 1 inputs

d = 0.5
L = 1/d/N
C = 1/d/N
w = 1
Z0 = 1
Zl = 3*Z0
print(L)

#build Z array
Z[0] = Zl
for j in range(1,N):
    y = 1/(Z[j-1]+i*w*L)
    Z[j] = 1/(y+i*w*C)
    

#Z_array[-1] = Z_array[-1] - i*w*L
#flip array
Z = Z[::-1]
print(Z)

#build I and V
V[0] = 1
I[0] = V[0]/Z[0]

for j in range(1,N):
    I[j] = I[j-1]-i*w*C*V[j-1]
    V[j] = V[j-1] - i*w*L*I[j]

print(Z)
print(I)
print(V)

#plotting HW11 solution

x = np.linspace(0,d,N)

V0_11 = (2/3)*(5/4+np.cos(8*pi*x))**0.5

plt.title('Comparison')
plt.xlabel('X')
plt.ylabel('V')
plt.plot(x,V0_11, 'g')
plt.plot(x,abs(V), 'b')
plt.show()
print("done")


