# def root(start,count,first):#현재위치 총도시수 출발점
#     global city
#     global check
#     global dis
#     global short
#     check[start] = True
#     if(False not in check):
#             short += city[start][first]
#             if(dis>short):
#                 dis = short
#             short -= city[start][first]

#     for i in range(count):
#         if(check[i] == True or city[start][i] == 0):
#             continue
#         short += city[start][i]
#         root(i,count,first)
#         short -= city[start][i]
#     check[start] = False
# a = int(input())
# city = []
# dis = 4000001
# short = 0
# check = [False]*a
# for i in range(a):
#     b = list(map(int,input().split(" ")))
#     city.append(b)
# for i in range(a):
#     root(i,a,i)
# print(dis)
import sys


def root(start,count,first):#현재위치 총도시수 출발점
    global city
    global check
    global dis
    global short
    check[start] = True # 방문
    if(False not in check): #전부다 방문 했으면
        if city[start][first] > 0: #경로가 있다면
            short += city[start][first]#마지막에서 처음 시작하는 도시로 이동
            if(dis>short):
                dis = short
            short -= city[start][first]#그 전으로
    for i in range(count):
        if(check[i] == True or city[start][i] == 0):# 들렸거나 길이 없다면 스킵
            continue
        short += city[start][i]#시작지점이 아닌 다른곳으로
        root(i,count,first)
        short -= city[start][i]
    check[start] = False #전으로 돌아가기
a = int(input())
city = []#도시의 가중치
dis = sys.maxsize
short = 0
check = [False]*a#들렀는지 여부 표시
for i in range(a):# 각 가중치받기
    b = list(map(int,input().split(" ")))
    city.append(b)
for i in range(a):
    root(i,a,i)
print(dis)