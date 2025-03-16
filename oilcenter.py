#기름값이 가장 적은 구간에서 나머지를 다채움
a = int(input())
b = list(map(int,input().split()))#거리
c = list(map(int,input().split()))#도시당 기름 가격
min = 10001
data = []
count = 0
cost = 0
for mn in range(len(b)):
    count += b[mn]
    if (c[mn]<min):
        data.append((c[mn],b[mn]))
        min = c[mn]
        count = 0
data.append((min,count))
for i in data:
    cost += i[0]*i[1]
print(cost)
        
