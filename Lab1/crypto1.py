#Реализовать программный продукт нахождения всех первообразных корней по заданному простому модулю с указанием всех этапов нахождения корня.
def razlo(m):
    i = 2
    li = []
    while m>1:
        if m%i==0:
            while m%i==0:
                m = m/i
            li.append(i)
        else:
            i+=1
    return li



print("modul: ")
modul = int(input())

stepen1 = 1
stepen2 = 1
stepen = []
itog = []
mn = razlo(modul-1) 
for elem in mn:
    
    stepen1 *= int(elem) - 1
    stepen2 *= int(elem)
    stepen.append(int((modul - 1) / int(elem)))
    
stepen1 *= modul - 1
count = stepen1 / stepen2
print ("count: " + str(int(count)))
print ("stepeni: " + str(stepen))

s = ""
i = 2
shagi = []

while count > 0:
    k = 1
    
    s = "g = " + str(i)
    if (i**stepen[0] % modul == modul - 1):
        s += "; " + str(i) + "^" + str(stepen[0]) + " mod " + str(modul) + " = " + str(modul-1) 
        for elem in stepen[1:]:
            s += "; " + str(i) + "^" + str(elem) + " mod " + str(modul) + " = " + str(i**elem % modul)
            if (i**elem % modul == 1):
                k = 0
                break
            
        if k == 1:
            count -= 1
            itog.append(str(i))
    shagi.append(s+".")
    i += 1
    
i = 0
print()
print("SHAGI:" )
for shag in shagi:
    i += 1
    print (str(i) + ") " + shag)        

print()
print ("Otvet: " + str(itog))
        
