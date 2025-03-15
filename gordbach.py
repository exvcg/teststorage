prime = []
for num in range(10001):
    for c in range(2,num+1):
        if(num%c == 0):
            if(num == c):
                prime.append(c)
            break
a = int(input())
lis = []
for bn in range(a):
    b = int(input())
    dif = 0
    mid = b//2
    big = 0
    for i in range(len(prime)):
        if (prime[i]>=mid):
            big = prime[i]
            dif = b - big
            if(dif in prime):        
                lis.append([dif,big])
                break
for i in lis:
    print(f'{i[0]} {i[1]}')