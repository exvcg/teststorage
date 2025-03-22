import sys
from collections import deque
input = sys.stdin.readline
a = int(input())
deq = deque()
for i in range(1,a+1):
    deq.append(i)
while len(deq)>1:
    deq.popleft()
    deq.rotate(-1)

print(deq[0])