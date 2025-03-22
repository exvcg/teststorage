#1629
# def dum(x,y,z):#a,c,지수
#     if(z == 1):
#         return x%y
#     else:
#         return (dum(x,y,z//2)*dum(x,y,z-z//2))%y
# import sys
# input = sys.stdin.readline
# a,b,c = map(int,input().split())

# p = dum(a,c,b)
# print(p)
#시간초과
#지수법칙 (a*b)%c = (a%c)*(b%c)%c
def dum(x,y,z):#a,c,지수
    if(z == 1):
        return x%y
    else:
        min = dum(x,y,z//2)
        if(z%2==0):
            return (min)*(min)%c
        else:
            return (min)*((min*x))%c
import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())

p = dum(a,c,b)
print(p)
