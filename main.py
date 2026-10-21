import math
print("Расчёт расхода жидкости через сечение трубопровода")
print("1—круглое сечение")
print("2—прямоугольное сечение")
print("3—кольцевое сечение")

choice=""
while choice not in ["1","2","3"]:
    choice=input("Выберите тип сечения(1-3):")
    if choice not in ["1","2","3"]:
        print("Ошибка:введите 1,2 или 3")
A=0.0
section_name=""
if choice=="1":
    section_name="круглое"
    f_i= False
    while not f_i:
        try:
            d=float(input("Введите диаметр d,мм(5..500):"))
            if 5<=d<=500:
                f_i=True
            else:
                print("Значение должно быть от 5 до 500 мм")
        except ValueError:
            print("Введите число")
    d_m=d/1000
    A=math.pi*d_m*d_m/4

elif choice=="2":
    section_name="прямоугольное"
    
    f_a=False
    while not f_a:
        try:
            a=float(input("Введите сторону a,мм(5..500):"))
            if 5<=a<=500:
                f_a=True
            else:
                print("Значение должно быть от 5 до 500 мм")
        except ValueError:
            print("Введите число")

    f_b=False
    while not f_b:
        try:
            b=float(input("Введите сторону b,мм(5..500):"))
            if 5<=b<=500:
                f_b=True
            else:
                print("Значение должно быть от 5 до 500 мм")
        except ValueError:
            print("Введите число")
    A=(a/1000)*(b/1000)

elif choice=="3":
    section_name="кольцевое"
    f_d=False
    while not f_d:
        try:
            D=float(input("Введите внешний диаметр D,мм(5..500):"))
            d=float(input("Введите внутренний диаметр d,мм(меньше D):"))
            if not(5<=D<=500 and 5<=d<=500):
                print("Диаметры должны быть в диапазоне 5–500мм")
                continue
            if d>=D:
                print("Внутренний диаметр d должен быть меньше внешнего D")
                continue
            f_d=True
        except ValueError:
            print("Введите числа")

    A=math.pi*((D/1000)**2-(d/1000)**2)/4

f_v = False
while not f_v:
    try:
        v=float(input("Введите скорость потока v,м/с(0.1..10):"))
        if 0.1<=v<=10:
            f_v=True
        else:
            print("Скорость должна быть от 0.1 до 10 м/с")
    except ValueError:
        print("Введите число")
Q=A*v*3600
print("Тип сечения:",section_name)
print("Площадь сечения:",round(A,6),"м2")
print("Расход жидкости Q:",round(Q,4),"м3/ч")
