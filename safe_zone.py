# zone = []
# max = 0
# xmove = [-1,1,0,0]
# ymove = [0,0,1,-1]
# top = 0
# count = 0
# def check(x,y,heig):#하나의 구역 찾기
#     global sink
#     sink[x][y] = True
#     for m in range(4):#상하좌우 전부
#         ndx = x + xmove[m]
#         ndy = y + ymove[m]
#         if ((0<=ndx<a) and (0<=ndy<a) and (sink[ndx][ndy] == False) and (zone[ndx][ndy]>heig)):
#             check(ndx,ndy,heig)
# a = int(input())
# sink = [[False]*a for _ in range(a)]
# for a1 in range(a):
#     c = list(map(int,input().split(" ")))
#     zone.append(c)
#     for i in c:
#         if(i>top):
#             top = i
# for hei in range(1,top):
#     count = 0
#     for x in range(a):#잠긴곳 찾기
#         for y in range(a):
#             if zone[x][y]<=hei:
#                 sink[x][y] = True
#             if(sink[x][y] == False and zone[x][y]>hei):
#                 check(x,y,hei)
#                 count+=1
#     if(count>max):
#         max = count
#     sink = [[False]*a for _ in range(a)]
    
# print(max)
#리커전예러 발생
# zone = []
# max = 0
# xmove = [-1,1,0,0]
# ymove = [0,0,1,-1]
# top = 0
# count = 0
# def check(x,y,heig):#하나의 구역 찾기
#     global sink
#     sink[x][y] = True
#     gh = [(x,y)]
#     while gh:
#         x,y = gh.pop()
#         for m in range(4):#상하좌우 전부
#             ndx = x + xmove[m]
#             ndy = y + ymove[m]
#             if ((0<=ndx<a) and (0<=ndy<a) and (sink[ndx][ndy] == False) and (zone[ndx][ndy]>heig)):
#                 sink[ndx][ndy] = True
#                 gh.append((ndx,ndy))
# a = int(input())
# sink = [[False]*a for _ in range(a)]
# for a1 in range(a):
#     c = list(map(int,input().split(" ")))
#     zone.append(c)
#     for i in c:
#         if(i>top):
#             top = i
# for hei in range(1,top):
#     count = 0
#     for x in range(a):#잠긴곳 찾기
#         for y in range(a):
#             if zone[x][y]<=hei:
#                 sink[x][y] = True
#             if(sink[x][y] == False and zone[x][y]>hei):
#                 check(x,y,hei)
#                 count+=1
#     if(count>max):
#         max = count
#     sink = [[False]*a for _ in range(a)]   
# print(max)
zone = []
max = 0
xmove = [-1,1,0,0]
ymove = [0,0,1,-1]
top = 0
count = 0
def check(x,y,heig):#하나의 구역 찾기
    global sink
    sink[x][y] = True
    gh = [(x,y)]
    while gh:
        x,y = gh.pop()
        for m in range(4):#상하좌우 전부
            ndx = x + xmove[m]
            ndy = y + ymove[m]
            if (0<=ndx<a and 0<=ndy<a and sink[ndx][ndy] == False and zone[ndx][ndy]>heig):
                sink[ndx][ndy] = True
                gh.append((ndx,ndy))
a = int(input())
sink = [[False]*a for _ in range(a)]
for a1 in range(a):
    c = list(map(int,input().split(" ")))
    zone.append(c)
    for i in c:
        if(i>top):
            top = i
for hei in range(top):
    count = 0
    for x in range(a):#잠긴곳 찾기
        for y in range(a):
            if zone[x][y]<=hei:
                sink[x][y] = True
            if(sink[x][y] == False and zone[x][y]>hei):
                check(x,y,hei)
                count+=1
    if(count>max):
        max = count
    sink = [[False]*a for _ in range(a)]   
print(max)