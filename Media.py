import random 
import math

def media(X):
    return sum(X) / len(X) #len saca la longitud de los valores (n)

def varianza(X):
    mu = media(X)
    acumulador = 0
    for x in X:
        acumulador += (x - mu)**2
    return acumulador / len(X)

def desviacion_estandar(X):
    return math.sqrt(varianza(X))

    if __name__ == '__main__':
        X = [random.randint(1, 21) for i in range (20)]
        mu = media(X)
        Var = varianza(X)
        sigma = desviacion_estandar(X)

        print(f'Arreglo X: {X}')
        print(mu)



#Otra forma de hacerlo usando la funcion MEAN

#import random
#import statistics

#if __name__ == '__main__':

 #   edades = [random.randint(1,35) for i in range (20)]
 #   print(edades)
 #   print(statistics.mean(edades))