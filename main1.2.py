#1.2 (var 4)
r=input("введи числа через пробел:") 
s=[float(x) for x in r.split()] 
n=len(s)
i=0
while i<n and s[i]>0:
    i+=1
print("количество положительных чисел в начале:",i)