import sys
from collections import deque
input = sys.stdin.readline
deq = deque()
x, y = map(int,input().split())
for i in range(1,x+1):
    deq.append(i)
print("<",end = "")
while len(deq)>0:
    deq.rotate(-y+1)
    if(len(deq) == 1):
        print(deq.popleft(),end="")
        continue
    print(deq.popleft(),end=", ")
print(">")