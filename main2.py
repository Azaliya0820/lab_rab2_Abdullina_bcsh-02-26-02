#2 (var 4)
s=input()
s1=''
c= 0
for i in range(len(s)):
    if s[i]=='а' or s[i]=='А':
        s1+='о' if s[i]=='а' else 'О'
        c += 1
    else:
        s1+=s[i]
print('Количество замен:',c)
print('Всего символов в строке:',len(s))

