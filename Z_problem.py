from math import*

#리커전 발생
# x = 0
# def Zsearch(a,b,c):#제곱수,가로,세로
#     global x
#     if(2**(a-1)>b and 2**(a-1)>c):#
#         Zsearch(a-1,b,c)
#     elif(2**(a-1)<b and 2**(a-1)>c):
#         x += (2**(a-1))**2
#         Zsearch(a-1,b-a+1,c)
#     elif(2**(a-1)>b and 2**(a-1)<c):
#         x += 2*((2**(a-1))**2)
#         Zsearch(a-1,b,c-a+1)
#     elif(2**(a-1)<b and 2**(a-1)<c):
#         x += 3*((2**(a-1))**2)
#         Zsearch(a-1,b-a+1,c-a+1)
# g = list(map(int,input().split(" ")))
# Zsearch(g[0],g[1],g[2])
# print(x)

x = 0

def Zsearch(a,b,c):#제곱수,가로,세로
    global x
    check = [(False,False)]*(a)
    for i in reversed(range(a)):
        if(2**i<b+1):
            if(2**i<c+1):
                check[i] = (True,True)
                c = c-2**i
            else:
                check[i] = (True,False)
            b = b - 2**i
        if(2**i<c+1):
            if(2**i>b):
                check[i] = (False,True)
                c = c-2**i
    for ck in reversed(range(a)):
        if(check[ck] == (True,True)):
            p = 3*((2**(ck))**2)
            x += p
        elif(check[ck] == (False,True)):
            p = 2*((2**(ck))**2)
            x += p
        elif(check[ck] == (True,False)):
            p = ((2**(ck))**2)
            x += p
g = list(map(int,input().split(" ")))
Zsearch(g[0],g[2],g[1])
print(x)