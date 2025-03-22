#2480
a = list(map(int,input().split()))
b = [0]*6 
max = 0
count = 0
for i in range(3):
    b[a[i]-1] += 1
for v in range(len(b)):
    if(b[v]>=count):
        max = v+1
        count = b[v]
if(count == 3):
    print(10000+max*1000)
elif(count == 2):
    print(1000+max*100)
else:
    print(max*100)