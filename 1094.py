N=int(input())
C=0
R=0
S=0
T=0

for i in range(N):
    quantity,animal=input().split()
    quantity=int(quantity)
    T+=quantity

    if animal=='C':
        C+=quantity
    elif animal=='R':
        R+=quantity
    elif animal=='S':
        S+=quantity
    
per_c=(C/T)*100
per_r=(R/T)*100
per_s=(S/T)*100

print(f"Total: {T} cobaias")
print(f"Total de coelhos: {C}")
print(f"Total de ratos: {R}")
print(f"Total de sapos: {S}")
print(f"Percentual de coelhos: {per_c:.2f} %")
print(f"Percentual de ratos: {per_r:.2f} %")
print(f"Percentual de sapos: {per_s:.2f} %")




