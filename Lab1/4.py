def nod(a,b):
    c = 1
    if a<b:
        c = a
        a = b
        b = c
        c = 1
    for i in range(1,a):
        if a % i == 0 and b % i == 0:
            c = i
    return c

print ("ax+by=c")
print ("Введите a:")
a = int(input())
print ("Введите b:")
b = int(input())
print ("Введите c:")
c = int(input())

x=0
x1 = 0
y=0
y1 = 0
xf=""
yf=""
res = ""

if c%nod(a,b) == 0:
    while a*x+b*y<=c or a*x1+b*y<=c or a*x+b*y1<=c or a*x1+b*y1<=c:
        x+=1
        x1-=1
        
        while a*x+b*y<=c or a*x1+b*y<=c or a*x+b*y1<=c or a*x1+b*y1<=c:
            y+=1
            y1-=1
            if a*x+b*y==c:
                xf = "x = (" + str(x) + ") + (" + str(c) + ")*k"
                yf = "y = (" + str(y) + ") - (" + str(a) + ")*k"
                res = str(a) + " * " + str(x) + " + " + str(b) + " * " + str(y) + " = " + str(c)
                break;
            elif a*x+b*y1==c:
                xf = "x = (" + str(x) + ") + (" + str(c) + ")*k"
                yf = "y = (" + str(y1) + ") - (" + str(a) + ")*k"
                res = str(a) + " * " + str(x) + " + " + str(b) + " * " + str(y1) + " = " + str(c)
                break;
            elif a*x1+b*y==c:
                xf = "x = (" + str(x1) + ") + (" + str(c) + ")*k"
                yf = "y = (" + str(y) + ") - (" + str(a) + ")*k"
                res = str(a) + " * " + str(x1) + " + " + str(b) + " * " + str(y) + " = " + str(c)
                break;
            elif a*x1+b*y1==c:
                xf = "x = (" + str(x1) + ") + (" + str(c) + ")*k"
                yf = "y = (" + str(y1) + ") - (" + str(a) + ")*k"
                res = str(a) + " * " + str(x1) + " + " + str(b) + " * " + str(y1) + " = " + str(c)
                break;
            
        y = 0
        y1 = 0
            
        if xf!="" and yf!="":
            break;
        
    if xf=="" and yf=="":
        print("решение не найдено")
    else:
        print(res)
        print(xf)
        print(yf)
        
else:
    print("решения нет")
    