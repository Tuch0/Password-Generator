#!bin/bash/python3

import funciones as f

def menu():
    print('GENERADOR DE CONTRASEÑAS')
    print('-------------------------------------------')
    print('1 - Solo letras')
    print('2 - Solo números')
    print('3 - Letras y números')
    print('4 - Salir')
    print('-------------------------------------------')

menu()

respuesta = int(input('SELECCIONE LA OPCIÓN QUE DESEAS: '))
print('-------------------------------------------')
if respuesta == 1:
    f.letras()
elif respuesta == 2:
    f.numeros()
elif respuesta == 3:
    f.letras_numeros()
elif respuesta == 4:
    exit
else:
    print('El dato introducido es inválido , prueba de nuevo solo introduciendo números enteros')
