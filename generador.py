import time
from sys import stdout
import funciones as f

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

banner = """
______              _____                           _             
| ___ \            |  __ \                         | |            
| |_/ /_ _ ___ ___ | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
|  __/ _` / __/ __|| | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| | | (_| \__ \__ \| |_\ \  __/ | | |  __/ | | (_| | || (_) | |    (By Tuch0)
\_|  \__,_|___/___(_)____/\___|_| |_|\___|_|  \__,_|\__\___/|_|                                                            
"""

def menu():
    red()
    print(banner)
    blue()
    time.sleep(1)
    print("1 -> Solo Letras")
    time.sleep(0.5)
    print("\n2 -> Solo Números")
    time.sleep(0.5)
    print("\n3 -> Letras y Números")
    time.sleep(0.5)
    print("\n4 -> Salir")
    time.sleep(0.5)

menu()
option = int(input("\n-->> "))

print('************************************************************************************')
if option == 1:
    f.letras()
elif option == 2:
    f.numeros()
elif option == 3:
    f.letras_numeros()
elif option == 4:
    exit
else:
    print('El dato introducido es inválido , prueba de nuevo solo introduciendo números enteros')
