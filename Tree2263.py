#2263번
# def tree(a,b):#포스트오더 인오더
#     root = a[-1]#중심은 포스트오더의 맨 끝
#     inorder = b.index(root)#인오더에서 중심 찾기
#     prelist.append(root)#중심추가
#     if(inorder<=len(b)-1):#인오더에서 끝이 아니라면
#         inoderleft = b[:inorder]#왼쪽구하기
#         leftlen = len(inoderleft)#왼쪽길이
#         if(leftlen>0):
#             postleft = a[:leftlen]#포스트에서 왼쪽구하기
#             tree(postleft,inoderleft)
#     if(inorder>=0):#인오더에서 시작이아니라면
#         inorderright = b[inorder+1:]#오른쪽구하기
#         rightlen = len(inorderright)#오른쪽길이
#         if(rightlen>0):
#             postright = a[leftlen:-1]#포스트에서 오른쪽 구하기
#             tree(postright,inorderright)
# y = int(input())
# prelist = []
# i = list(map(int,input().split()))
# p = list(map(int,input().split()))

# tree(p,i)
# for mn in prelist:
#     print(mn,end=" ")
#메모리 초과 발생
#인덱스만 있으면 원하는 위치의 값을 가져올 수 있음 그러면 매개변수로 인덱스를 받게 구현
#슬라이싱을 사용하면 메모리 증가

# def tree(a,b,c,d):#인오더의 처음과끝 인덱스 포스트오더의 처음과 끝인덱스
#     if(b<a):
#         return
#     global i#인오더 배열
#     global p#포스트오더 배열
#     root = p[d]#중심은 포스트오더의 맨 끝
#     inorder = i.index(root)#인오더에서 중심 찾기
#     #왼쪽의 길이 
#     leftlen = inorder-a
#     print(root ,end= " ")#중심출력
#     tree(a,inorder-1,c,c+leftlen-1)#왼쪽
#     tree(inorder+1,b,c+leftlen,d-1)#오른쪽
# y = int(input())
# i = list(map(int,input().split()))
# p = list(map(int,input().split()))

# tree(0,y-1,0,y-1)
#리커전에러 
import sys
sys.setrecursionlimit(10**6)
def tree(a,b,c,d):#인오더의 처음과끝 인덱스 포스트오더의 처음과 끝인덱스
    if(b<a):
        return
    global i#인오더 배열
    global p#포스트오더 배열
    root = p[d]#중심은 포스트오더의 맨 끝
    inorder = in_order_index[root]#인오더에서 중심 찾기
    #왼쪽의 길이 
    leftlen = inorder-a
    print(root ,end= " ")#중심출력
    tree(a,inorder-1,c,c+leftlen-1)#왼쪽
    tree(inorder+1,b,c+leftlen,d-1)#오른쪽
y = int(input())
i = list(map(int,input().split()))
p = list(map(int,input().split()))
in_order_index = {value: index for index, value in enumerate(i)}
tree(0,y-1,0,y-1)



    