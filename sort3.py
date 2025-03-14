#1차시도
# a = int(input())
# num = []
# for i in range(a):
#     b = int(input())
#     if (len(num) == 0):
#         num.append(b)
#         continue
#     for mn in range(len(num)):
#         if(b<=num[mn]):
#             num.insert(mn,b)
#             break
#         if(mn == len(num)-1):
#             num.append(b)

# for bv in num:
#     print(bv)
#성공케이스
import sys
# 여러 줄 입력을 받아들인다.
input = sys.stdin.readline
lis = [0]*10001
for a in range(int(input())):
    lis[int(input())] += 1
for i in range(10001):
    if(lis[i] != 0):
       for a in range(lis[i]):
           print(i)