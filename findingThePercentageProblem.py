if __name__ == '__main__':
    n = int(input())
    SUM = 0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for keys, values in student_marks.items():
        if query_name == keys:
            myList = values

    for i in myList:
        SUM += i
    Avg = SUM / len(myList)
    print("%.2f" % Avg)
