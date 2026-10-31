#3.1 (var 4)
a=list(map(float, input("Введите числа через пробел:").split()))
i_max=0          
m=a[0]   
for i in range(2,len(a)):
    if a[i]>m:
        m=a[i]
        i_max=i
print("Максимум:",m)
print("Порядковый номер:",i_max+1)

