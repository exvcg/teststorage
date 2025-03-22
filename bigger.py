# import sys
# input = sys.stdin.readline
# a,b = map(int,input().split())
# c = int(input())
# d = []
# solve = 0
# count = 0
# for vi in range(a):
#     d.append(c%10)
#     c = c//10

# for i in reversed(range(len(d))):
#     if(i == 0):
#         del d[i]
#         count+=1
#         if(count == b):
#             break
#     else:
#         if(d[i]<d[i-1]):
#             del d[i]
#             count +=1
#             if(count == b):
#                 break
# for bn in reversed(d):
#     print(bn,end ="")
#시간 초과
#그리디 알고리즘:가장 큰것부터 넣을것
#스택 앞자리부터 넣고 그 다음에 들어올것 보다 작으면 pop
# import sys
# input = sys.stdin.readline
a,b = map(int,input().split())
c = list(input())
d = []
for pp in c:
    while d and d[-1]<pp and b>0:
        d.pop()
        b-=1
    d.append(pp)
print(d)
if(b>0):
    print(''.join(d[:-b]))
else:
    print(''.join(d))
# print()
# for i in range(len(d)):
#     solve += d[i]*10**(a-b-i)
# print(solve)
    

