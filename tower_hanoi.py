def move(a,b,c,d):#갯수,출발지,목적지,경유지
    if(a == 1):#옮겨야될 게 1개라면
        return print(b,c,sep=" ")
    move(a-1,b,d,c)#위에있는걸 전부 경유지로 옮기고
    print(b,c,sep=" ")
    move(a-1,d,c,b)#겨유지에있는걸 전부 목적지로
    
a = int(input())
print((2**a)-1)
if(a <= 20):
    move(a,1,3,2)