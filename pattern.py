n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        if i%2==0:
            print('*',end='')
        else:
            print("#",end='')    
    for j in range(i+1):
        if i%2==0:
            print('*',end='')
        else:
            print("#",end='')
        
    print()

n=5
for i in range(n,0,-1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(1,i):
        if i%2==0:
            print('*',end='')
        else:
            print("#",end='')    
    for j in range(i+1):
        if i%2==0:
            print('*',end='')
        else:
            print("#",end='')
        
    print()
    