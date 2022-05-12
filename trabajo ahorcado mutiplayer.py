'''
juego del ahoracado mutiplayer
'''
from distutils.command.clean import clean
import time
from random import choice

nombre_p1 = str(input('¿Jugador 1, ¿cuál es tu nombre? '))
time.sleep(1)
nombre_p2 = str(input('¿Jugador 2, ¿cuál es tu nombre? '))

time.sleep(1)
print('Hola', nombre_p1, 'y', nombre_p2)
print('Bienvenid@s al juego del ahoracado multiplayer')
time.sleep(2)

quien_parte_list = [nombre_p1, nombre_p2]
quien_parte = choice(quien_parte_list)
print('El jugador que parte es...')
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print(quien_parte)
time.sleep(2)

if quien_parte == nombre_p1:
    print(nombre_p2.upper, 'escribe una palabra la cual quieres que', nombre_p1.upper ,'adivine')
    palabra_p1 = input('')
    tupalabra = ''
    vidas = 5
    clean

    while vidas > 0: 
        fallas = 0
        for letra in palabra_p1:
            if letra in tupalabra:
                print(letra, end = '')
            else: 
                print('_', end = '')
                fallas = 1
        if fallas == 0:
            puntos_p1 = 1
            print('')
            print('¡Felicitaciones, ganaste 1 punto!')
            break

        tuletra = input(' Introduce una letra: ')
        tupalabra += tuletra

        if tuletra not in palabra_p1:
            vidas -= 1
            print('')
            print('Equivocación')
            print('Tu tienes ', +vidas, ' vidas')
        if vidas == 0:
            print('¡Perdiste!')
    else:
        print('Gracias por participar')
    
else:
    print(nombre_p1.capitalize, 'escribe una palabra la cual quieres que', nombre_p2.capitalize, 'adivine')
    palabra_p2 = input('')
    tupalabra_2 = ''
    vidas = 5

    while vidas > 0:
        fallas = 0
        for letra in palabra_p2:
            if letra in tupalabra_2:
                print(letra, end = '')
            else:
                print('_', end = '')
                fallas =1
        if fallas == 0:
            puntos_p2 = 1
            print('')
            print('¡Felicitaciones, ganaste 1 punto!')
            break

        tuletra = input(' introduce una letra: ')
        tupalabra_2 += tuletra

        if tuletra not in palabra_p2:
            vidas -= 1
            print('')
            print('Equivocación')
            print('Tu tienes ', +vidas, ' vidas')
        if vidas == 0:
            print('¡Perdiste!')
    else:
        print('Gracias por participar')