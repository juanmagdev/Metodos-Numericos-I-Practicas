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
    
print()
print("----- Apartado (d) -----")
print() 
    
def bisec2(f,a,b,eps):
    an=a
    bn=b
    fan=f(an)
    fbn=f(bn)
    
    if (fan == 0):
        print (a, "es raíz de la función")
        return a
    elif (fbn == 0):
        print (b, "es raíz de la función")
        return b
    elif (fan * fbn > 0):
        print("No hay cambio de signo: no se puede aplicar el método")
        
    print("%1s %11s %11s" % ("k", "cn", "f(cn)" ))
    
    N = int((log(b-a) - log(eps))/log(2)) + 1
    
    for k in range(N):
        cn=(an+bn)/2.0
        fcn=f(cn)
        print("%1i %11.8f %11.8f" % (k, cn, fcn))
        if fcn==0:
            print(cn, "es la raíz de la función")
            return cn
        elif fan*fcn<0:
            bn=cn
            fbn=fcn
        else:
            an=cn
            fan=fcn
    print("La aproximacion de la raíz tras",N, "iteraciones es",cn, "y f(cn) es",fcn)
    print()
    return cn

bisec2(funcion2,0,1,10e-7)


print()
print("----- EJERCICIO 3 -----")

print()
print("--- APARTADO A ---")

def secante(f,a,b,x0,x1,eps):  
    print()
    print("----- MÉTODO DE LAS SECANTES -----")
    print("%1s %13s %13s" % ("k", "xk", "f(xk)"))
    def secante2(f,a,b,x0,x1,eps,k):
        if f(x0) == f(x1):
            return "Error: f(x0) = f(x1)"
        else:
            x2 = x1 - (x1 - x0)*f(x1)/(f(x1) - f(x0))
            if x2 >= a:
                if x2 <= b:
                    if f(x2) == 0:
                        print("La raiz es:" ,x2)
                    else:
                        if abs(x2 - x1) <= eps:
                            print("%1i %13.10f %13.10f" % (k, x2, f(x2)))
                            return x2
                        else:
                            print("%1i %13.10f %13.10f" % (k, x2, f(x2)))
                            secante2(f,a,b,x1,x2,eps,k+1)
    return secante2(f,a,b,x0,x1,eps,0) 

print()
print("--- APARTADO B ---")

# secante(funcion1,0,1,0,1,10e-7)
# secante(funcion1,-3,-2,-3,-2,10e-7)
# secante(funcion1,2,3,2,3,10e-7)       
# secante(funcion2,0,1,0,1,10e-7)

print()
print("--- APARTADO C ---")

def secante2(f,a,b,x0,x1,eps):  
    print()
    print("----- MÉTODO DE LAS SECANTES -----")
    print("%1s %13s %13s" % ("k", "xk", "f(xk)"))
    def secante2(f,a,b,x0,x1,eps,k):
        if f(x0) == f(x1):
            return "Error: f(x0) = f(x1)"
        else:
            x2 = x1 - (x1 - x0)*f(x1)/(f(x1) - f(x0))
            if x2 >= a:
                if x2 <= b:
                    if f(x2) == 0:
                        print("La raiz es:" ,x2)
                    else:
                        if abs(f(x2)) <= eps:
                            print("%1i %13.10f %13.10f" % (k, x2, f(x2)))
                            return x2
                        else:
                            print("%1i %13.10f %13.10f" % (k, x2, f(x2)))
                            secante2(f,a,b,x1,x2,eps,k+1)
    return secante2(f,a,b,x0,x1,eps,0) 

print()
print("--- APARTADO D ---")

# secante2(funcion1,0,1,0,1,10e-7)
# secante2(funcion1,-3,-2,-3,-2,10e-7)
# secante2(funcion1,2,3,2,3,10e-7)       
# secante2(funcion2,0,1,0,1,10e-7)

def dinero(n):
    print("%1s %13s" % ("Día", "Dinero"))
    for k in range(n):
        x = (2**k)*0.02 - 0.01
        print("%1i %13.2f" % (k+1, x))
    return x


dinero(30)
