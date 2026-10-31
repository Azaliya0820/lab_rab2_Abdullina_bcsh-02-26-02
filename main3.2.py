#3.2 (var 4)
a=list(map(int,input("Введите числа через пробел:").split()))
b=[]
for i in range(len(a)):
    if a[i]%2!=0:
        b.append(a[i])
if b:
    print('Получившийся массив:',b)
else:
    print('Нечётных чисел нет')
