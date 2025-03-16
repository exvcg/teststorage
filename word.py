a = input()
b = a.lstrip(" ").rstrip(" ")
if(b == ""):
    print(0)
else:
    c = b.split(" ")
print(len(c))