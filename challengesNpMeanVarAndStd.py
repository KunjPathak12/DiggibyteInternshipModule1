import numpy as np

mVal = input().split()
r = int(mVal[0])
c = int(mVal[1])
newList = []

for i in range(r):
    eleList = input().split()
    for i in eleList:
        newList.append(int(i))
myVar = np.array(newList).reshape(r,c)
print(np.mean(myVar, axis=1))
print(np.var(myVar, axis=0))
print(round(np.std(myVar), 11))