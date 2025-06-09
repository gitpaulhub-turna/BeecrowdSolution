N=int(input())
num=[]
for i in range(N):
    i=int(input())
    num.append(i)
    
#print(num)
for i in num:
    if i<0 and i%2==0:
        print("EVEN NEGATIVE")
    elif i<0 and i%2!=0:
        print("ODD NEGATIVE")
    elif i>0 and i%2==0:
        print("EVEN POSITIVE")
        
    elif i>0 and i%2!=0:
        print("ODD POSITIVE")
    else:
        print("NULL")
    
    
