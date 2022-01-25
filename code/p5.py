from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import quad

def funexp(x):
    return exp(-x**2)

iquad, equad =  quad(funexp,0,1)

print()
print("El valor aproximado obtenido:",iquad,"y la cora del error es:",equad)

print()
print("----- EJERCICIO 1 -----")

def puntomedio(f,a,b):
    c = 0.5*(a+b)
    ipuntomedio = (b-a)*f(c)
    epuntomedio = abs(ipuntomedio - iquad)
    print()
    print("La integral usando la Fórmula del Punto Medio es aproximadamente:",ipuntomedio, "y el 'error' es:",epuntomedio)
    return ipuntomedio

puntomedio(funexp,0,1)

print()
print("----- EJERCICIO 2 -----")

def trapecio(f,a,b):
    itrapecio = 0.5*(b-a)*(f(a) + f(b))
    etrapecio= abs(itrapecio - iquad)
    print()
    print("La integral usando la Fórmula del Trapecio es aproximadamente:",itrapecio, "y el 'error' es:",etrapecio)
    return itrapecio

trapecio(funexp,0,1)

print()
print("----- EJERCICIO 3 -----")

def simpson(f,a,b):
    c = 0.5*(a+b)
    isimpson = ((b-a)/6)*(f(a) + 4*f(c) + f(b))
    esimpson = abs(isimpson - iquad)
    print()
    print("La integral usando la Fórmula de Simpson es aproximadamente:",isimpson, "y el 'error' es:",esimpson)
    return isimpson

simpson(funexp,0,1)

print()
print("----- EJERCICIO 4 -----")

def puntomedioC(f,a,b,N):
    x = linspace(a,b,N+1)
    c = 0.5*(x[0:N] + x[1:N+1])
    integral = ((b-a)/N)*sum(f(c))
    error = abs(integral - iquad)
    print()
    print("[Fórmula del Punto Medio Compuesta] N = ",N,", h =",1/N,", Aproximación:",integral, ", 'Error':",error)
    return integral

puntomedioC(funexp,0,1,10)
puntomedioC(funexp,0,1,20)
puntomedioC(funexp,0,1,40)
puntomedioC(funexp,0,1,80)

print()
print("----- EJERCICIO 5 -----")

def trapecioC(f,a,b,N):
    x = linspace(a,b,N+1)
    integral = ((b-a)/(2*N))*(f(a) + f(b) + 2*sum(f(x[1:N])))
    error = abs(integral - iquad)
    print()
    print("[Fórmula del Trapecio Compuesta] N = ",N,", h =",1/N,", Aproximación:",integral, ", 'Error':",error)
    return integral

trapecioC(funexp,0,1,10)
trapecioC(funexp,0,1,20)
trapecioC(funexp,0,1,40)
trapecioC(funexp,0,1,80)

print()
print("----- EJERCICIO 6 -----")

def simpsonC(f,a,b,N):
    x = linspace(a,b,N+1)
    c = 0.5*(x[0:N] + x[1:N+1])
    fb = f(b)
    integral = ((b-a)/(6*N))*(f(a) + 2*sum(f(x[1:N])) + 4*sum(f(c) + fb))
    error = abs(integral - iquad)
    print()
    print("[Fórmula de Simpson Compuesta] N = ",N,", h =",1/N,", Aproximación:",integral, ", 'Error':",error)
    return integral

simpsonC(funexp,0,1,10)
simpsonC(funexp,0,1,20)
simpsonC(funexp,0,1,40)
simpsonC(funexp,0,1,80)

print()
print("----- EJERCICIO 7 -----")

def gauss3(f,a,b):
    t = array([-0.77459667,0,0.77459667])
    alphatilde = array([5/9, 8/9, 5/9])
    x = zeros(size(t))
    alpha = zeros(size(t))
    for k in range(size(t)):
        x[k] = a + 0.5*(b-a)*(t[k] + 1)
        alpha[k] = 0.5*(b-a)*alphatilde[k]
    gauss3 = sum(alpha*f(x))
    error = abs(gauss3 - iquad)
    print()
    print("[Fórmula de Gauss de 3 puntos] Aproximación:",gauss3,",'Error':",error)
    return gauss3

gauss3(funexp,0,1)