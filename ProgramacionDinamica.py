#PROGRAMACION DINAMICA
#Ejemplo serie de Fibonacci
import sys
def fibonacci_recursivo(n): #Hay que elegir numeros pequeños porque si no tarma mucho en calcularlo
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_dinamico(n, memo = {}): #Ahora tarda menos de un segundo en calcular numeros grandes
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado #Lo guardamos en un diccionario

if __name__=='__main__':
    sys.setrecursionlimit(10002)
    n = int(input("Ingresa un numero: "))
    resultado = fibonacci_dinamico(n)
    print(resultado)