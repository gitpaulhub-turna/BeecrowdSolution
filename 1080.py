max_value=-1
position=0

for i in range(100):
    num=int(input())
    if num>max_value:
        max_value=num
        position=i+1

print(max_value)
print(position)
