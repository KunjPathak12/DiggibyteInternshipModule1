# Enter your code here. Read input from STDIN. Print output to STDOUT
myRange = input().split()
happiness = input().split()
myVal = []
myVal1 = input().split()
myVal2 = input().split()
mySet1 = set()
mySet2 = set()
count = 0

for i in range(len(happiness)):
    myVal.append(int(happiness[i]))

for j in range(len(myVal1)):
    mySet1.add(int(myVal1[j]))
    mySet2.add(int(myVal2[j]))

for k in range(len(happiness)):
  if int(happiness[k]) in mySet1:
    count+=1
  elif int(happiness[k]) in mySet2:
    count-=1
  else:
    count += 0

print(count)
