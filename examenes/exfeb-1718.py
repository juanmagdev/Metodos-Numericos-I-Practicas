from numpy import *
from matplotlib.pyplot import *
from scipy.interpolate import interp1d
from scipy.integrate import quad  # paquete para aproximar integrales

def tabla_diferencias_divididas(x, y):
    # x: array con n coordenadas x, y: array con n coordenadas y
    """ Calcula la tabla completa de las diferencias divididas a 
    partir de los datos x e y. Devuelve una matriz (df) triangular 
    inferior que en la columna k-esima contiene las diferencias 
    divididas de orden k"""

    n = len(y)
    df = zeros([n, n])
    df[:, 0] = y
    yn = y
    for i in range(0, n-1):
        dx = x[i+1: n]-x[0:n-(i+1)]
        yn = diff(yn)/dx
        df[i+1:n, i+1] = yn
    return df

x = [0, 0.5, 1, 1.5, 2]
y = [1.533, 0.533, -0.554, -1.11, -2.1]

tabla_diferencias_divididas(x,y)