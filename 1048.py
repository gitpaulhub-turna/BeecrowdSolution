def salary_adjustment(salary):
    if salary<=400.00 :
        percentage=15
    elif salary<=800.00:
        percentage=12
    elif salary<=1200.00:
        percentage=10
    elif salary<=2000.00:
        percentage=7
    else :
        percentage=4
    Bonus=salary*(percentage/100)
    new_salary=salary+Bonus
    return new_salary,Bonus,percentage

salary=float(input())
new_salary,Bonus,percentage=salary_adjustment(salary)
print(f"Novo salario: {new_salary:.2f}")
print(f"Reajuste ganho: {Bonus:.2f}")
print(f"Em percentual: {percentage} %")

