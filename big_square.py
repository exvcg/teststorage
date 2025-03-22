# import sys
# input = sys.stdin.readline
# def segtree(start,end,segm,index):#시작점,끝점,배열,인덱스
#     global a
#     if(start == end):
#         segm[index]=a[start]
#         if(a[start] == bottom):
#             bottoms.append(start)
#         return segm[index]
#     mid = (start+end)//2
#     segm[index] = min(segtree(start,mid,segm,index*2),segtree(mid+1,end,b,index*2+1))
#     return segm[index]
# def height(start,end,left,right,index):
#     global b
#     if left > end or right < start:
#         return sys.maxsize
#     if left <= start and right >= end:
#         return b[index]
#     mid = (start + end) // 2
#     return min(height(start, mid, left,right,index*2) , height(mid+1,end, left,right,index*2+1))
# while 1:
#     c = input().rstrip()
#     if(c == '0'):
#         break
#     a = list(map(int,c.split()))
#     b = [0]*(a[0]*4)#최솟값을 저장할 트리
#     bottom = min(a[1:])
#     max = a[0]*bottom
#     bottoms=[]
#     segtree(1,a[0],b,1)
#     for v in range(len(bottoms)):
#         if(v == 0):
#             area = height(1,a[0],1,bottoms[v]-1,1)*(bottoms[v]-1)
#         else:
#             area = height(1,a[0],bottoms[v-1]+1,bottoms[v]-1,1)*(bottoms[v]-bottoms[v-1]-1)
#         if(area>max):
#             max = area
#     print(max)
# import sys
# input = sys.stdin.readline
# def segtree(start,end,segm,index):#시작점,끝점,배열,인덱스
#     global a
#     if(start == end):
#         segm[index]=a[start]
#         if(a[start] == bottom):
#             bottoms.append(start)
#         return segm[index]
#     mid = (start+end)//2
#     segm[index] = min(segtree(start,mid,segm,index*2),segtree(mid+1,end,b,index*2+1))
#     return segm[index]
# def height(start,end,left,right,index):
#     global b
#     if left > end or right < start:
#         return sys.maxsize
#     if left <= start and right >= end:
#         return b[index]
#     mid = (start + end) // 2
#     return min(height(start, mid, left,right,index*2) , height(mid+1,end, left,right,index*2+1))

# while 1:
#     c = input().rstrip()
#     if (c == "0"):
#         break
#     a = list(map(int,c.split()))
#     b = [0]*(a[0]*4)#최솟값을 저장할 트리
#     bottom = min(a[1:])
#     p = []
#     p.append(a[0]*bottom)
#     bottoms=[]
#     segtree(1,a[0],b,1)
#     bottoms.append(a[0]+1)
#     for v in range(len(bottoms)):
#         if(v == 0):
#             for i in range(1,bottoms[v]):
#                 area = height(1,a[0],1,i,1)*(bottoms[v]-i)
#                 p.append(area)
#         else:
#             for i in range(bottoms[v-1] + 1,bottoms[v]):
#                 area = height(1,a[0],bottoms[v-1]+1,i,1)*(i-bottoms[v-1])
#                 p.append(area)
#     print(max(p))
from math import log2
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def segtree(start,end,index):#시작점,끝점,배열,인덱스
    global a
    if(start == end):
        b[index]=start
        return 
    mid = (start+end)//2
    segtree(start,mid,index*2)
    segtree(mid+1,end,index*2+1)
    if(a[b[index*2]]>a[b[index*2+1]]):
        b[index] = b[index*2+1]
    else:
        b[index] = b[index*2]
def ind(start,end,left,right,index):
    if right < start or end < left:
        return -1
    if left <= start and end <= right:
        return b[index]
    mid = (start + end) // 2
    lef = ind(start,mid,left,right,index*2)
    righ = ind(mid+1,end,left,right,index*2+1)
    if lef == -1 or righ == -1:
        return max(lef, righ)
    if(a[lef]>a[righ]):
        return righ
    else:
        return lef
def area(left,right):
    place = ind(1,a[0],left,right,1)
    areas = [(right-left+1)*a[place]]
    if(place-1>=left):
        areas.append(area(left,place-1))
    if(place+1<=right):
        areas.append(area(place+1,right))
    return max(areas)

while 1:
    c = list(map(int,input().split()))
    if (c[0] == 0):
        break
    b = [0]*(c[0]*(2**int(log2(c[0])+1)))#최솟값을 저장할 트리
    bottom = min(c[1:])
    segtree(1,c[0],1)
    print(area(1,c[0]))
