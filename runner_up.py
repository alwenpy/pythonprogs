a=int(input())


c=[]
for i in range (0,a):
    b=int(input())
    c.append(b)
    b=c[i]
    i+=1

c.sort()
print(c[a-2])

