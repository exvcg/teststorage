#8983
#대각선 이용 N_QUEEN 참조
import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())
d = list(map(int,input().split()))
check = [False]*b
animal= [0]*b
for m in range(b):
    ani = tuple(map(int,input().split()))
    animal[m] = ani
for i in range(a):
    for an in animal:
        if(an[0]+an[1]<=d[i]+c and an[0]-an[1]>=d[i]-c and check[animal.index(an)] == False):
            check[animal.index(an)] = True
print(check.count(True))