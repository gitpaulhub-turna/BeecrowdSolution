salary=float(input())
if salary<=2000:
    print("Isento")
elif 2000<salary<=3000:
    res=(salary-2000)*0.08
    print(f"R$ {res:.2f}")
elif 3000<salary<=4500:
    res=(1000*.08)+(salary -3000)*0.18
    print(f"R$ {res:.2f}")
else:
    res=(1000*0.08)+(1500*0.18)+(salary-4500)*0.28
    print(f"R$ {res:.2f}")
