def xb(n, a, b):
    if n==1:
        print(n, a, b)  #Тогда перемещаем n с a на b
    else:
        tmp = (6-a-b)
        xb(n-1, a, tmp)  #Перемещаем все диски кроме большого на 2
        print(n, a, b)
        xb(n-1, tmp, b)  #Перемещаем сотавшийся диск на 3
n=int(input())
xb(n, 1, 3)