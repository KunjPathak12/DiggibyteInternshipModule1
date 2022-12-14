def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        m = string[i:i+k]
        ans = ""
        for j in m:
          if j not in ans:
            ans+=j
        print(ans)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)