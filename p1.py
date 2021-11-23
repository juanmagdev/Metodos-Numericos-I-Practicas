# %%
# Juan Manuel García Delgado
# Práctica 1
# -------------------------------------

from numpy import *
from matplotlib.pyplot import *

print("Ejercicio 1")

# for


def sumaVeces1(a, n):
    s = 0
    for i in range(n):
        s += a
    return s


print(sumaVeces1(2, 10))

# while


def sumaVeces2(a, n):
    i = 0
    s = 0
    while i != n:
        s += a
        i += 1
    return s


print(sumaVeces2(2, 10))

# -------------------------------------
print("Ejercicio 2")


def precision(n):
    x = 1
    while 1 + x > 1:
        x = x/n
    print("El epsilon de la maquina es", x)


precision(10)


# -------------------------------------
print("Ejercicio 3")

x = linspace(-2, 2, 500)
y = x - exp(-x)
plot(x, y)

show()
print()


# -------------------------------------
print("Ejercicio 4")


def aproxe(n):
    return (1 + 1/n)**n


def error(n):
    return exp(n) - aproxe(n)


print(aproxe(100), exp(100), error(100))

# --------------------------------------
print("Ejercicio 5")


def sumaparcial(n):
    sumaP = 0
    # if n <= 0:
    #    return "Error, no se puede hacer la raiz negativa"
    for k in range(1, n+1):
        sumaP += 1/sqrt(k)

    return sumaP


print(sumaparcial(20))
# --------------------------------------
print("Ejercicio 6")

ns = linspace(1, 100, 100)
sumas = zeros(100)

for n in ns:
    n = int(n)
    sumas[n-1] = sumaparcial(n)

plot(ns, sumas)
show()

plot(x, y)

print()
print("Ejercicio 7")


def sumanesima(n):
    Sn = 0
    for k in range(1, n+1):
        Sn += 1/(k*(k+1))
    print('n=', n, 'Sn=', Sn, 'error', abs(1-Sn))
    return Sn


def sumanesima2(n):
    Sn = 1-(1/(n+1))
    print('n=', n, 'Sn=', Sn, 'error', abs(1-Sn))
    return Sn


sumanesima(10**3)
sumanesima(10**5)
sumanesima(10**7)

sumanesima2(10**3)
sumanesima2(10**5)
sumanesima2(10**7)
sumanesima2(10**20)

print("Ejercicio 8")


def factorial(n):
    if (n == 0):
        return 1
    return n*factorial(n-1)


def aprox2(n):
    Sn = 0
    for k in range(n+1):
        Sn += 1/factorial(k)
    print('n=', n, 'Sn=', Sn, 'error', abs(exp(1)-Sn))
    return Sn


aproxe(10)
aprox2(10)
aproxe(50)
aprox2(50)
aproxe(100)
aprox2(100)
print("Ejercicio 9")


def expTaylor(n, x):
    suma = 0
    for k in range(n):
        suma += x**k/factorial(k)

    print('Sn = ', suma, ' Error= ', abs(exp(x) - suma))
    return suma


expTaylor(400, 4)

print("Ejercicio 10")


def ej10(list):
    contador = 0
    suma = 0
    for i in list:
        suma += i
        contador += 1
    media = suma/contador
    print('En la lista', list, ' sus elementos suman',
          suma, ' y su media es ', media)


ej10([1, 2, 3, 4])
# %%
