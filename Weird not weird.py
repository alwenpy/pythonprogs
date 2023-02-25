

num=int(input("Number daalo"))

if num %2 != 0 or num in range(6,20):
    print("Weird")
    
elif num % 2 == 0  or num in range(2,5) or num> 20:
    print("Not Weird")
   