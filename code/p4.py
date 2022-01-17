from numpy import *
from matplotlib.pyplot import *
from scipy.interpolate import interp1d

print()
print("----- EJERCICIO 1 -----")
print("Cálculo de las diferencias divididas")

def tabla_diferencias_divididas(x,y):
   """ Calcula la tabla completa de las diferencias divididas a 
   partir de los datos x e y. Devuelve una matriz (df) triangular 
   inferior que en la columna k-esima contiene las diferencias 
   divididas de orden k"""

   n= len(y)
   df=zeros([n,n])
   df[:,0]=y
   yn=y
   for i in range(0, n-1):
       dx=x[i+1: n]-x[0:n-(i+1)]
       yn=diff(yn)/dx
       df[i+1:n,i+1]=yn
   return df

print()
print("A)")

x = linspace(0,1,5)
y = exp(x)
tabla_ejercicio1 = tabla_diferencias_divididas(x,y)
print(tabla_ejercicio1)

print()
print("----- EJERCICIO 2 -----")
print("Cálculo del polinomio de interpolación de Lagrange mediante la fórmula de Newton")
    
def eval_forma_newton(x,y,z_0):
    """ Calcula en primer lugar el polinomio de interpolacion de 
    Lagrange que interpola los datos x e y mediante la formula de 
    ewton y lo evalua en z0."""  
    
    n= len(y)
    df=tabla_diferencias_divididas(x,y)
    peval=df[0,0]
    prod=1.0
    for i in range(1,n):
        prod=prod*(z_0-x[i-1])
        peval=peval+df[i,i]*prod
    return peval   

print()
print("A)")

x = linspace(0,1,5)
y = exp(x)
print("El resultado de evaluar el polinomio en 1/3 es: " ,eval_forma_newton(x,y,1/3))
print("El polinomio pasa por los puntos de evaluacion: " ,eval_forma_newton(x,y,x) == y)

print()
print("B)")

def eval_pol_horner(p,z0):
    n = len(p)
    cn = p[n-1]
    for i in range (n-2,-1,-1):
        cn = p[i] + cn*z0
    return cn

polinomio=array([-1,0,1])
z0 = array([0,20])
print(eval_pol_horner(polinomio,z0))

print()
print("C)")

def eval_forma_newton_horner(x,y,z0):   
    n = len(y)
    df = tabla_diferencias_divididas(x,y)
    cn = df[n-1,n-1]
    for i in range (n-2,-1,-1):
        cn = cn*(z0-x[i])+df[i,i]
    return cn

x = linspace(0,1,5)
y = exp(x)
print("El resultado de evaluar el polinomio en 1/3 es: " ,eval_forma_newton_horner(x,y,1/3))
print("El polinomio pasa por los puntos de evaliacion: " ,eval_forma_newton_horner(x,y,x) == y)

print()
print("D)")

def apartado_d(f,a,b,N,z0):
    x = linspace(a,b,N+1)
    y = f(x)
    cn = eval_forma_newton_horner(x,y,z0)
    error = max(abs(f(z0) - cn))    
    return cn, error

print()
print("E)")

z0 = linspace(-3,3,601)
for N in range (5,21,5):
    px, error = apartado_d(exp,-3,3,N,z0)
    plot(z0,exp(z0),"r",z0,px,"y")
    show()
    print("El error cometido con N =" ,N, "es" ,error)
            
print()
print("F)")

z0 = linspace(-5,5,1001)
def ff(x):
    return 1/(1 + x**2)
for N in range (5,21,5):
    px, error = apartado_d(ff,-5,5,N,z0)
    plot(z0,ff(z0),"r",z0,px,"y")
    show()
    print("El error cometido con N =" ,N, "es" ,error)


print()
print("----- EJERCICIO 3 -----")
print("Interpolación de tipo spline")



print()
print("A)")

def splineLin(f, a, b, N):
    x = linspace(a, b, N + 1)
    y = f(x)
    pol = inter1d(x, y, kind = "lineal")
    return pol

print()
print("B)")

def splineCub(f, a, b, N):
    x = linspace(a, b, N + 1)
    y = f(x)
    pol = inter1d(x, y, kind = "cubic")
    return pol
