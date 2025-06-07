count_even=0
count_odd=0
count_positive=0
count_negative=0

for i in range(5):
    num=int(input())
    if num>0:
     count_positive+=1
    if num<0:
        count_negative+=1
    if num%2==0:
        count_even+=1
    else:
        count_odd+=1
       
       
       

        
print(f"{count_even} valor(es) par(es)")
print(f"{count_odd} valor(es) impar(es)")
print(f"{count_positive} valor(es) positivo(s)")
print(f"{count_negative} valor(es) negativo(s)")
