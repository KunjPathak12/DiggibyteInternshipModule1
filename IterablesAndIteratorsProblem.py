from itertools import combinations
n = int(input())
strArr = input().split()
indices = int(input())
myArr = sorted(list(combinations(strArr,indices)))
count=0
for i in myArr:
    if "a" in i:
        count+=1
print("%.3f"%(count/len(myArr)))
#     for j in range (n):
#         if(j>i):
#             myArr.append(tuple(set((strArr[i],strArr[j]))))
# # print(myArr)
# for i in myArr:
#     if "a" in i:
#         count+=1
# print("%.3f" %(count/len(myArr)))
