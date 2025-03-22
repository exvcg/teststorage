# 2805
# def height(c,bottom,top,max):
#     mid= (bottom+top)//2
#     sum = 0
#     for tree in c:
#         if(tree>mid):
#             sum += tree-mid
#     if(sum>max):
#         height(c,mid,top,max)
#     elif(sum<max):
#         height(c,bottom,mid,max)
#     elif(sum == max):
#         print(mid)
a,b = map(int,input().split())
tl = list(map(int,input().split()))
top = max(tl)
bottom = 0
sum = 0
minimum = 0
while bottom<top:
    mid = (top+bottom)//2
    for i in tl:
        if(i>mid):
            sum += i-mid
    if(sum>=b):
        minimum = mid
        sum = 0
        bottom = mid+1
    elif(sum<b):
        sum = 0
        top = mid
print(minimum)
