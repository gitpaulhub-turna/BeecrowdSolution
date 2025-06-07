a=int(input())
if a%2==0:
    for i in range(a+1,a+12,2):
        print(i)
else:
    for i in range(a,a+11,2):
        print(i)
