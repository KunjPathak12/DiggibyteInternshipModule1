myDict = {}
n = int(input())
for i in range(n):
    e = input()
    if e in myDict.keys():
        myDict[e]+=1
    else:
        myDict[e]=1
print(len(myDict))
# myList=myDict.values()
# string = ""
for i,j in myDict.items():
    print(j,end=" ")
