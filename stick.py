a = int(input())
c = []
max = 0
count = 0
for v in range(a):
    b = int(input())
    c.append(b)
for mn in range(a):
    p = c.pop()
    if(p > max):
        max = p
        count += 1
print(count)
