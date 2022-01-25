from numpy import *
from matplotlib.pyplot import *
from scipy.interpolate import interp1d

############################################
################## TEMA 2 ##################
############################################

# Metodo de la dicotomía
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



# Metodo de la dicotonia modificado para aproximar dado un \epsilon de precision
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



# Regula Falsi
def regula_falsi(f,a,b,eps,nMax):
    an=a
    bn=b
    fan=f(an)
    fbn=f(bn)
    if fan==0:
        print(an,' es raiz de la funcion')
        return an
    elif fbn==0:
        print(bn,' es raiz de la funcion')
        return bn
    if fan*fbn>0:
        print('No hay cambio de signo,luego no se puede aplicar el metodo')
        return 
    error=eps+1 #siempre entra al bucle
    cont=0
    while(error > eps and cont < nMax):
        cn=bn-(bn-an)/(fbn-fan)*fbn
        fcn=f(cn) 
        print('iter ',cont,', c= ',cn,', fc= ',fcn)
        cont+=1
        error=abs(fcn)
        if fcn==0:
            return cn
        elif fan*fcn<0:
            bn=cn
            fbn=fcn
        else:
            an=cn
            fan=fcn
    print('La aproximacion de la raiz tras ',cont,' iteraciones es ',cn)
    if error<=eps:
        print('Se ha alcanzado una aproximacion satisfactoria')
    else:
        print('Se ha alcanzado el numero maximo de iteraciones')
    return cn



## Regula Falsi modificado de manera que se detiene cuando llega a una aproximacion c_n con |f(c_n)| \leq \epsilon
def regula_falsi_mod(f,a,b,eps,nMax):
    an=a
    bn=b
    fan=f(an)
    fbn=f(bn)
    if fan==0:
        print(an,' es raiz de la funcion')
        return an
    elif fbn==0:
        print(bn,' es raiz de la funcion')
        return bn
    if fan*fbn>0:
        print('No hay cambio de signo,luego no se puede aplicar el metodo')
        return 
    cont=0
    cn=bn-(bn-an)/(fbn-fan)*fbn
    fcn=f(cn) 
    print('iter ',cont,', c= ',cn,', fc= ',fcn)
    cn_old=cn
    if fcn==0:
        return cn
    elif fan*fcn<0:
        bn=cn
        fbn=fcn
    else:
        an=cn
        fan=fcn
    cont+=1
    error=eps+1 #siempre entra al bucle
    while(error > eps and cont < nMax):
        cn=bn-(bn-an)/(fbn-fan)*fbn
        fcn=f(cn) 
        print('iter ',cont,', c= ',cn,', fc= ',fcn)
        cont+=1
        error=abs(cn-cn_old)
        cn_old=cn
        if fcn==0:
            return cn
        elif fan*fcn<0:
            bn=cn
            fbn=fcn
        else:
            an=cn
            fan=fcn
    print('La aproximacion de la raiz tras ',cont,' iteraciones es ',cn)
    if error<=eps:
        print('Se ha alcanzado una aproximacion satisfactoria')
    else:
        print('Se ha alcanzado el numero maximo de iteraciones')
        
    return cn

## Metodo de la secante
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


## Metodo del punto fijo
def puntoFijo(g, x0, eps, nmax):
    # g: funcion de iteracion, x_0: semilla, eps: precision, nmax: Numero maximo de iteraciones
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

    #*INCISO:*
    # El metodo del punto dijo es aplicable:
    #   - a una sucesion dada: 
    #       1. definimos la sucesion y luego la pasamos como paramentros
    #   - al metodo de Newton, donde: 
    #       1. hay que definir la funcion x - f(x)/f'(x)
    #  

   


############################################
################## TEMA 3 ##################
############################################

## Tabla diferencias divididas
def tabla_diferencias_divididas(x,y):
    # x: array con n coordenadas x, y: array con n coordenadas y
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

    #
    # Ejemplo uso: 
    #   Obten la tabla paara x = [0, 0.25, 0.5, 0.75, 1.0], 
    #                        y = exp ([0, 0.25, 0.5, 0.75, 1.0]
    #   x = linspace(0,1,5)
    #   y = exp(x)
    #   tabla_ejercicio1 = tabla_diferencias_divididas(x,y)
    #   print(tabla_ejercicio1)
    #

## Cálculo del polinomio de interpolación de Lagrange mediante la fórmula de Newton
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

## Calculo del polinomio usando el algoritmo de Horner
def eval_pol_horner(p,z0):
    # p(z0) = (((anz0 + an−1)z0 + an−2 )z0 + . . . + a1 )z0 + a0.
    n = len(p)
    cn = p[n-1]
    for i in range (n-2,-1,-1):
        cn = p[i] + cn*z0
    return cn

## Calculo del polinomio usando el algoritmo de Horner y la formula de Newton
def eval_forma_newton_horner(x,y,z0):   
    n = len(y)
    df = tabla_diferencias_divididas(x,y)
    cn = df[n-1,n-1]
    for i in range (n-2,-1,-1):
        cn = cn*(z0-x[i])+df[i,i]
    return cn

## Calculo del polinomio de interpolacion de f: [a,b] -> R
def calculo_polinomio(f,a,b,N,z0):
    # f: funcion, a,b: limites del intervalo, N: numero de particiones, z_0: punto a evaluar
    x = linspace(a,b,N+1)
    y = f(x)
    cn = eval_forma_newton_horner(x,y,z0)
    error = max(abs(f(z0) - cn))    
    return cn, error

    # Ejemplo de uso:
    #   z0 = linspace(-3,3,601)
    #   for N in range (5,21,5):
    #   px, error = calculo_polinomio(exp,-3,3,N,z0)
    #   plot(z0,exp(z0),"r",z0,px,"y")
    #   show()
    #   print("El error cometido con N =" ,N, "es" ,error)

# Interpolacion a trozos SPLINE lineal
def splineLin(f, a, b, N):
    x = linspace(a, b, N + 1)
    y = f(x)
    pol = interp1d(x, y, kind = "lineal")
    return pol

# Interpolacion a trozos SPLINE cubica
def splineCub(f, a, b, N):
    x = linspace(a, b, N + 1)
    y = f(x)
    pol = interp1d(x, y, kind = "cubic")
    return pol

splineCub(exp, 2, 4, 10)
