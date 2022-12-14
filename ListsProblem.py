if __name__ == '__main__':
    N = int(input())
    myList = []
    for i in range (N):
        myVal = input().split()
        command = myVal[0]
        if command == "insert":
            myList.insert(int(myVal[1]),int(myVal[2]))

        elif command == "remove":
            myList.remove(int(myVal[1]))

        elif command == "append":
            myList.append(int(myVal[1]))
        elif command == "sort":
            myList.sort()
        elif command == "reverse":
            myList.reverse()
        elif command == "pop":
            myList.pop()
        else:
            print(myList)
