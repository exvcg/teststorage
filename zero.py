a = int(input())
b=[]
for bn in range(a):
    c = input()
    if(c == "top"):
        if(len(b) == 0):
            print(-1)
        else:
            print(b[-1])
    if(c == "empty"):
        if(len(b) == 0):
            print(1)
        else:
            print(0)
    if(c == "size"):
        print(len(b))
    if(c == "pop"):
        if(len(b) == 0):
            print(-1)
        else:
            print(b[-1])
            b.pop()
    if("push" in c):
        v = int(c.split()[1])
        b.append(v)