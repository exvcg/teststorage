a = input()
dif = 0
if(int(a)<=99):
    print(a)
else:
    count = 99
    for i in range(100,int(a)+1):
        dif = int(str(i)[0])-int(str(i)[1])
        for v in  range(2,len(str(i))):
            if(int(str(i)[v-1])-int(str(i)[v]) != dif):
                break
            count+=1
    print(count)