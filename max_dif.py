def bf(h,leng,t):
    global check
    global nums
    global max
    curent = 0
    global cmax
    check[h] = True
    for m in range(leng):
        if(check[m] == True):
            continue
        curent = abs(nums[h]-nums[m])
        cmax += curent
        bf(m,leng,curent)
    if(cmax>max):
        max = cmax
    cmax = cmax-t
    check[h] = False
a= int(input())
nums = [0]*a
check = [False]*a
max = 0
cmax = 0
b = list(map(int,input().split(" ")))
for i in range(a):
    nums[i]=b[i]
for i in range(a):
    bf(i,a,0)
print(max)


        