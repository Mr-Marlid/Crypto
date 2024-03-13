import math

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

def sposob1(a,b,m):
    print ("1 sposob")
    x_f = ""
    for i in range (0,m):
        if (a*i-b)%m == 0:
            x_f = "x = " + str(i) + "(mod " + str(m) +")"
            break;
    if x_f!="":
        print(x_f)
    else:
        print ("Решения нет")    

def f2(a,m,c):
    
    if a > 0:
        c.append(math.floor(m / a))
        return f2(m%a,a,c)
    else:
        
        return c
        
        
def sposob2(a,b,m):
    q = []
    x_f = ""
    q = f2(a,m,q)
    
    p = []
    for i in range(len(q)):
        if i == 0:
            p.append( q[0])
            n= 0
        elif i == 1:
            p.append(q[0]*q[1] + 1)
            n = 1
        else:
            p.append(q[i]*p[i-1] + p[i-2])
            n = i
    x = ((-1)**(n) * p[n-1] * b) % m
    x_f = "x = " + str(x) + "(mod " + str(m) + ")"   
    print("2 sposob")
    print (x_f)


print ("ax=b(mod m)")
print ("Введите a:")
a = int(input())
print ("Введите b:")
b = int(input())
print ("Введите m:")
m = int(input())



no = nod(a,m)

if no>1 and b%no!=0:
    print ("Решения нет")
else:
    
    a = int(a / no)
    b = int(b / no)
    m = int(m / no)
    
    no = nod(a,m)
    
    sposob1(a,b,m)

    sposob2(a,b,m)
        

    
    
