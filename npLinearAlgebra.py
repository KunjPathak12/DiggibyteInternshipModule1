import numpy as np
dimension = int(input())
myVal =[]
for i in range(dimension):
    elements = input().split()
    for i in elements:
        myVal.append(float(i))
myNewVal = np.array(myVal).reshape(dimension,dimension)
print(round(np.linalg.det(myNewVal),2))
