#로프를 전부 사용안해도 됨 두꺼운것부터 쓰다가 최대치가 낮아지면 끝
a = int(input())
c=[]
max = 0
for i in range(a):
    b = int(input())
    c.append(b)
c.sort(reverse=True)
for v in range(len(c)):
    if(max<c[v]*(v+1)):
        max = c[v]*(v+1)
        
print(max)






    
    