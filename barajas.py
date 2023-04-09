import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '10', 'jota', 'reina', 'rey']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas

def obtener_mano(barajas, tamanio_mano):
    mano = random.sample(barajas, tamanio_mano)

    return mano

def main(tamanio_mano, intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamanio_mano)
        manos.append(mano)

    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter = dict(collections.Counter(valores)) #convertirlo en un diccionario
        for val in counter.values():
            if val == 2:
                pares += 1
                break 
    
    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en una mano de {tamanio_mano} barajas es {probabilidad_par}')


if __name__ == '__main__':
    tamanio_mano = int(input('De cuantas barajas sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))
    main(tamanio_mano, intentos)

    #barajas = crear_baraja()
    #mano = obtener_mano(barajas, 5)
    #print(mano)