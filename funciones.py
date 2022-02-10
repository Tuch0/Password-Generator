#!bin/bash/python3
from random import choice
from sys import stdout

# Colores:
def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)

# Funciones
def letras():
    purple()
    longitud = int(input('Introduce la longitud de la contraseña: '))
    valores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    a = ""
    a = a.join([choice(valores) for i in range(longitud)])
    white()
    print(a)


def numeros():
    purple()
    longitud = int(input('Introduce la longitud de la contraseña: '))
    valores = "0123456789"
    a = ""
    a = a.join([choice(valores) for i in range(longitud)])
    white()
    print(a)


def letras_numeros():
    purple()
    longitud = int(input('Introduce la longitud de la contraseña: '))
    valores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    a = ""      
    a = a.join([choice(valores) for i in range(longitud)])
    white()
    print(a)

def letras_numero_simbolos():
    purple()
    longitud = int(input('Introduce la longitud de la contrasñea: '))
    valores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789!$%&'()*+-./0123456789:;=?@[\]^_`{|}~"
    a = ""      
    a = a.join([choice(valores) for i in range(longitud)])
    white()
    print(a)
