import datetime
myList = list(input().split())
var = datetime.datetime(int(myList[2]),int(myList[0]),int(myList[1]))
print(var.strftime("%A").upper())
