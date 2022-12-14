# Enter your code here. Read input from STDIN. Print output to STDOUT
cases = int(input())
for i in range(cases):
    n = int(input())
    blocks = list(map(int, input().split()))
    count = 0
    k = 0
    j = 1
    l = n - 1
    # print(blocks1)
    while j < n:
        if blocks[k] >= blocks[j]:
            count += 1
        elif blocks[l] >= blocks[j]:
            count += 1
        j += 1

    if count == (len(blocks) - 1):
        print("Yes")
    else:
        print("No")

    # print(blocks)
    # f=0
    # def divide(blocks,f,n):
    #     mid = (n+f)//2
    #     if blocks[f]==blocks[n-1]:
    #         print("Yes")
    #     else:
    #         while f<n:

    #             if blocks[f]>=blocks[mid] or blocks[n-1]>=blocks[mid]:
    #                 f+=1
    #                 n-=1
    #                 divide(blocks,f,n)
    #             else:
    #                 print("No")
    #                 break
    # divide(blocks,f,n)
