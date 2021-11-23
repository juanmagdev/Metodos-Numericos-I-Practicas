from  numpy import *
from matplotlib.pyplot import *

import sys
sys.setrecursionlimit(100) #para evitar errores recursivos


#Ejercicio 1
def puntoFijo(g, x0, eps, nmax):

    it = 0
    error = 1 + eps
    while error > eps and it<= nmax:
        x1 = g(x0)
        error = abs(x1 - x0)
        it += 1
        x0 = x1

    if it>nmax:
        print('Se ha alcanzado el numero máximo de iteraciones sin encontrar el punto fijo')
    else: 
        print('Se ha alcanzado el cirterio de parada. Tras ', it, ' iteraciones la solución obtenida es', x0, 'con error', error)
    return x1

def g_cos_newton(x):
    return x + cos(x)/sin(x)

puntoFijo(g_cos_newton, 1, 1e-7, 100)

#EJERCICIO 2
def fej2(x):
    return x - exp(-x)

def gej2a(x):
    return  exp(-x)

puntoFijo(gej2a, 0.5, 1e-7,100)

def gej2b(x):
    return x - fej2(x)/(1 + exp(-x))

puntoFijo(gej2b, 0.5, 1e-7,100)

#EJERCICIO3
k = 2/3
a = 0.093

def kepler(x):
    return k -x +a*sin(x)

def gej3(x): 
    return k +a*sin(x)

puntoFijo(gej3,0.5, 1e-7, 100)

def gej3b (x):
    return x -kepler(x)/(a*cos(x) -1)

puntoFijo(gej3b,0.5, 1e-7, 100)

#EJERCICIO 4
def f4(x):
    return cos(x) - x

def g4a(x):
    return cos(x)

puntoFijo(g4a, 0.5, 1e-7, 100)

def g4b(x):
    return x - f4(x)/(-sin(x)-1)

puntoFijo(g4b, 0.5, 1e-7, 100)

#EJERCICIO 5
def f5(x):
    return x**5 - 5*x**3 + 1

def g5a(x):
    return x - f5(x)/5*x**4 - 15*x**2


#EJERCICIO 6

def puntofijo2(f,g,x0,eps,nmax):
    error = eps + 1
    k = 0
    while (error > eps and k < nmax):
        x1 = g(x0)
        error = abs(f(x1))
        x0 = x1
        k = k + 1
    if k == nmax:
        print("Se alcanza el número máximo de iteraciones")
        print("El último valor calulado es",x1)
    else:
        print("Se alcanza la precisión requerida en",k,"iteraciones")
        print("El último valor calulado es",x1)
    return x1
            
print()
print("B)")

def f6b(x):
    return x + (x-1)*exp(x)

x = linspace(0,1,100)
y =f6b(x)
plot(x,y,"r",x,0*x)
xlabel("Eje X")
ylabel("Eje Y")
show()

print()
print("C)")
def g6c(x):
    return x - f6b(x)/(1 + x*exp(x))

puntofijo2(f6b,g6c,0.7,10e-8,100)




