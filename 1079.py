N=int(input())
A=[]
for i in range(N):
    B,C,D=list(map(float, input().split()))
    b=B*2
    c=C*3
    d=D*5
    average=((b+c+d)/10)
    
    A.append(f"{average:.1f}")

for i in A:
    print(i)

