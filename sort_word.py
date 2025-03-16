a = int(input())
c = [""]*a
for i in range(a):
    b = input()
    c[i] = b
c = list(set(c))
c.sort()
c.sort(key=len)
for v in c:
    print(v)
    