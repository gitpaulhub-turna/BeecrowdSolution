age=int(input())
years=age//365
print(f"{years} ano(s)")
month=(age%365)//30
print(f"{month} mes(es)")
day=(age%365)%30
print(f"{day} dia(s)")
