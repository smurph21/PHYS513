#HW3
#problem 3_2

import numpy as np

n = 4
x = np.zeros([n,n])

x[1,0] = 80
x[2,0] = 80

for i in range(1,3):
    for j in range(1,3):
        x[i,j] = 20
print(x)
for n in range(5):
    for i in range(1,3):
        for j in range(1,3):
            x[i,j] = (x[i+1,j]+x[i-1,j]+x[i,j+1]+x[i,j-1])/4
    print(n)
    print(x)
print(x)