p1,unit,unit_price=map(float,input().split())
p2,unit2,unit_price2=map(float,input().split())
operation=(unit*unit_price)+(unit2*unit_price2)

print(f"VALOR A PAGAR: R$ {operation:.2f}")
