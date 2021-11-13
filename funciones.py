#!bin/bash/python3

from random import choice

def letras():
    longitud = int(input('Introduce la longitud de la contraseña: '))
    valores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    a = ""
    a = a.join([choice(valores) for i in range(longitud)])
    print(a)


def numeros():
    longitud = int(input('Introduce la longitud de la contraseña: '))
    valores = "0123456789"
    a = ""
    a = a.join([choice(valores) for i in range(longitud)])
    print(a)


def letras_numeros():
    longitud = int(input('Introduce la longitud de la contraseña: '))
    valores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    a = ""      
    a = a.join([choice(valores) for i in range(longitud)])
    print(a)
