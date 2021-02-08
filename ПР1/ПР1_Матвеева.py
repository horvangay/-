#Задание  1.
a = int(input())
b = int(input())
a, b = b, a
print (a, b)

#Задание 2.
a = input()
print(sum(map(int,str(a))))

#Задание 3.
try:
    a = float(input())
    b = float(input())
    с = float(input())
    d = ( b**2 -4*a*с)
    if d > 0:
        x1 = (-b - d**0.5)/(2*a)
        x2 = (-b + d**0.5)/(2*a)
        if x1 > x2:
            print(x1,x2)
        else:
            print(x2,x1)
    elif d == 0:
        print (-b/(2*a))
    else:
        print ("Нет корней")
except ZeroDivisionError:
    print ("Error")

