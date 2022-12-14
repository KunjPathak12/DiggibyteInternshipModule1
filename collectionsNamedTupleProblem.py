from collections import namedtuple

n = int(input())
myTuple = namedtuple("Students", input())
Sum = 0
for i in range(n):
    student = myTuple._make(input().split())
    Sum += float(student.MARKS)

print("%.2f" % (Sum / n))