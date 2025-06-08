X=int(input())
Y=int(input())

sum=0
for i in range (Y+1,X,1):
    #print(i)
    if i%2!=0:
        sum+=i
    
print(sum)
