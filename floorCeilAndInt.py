import numpy as  np
np.set_printoptions(legacy="1.13")

myList = input().split()
newList = []
for i in range(len(myList)):
    newList.append(float(myList[i]))

np.array(newList)
print(np.floor(newList))
print(np.ceil(newList))
print(np.rint(newList))
