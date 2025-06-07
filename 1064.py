count=0
total=0.0

for i in range (6):
    val=float(input())
    if val>0:
        count+=1
        total+=val
average=total/count
print(f"{count} valores positivos")
print(f"{average:.1f}")


    
