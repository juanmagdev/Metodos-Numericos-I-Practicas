from numpy import *
from matplotlib.pyplot import *

## ---------------------------FUNCIONES YA DEFINIDAS-----------------------------
def bisec(f,a,b,N):
    an=a
    bn=b
    fan=f(an)
    fbn=f(bn)
    if fan==0:
        print(str(a)+'es raíz de la función')
        return a
    elif fbn==0:
        print(str(b)+'es raíz de la función')
        return b
    elif fan*fbn>0:
        print('No hay cambio de signo: no se puede aplicar el método')
        #return
    
    print("%1s %11s %11s" % ("k", "cn", "f(cn)" ))
    
    for k in range(N):
        cn=(an+bn)/2.
        fcn=f(cn)
        print("%1i %11.8f %11.8f" % (k, cn, fcn))
        if fcn==0:
            print(str(cn)+'es raíz de la función')
            return cn
        elif fan*fcn<0:
            bn=cn
            fbn=fcn
        else:
            an=cn
            fan=fcn
    print('La aproximación de la raíz tras '+str(N)+' iteraciones es '+str(cn))
    return cn

## ------------------------------------------------------------------------------


print()
print("----- EJERCICIO 1 -----")
print()

print()
print("----- Apartado (a) -----")
print()
# Modificado en la sección FUNCIONES YA DEFINIDAS
print()
print("----- Apartado (b) -----")
print()
def funcion1(x):
    return x**5 - 5*(x**3) + 1

x = linspace(-3,3,100)
y = funcion1(x)

plot(x,y,"r",x,0*x)
xlabel("Eje X")
ylabel("Eje Y")
show()
bisec(funcion1,0,1,20) #Metodo de la dicotomia para funcion1 en [0,1] con 20 iteraciones
bisec(funcion1,-3,-2,20)
bisec(funcion1,2,3,20)

print("Se observa que se estabilizan 5 cifras decimales")

print()
print("----- Apartado (c) -----")
print()

def funcion2(x):
    return cos(x) - x
    
x2 = linspace(0,2*pi,100)
y2 = funcion2(x2)

plot(x2,y2,"r",x2,0*x2)
xlabel("Eje X")
ylabel("Eje Y")
show()

bisec(funcion2,0,1,20)
print("Se observa que se estabilizan 5 cifras decimales")
    
   

