
#/Python/NumerosAT.p
# Este es un recopilador de datos
import random
from datetime import datetime
#from collections import Counter

fecha_actual = datetime.now()
print("Fecha actual:", fecha_actual)

print ("Hola Navegantes")
print ("Hello World - Hellow navigators")
print ("Bienvenidos a mi Universo, donde todo es posible para el que cree")
print (" ¿Y tu, crees que es posible?")
conviccion = input ()

# print("El nombre de tu script es NumerosAT.py")

'''

Buscar numeros repetidos de cadena_TINKA
Buscar numeros repetidos de cadena_Boliyapa
Buscar numeros repetidos de cadena_SIOSI

'''

# print ("Sorteo 1070- 06/03/2024")u*
# print ("Sorteo 1069 - 03/03/2024")
# print ("Sorteo 1068 - 28/02/2024")
# print ("Sorteo 1067 - 25/02/2024")
# print ("Sorteo 1066 - 21/02/2024")
# print ("Sorteo 1065 - 18/02/2024")
# print ("Sorteo 1064 - 14/02/2024")
# print ("Sorteo 1063 - 11/02/2024")
# print ("Sorteo 1062 - 07/02/2024")
# print ("Sorteo 1061 - 04/02/2024")
# print ("Sorteo 1060 - 31/01/2024")
# print ("Sorteo 1059 - 28/01/2024")
# print ("Sorteo 1058 - 24/01/2024")
# print ("Sorteo 1057 - 21/01/2024")
# print ("Sorteo 1056 - 17/01/2024")
# print ("Sorteo 1055 - 14/01/2024")
# print ("Sorteo 1054 - 10/01/2024")
# print ("Sorteo 1053 - 07/01/2024")
print ("Sorteo 1052 - 03/01/2024" " 35, 28, 12, 15, 4, 39")
# print ("Sorteo 1051 - 31/12/2023")
# print ("Sorteo 1050 - 27/12/2023")
# print ("Sorteo 1049 - 24/12/2023")
# print ("Sorteo 1048 - 20/12/2023")
# print ("Sorteo 1047 - 17/12/2023")
# print ("Sorteo 1046 - 13/12/2023")
# print ("Sorteo 1045 - 10/12/2023")
# print ("Sorteo 1044 - 06/12/2023")
# print ("Sorteo 1043 - 03/12/2023")
# print ("Sorteo 1042 - 29/11/2023")
# print ("Sorteo 1041 - 26/11/2023")
# print ("Sorteo 1040 - 22/11/2023")
# print ("Sorteo 1039 - 19/11/2023")
# print ("Sorteo 1038 - 15/10/2023")
# print ("Sorteo 1037 - 12/11/2023")
# print ("Sorteo 1036 - 08/11/2023")
# print ("Sorteo 1035 - 05/11/2023")
# print ("Sorteo 1034 - 01/11/2023")
# print ("Sorteo 1033 - 29/10/2023")
# print ("Sorteo 1032 - 25/10/2023")
# print ("Sorteo 1031 - 23/10/2023")
# print ("Sorteo 1030 - 18/10/2023")
# print ("Sorteo 1029 - 15/10/2023")
# print ("Sorteo 1028 - 11/10/2023")
# print ("Sorteo 1027 - 08/10/2023")
# print ("Sorteo 1026 - 04/10/2023")
# print ("Sorteo 1025 - 01/10/2023")
# print ("Sorteo 1024 - 27/09/2023")
# print ("Sorteo 1023 - 24/09/2023")
# print ("Sorteo 1022 - 20/09/2023")
# print ("Sorteo 1021 - 17/09/2023")
# print ("Sorteo 1020 - 13/09/2023")
# print ("Sorteo 1019 - 10/09/2023")
# print ("Sorteo 1018 - 06/09/2023")
# print ("Sorteo 1017 - 03/09/2023")
# print ("Sorteo 1016 - 30/08/2023")
# print ("Sorteo 1015 - 27/08/2023")
# print ("Sorteo 1014 - 23/08/2023")
# print ("Sorteo 1013 - 20/08/2023")
# print ("Sorteo 1012 - 16/08/2023")
# print ("Sorteo 1011 - 13/08/2023")
# print ("Sorteo 1010 - 09/08/2023")
# print ("Sorteo 1009 - 06/08/2023")
# print ("Sorteo 1008 - 02/08/2023")
# print ("Sorteo 1007 - 30/07/2023")
# print ("Sorteo 1006 - 26/07/2023")
# print ("Sorteo 1005 - 23/07/2023")
# print ("Sorteo 1004 - 19/07/2023")
# print ("Sorteo 1003 - 16/07/2023")
# print ("Sorteo 1002 - 12/07/2023")
# print ("Sorteo 1001 - 09/07/2023")
# print ("Sorteo 1000 - 05/07/2023")
# print ("Sorteo 999 - 02/07/2023")
# print ("Sorteo 998 - 28/06/2023")
# print ("Sorteo 997 - 25/06/2023")
# print ("Sorteo 996 - 21/06/2023")
# print ("Sorteo 995 - 18/06/2023")
# print ("Sorteo 994 - 14/06/2023")
# Codigo

from collections import Counter

def contar_numeros_repetidos(cadena):
    # Filtrar solo los caracteres numéricos
    numeros = [int(caracter) for caracter in cadena if caracter.isdigit()]

    # Usar Counter para contar la frecuencia de cada número
    frecuencia_numeros = Counter(numeros)

    return frecuencia_numeros

# Ejemplo de uso numeros_TINKA
print ("TINKA")
cadena_TINKA = " -TK, 30, 22, 4, 7, 39, 37, 25, 31, 6, 27, 33, 48, 42, 13, 30,  27, 45, 14, 45, 40, 31, 35, 14, 5, 14, 35, 30, 39, 8, 2, 42, 24, 31, 12, 35, 23, 42, 3, 18, 7, 29, 39, 19, 41, 1, 31, 27, 12, 8, 30, 16, 12, 48, 27, 34, 45, 42, 41, 18, 38, 4, 22, 21, 34, 13, 48, 25, 3, 19, 21, 24, 15, 4, 1, 46, 24, 38, 39, 22, 33, 36, 44, 27, 19, 43, 6, 21, 9, 34, 47, 47, 27, 20, 44, 41, 28, 29, 1, 11, 10, 36, 30, 18, 27, 4, 33, 7, 1, 35, 28, 12, 15, 4, 39, 45, 9, 19, 26, 47, 25, 36, 8, 42, 25, 35, 29, 44, 7, 9, 27, 21, 11, 5, 22, 11, 17, 38, 10, 10, 42, 37, 2, 32, 1, 6, 40, 32, 17, 47, 24, 12, 14, 2, 15, 27, 18, 22, 8, 3, 1, 27, 19, 17, 3, 11, 18, 39, 12, 33, 8, 40, 24, 45, 41, 43, 25, 27, 34, 6, 7, 37, 19, 13, 26, 45, 2, 42, 19, 25, 38, 12, 37, 32, 42, 23, 2, 24, 27, 47, 25, 39, 35, 27, 6, 42, 38, 5, 33, 16, 12, 40, 27, 18, 44, 21, 39, 13, 17, 26, 24, 15, 39, 15, 38, 31, 9, 26, 43, 6, 38, 35, 23, 9, 31, 32, 48, 24, 44, 33, 25, 1, 13, 20, 42, 27, 23, 26, 38, 29, 21, 6, 11, 34, 28, 11, 1, 24, 5, 12, 43, 20, 10, 13, 22, 35, 43, 34, 14, 7, 38, 19, 26, 23, 25, 2, 11, 26, 1, 38, 13, 42, 30, 29, 13, 27, 21, 25, 11, 27, 2, 22, 9, 18, 41, 45, 44, 11, 35, 40, 27, 13, 8, 42, 41, 44, 36, 20, 43, 5, 38, 22, 16, 41, 28, 4, 10, 26, 18, 41, 6, 23, 45, 47, 19, 44, 42, 38, 4, 6, 31, 27, 24, 42, 34, 19, 47, 36, 5, 47, 46, 7, 8, 42, 28, 41, 48, 24, 19, 34, 41, 47, 7, 20, 3, 28, 29, 46, 27, 48, 6, 9, 24, 38, 33, 29, 46, 1, 33, 28, 25, 12, 44, 20, 22, 38, 28, 16, 14, 32, 43, 38, 25, 24, 11, 43, 25, 27, 34, 6, 7, 37, 19, 13, 26, 45, 2, 42, 19, 25, 38, 12, 37, 32, 42, 23, 2, 24, 27, 47, 25, 39, 35, 27, 6, 42, 38, 5, 33, 16, 12, 40, 21, 39, 13, 17, 26, 24, 15, 39, 15, 38, 31, 9, 26, 43, 6, 38, 35, 23, 9, 31, 32, 48, 24, 44, 33, 25, 1, 13, 20, 42, 27, 23, 26, 38, 29, 21, 6, 11, 34, 28, 11, 1, 24, 5, 12, 43, 20, 10, 13, 22, 35, 43, 34, 14, 7, 38, 19, 26, 23, 25, 2, 11, 26, 1, 38, 13, 42, 30, 29, 13, 27, 21, 25, 11, 27, 2, 22, 9, 18, 41"
# Convertir la cadena en una lista de números
numeros = [int(numero.strip()) for numero in cadena_TINKA.split(",")[1:]]

# Obtener 6 números aleatorios
seis_numeros_aleatorios = random.sample(numeros, 6)

print(seis_numeros_aleatorios)

resultado = contar_numeros_repetidos(cadena_TINKA)
print(resultado)

from collections import Counter

def contar_numeros_repetidos(cadena):
    # Filtrar solo los caracteres numericos
    numeros = [int(caracter) for caracter in cadena if caracter.isdigit()]

    # Usar Counter para contar la frecuencia de cada número
    frecuencia_numeros = Counter(numeros)

    return frecuencia_numeros

# Ejemplo de uso numeros_Boliyapa
print ("Boliyapa")
cadena_Boliyapa = " -BY, 38, 46, 8, 33, 5, 28, 30, 44, 40, 47, 6, 12, 25, 24, 17, 43, 31, 31, 29, 14, 44, 28, 47, 14, 30, 16, 23, 6, 7, 2, 25, 23, 7, 21, 16, 46, 4, 7, 26, 47, 16, 32, 47, 19, 42, 35, 32, 27, 31, 32, 35, 25, 9, 4, 30, 22, 34, 10, 2, 41, 45, 30, 31, 20, 3, 43, 40, 14, 20, 12, 34, 41, 6, 13, 26, 27, 33, 14, 11, 16, 8, 26, 36, 20, 31, 32, 35, 38, 25, 9, 4, 30, 22, 34, 10, 2, 41, 45, 30, 31, 20, 3, 43, 40, 14"

# Convertir la cadena en una lista de números
numeros = [int(numero.strip()) for numero in cadena_Boliyapa.split(",")[1:]]

# Obtener 6 números aleatorios
seis_numeros_aleatorios = random.sample(numeros, 6)

print(seis_numeros_aleatorios)

resultado = contar_numeros_repetidos(cadena_Boliyapa)
print(resultado)

from collections import Counter

def contar_numeros_repetidos(cadena):
    # Filtrar solo los caracteres numericos
    numeros = [int(caracter) for caracter in cadena if caracter.isdigit()]

    # Usar Counter para contar la frecuncia de cada número
    frecuencia_numeros = Counter(numeros)

    return frecuencia_numeros

# Ejamplo de uso numeros_SIOSI
print ("SIOSI")
cadena_SIOSI = " -SS, 43, 2, 18, 39, 44, 21, 15, 3, 43, 23, 13, 38, 45, 37, 14, 33, 7, 28, 31, 35, 5, 10, 17, 18, 47, 35, 8, 17, 2, 11, 18, 36, 2, 6, 21, 45, 10, 22, 38, 45, 22, 16, 34, 38, 23, 20, 40, 23, 2, 37, 45, 32, 40, 41, 27, 46, 2, 26, 16, 3, 17, 7, 41, 16, 25,18, 39, 34, 24, 10, 18, 19, 9, 16, 42, 29, 25, 25, 44, 29, 11, 7, 5, 2, 16, 30, 1, 11, 35, 2, 1, 18, 32, 10, 22, 34, 14, 34, 15, 42, 34, 43, 8, 34, 6, 9, 35, 25, 33, 38, 1, 27, 45, 34, 9, 34, 30, 26, 32, 11, 29, 8, 13, 48, 7, 29, 30, 33, 16, 4, 47, 17, 10, 24, 10, 15, 44, 5, 42, 39, 44, 9, 32, 7, 19, 21, 40, 37, 14, 39, 29, 13, 26"

# Convertir la cadena en una lista de números
numeros = [int(numero.strip()) for numero in cadena_SIOSI.split(",")[1:]]

# Obtener 6 números aleatorios
seis_numeros_aleatorios = random.sample(numeros, 6)

print(seis_numeros_aleatorios)

resultado =contar_numeros_repetidos(cadena_SIOSI)
print(resultado)

#print (repetidos)
print (cadena_TINKA)
print (cadena_Boliyapa)
print (cadena_SIOSI)
#
#
print ("Haz de saber que tus pensamientos son los maximos deseos de tu corazón, que al proclamarlas constantemente y ejercer la fuerza de la voluntad sobre ellos se hacen realidad")
print ( "¿como te llamas?")
nombre = input()
#
print (nombre + " Soy el Arcagel T encargado de darte las Riquezas que el padre de la creacion tiene para ti")
print ("¿Te gustaria Crear o jugar?")
respuesta = input()
#
print ("Hello " + nombre + " ¿Cual es tu maximo deseo?")
respuesta = input()
#
print ("Crees que lo lograras")
respuesta = input ()
#
print ("Hello " + nombre + ", el Arcangel T te confirma que,"" Haz de saber que tu maxino anhelo se hace realidad")
print (nombre + " ¿Dedeseas recibirlo?")
respueta = input()
#
print ("Arcangel T, dame la Bendicion que el Padre de la Creación te ha dado para mí")
mensaje = input()
print ("Bendicion Concedida")
#

import random
# l.Let's generate 6 values between 1 and 50. Store valued on a list.random

my_list = []

for _ in range (6):
  rand_num = random.randint(1, 50)
  my_list.append(rand_num)

print(my_list)

# 2 - let's generate 3 odd values between 1 and 50
my_list = []

for _ in range (3):
  num = random.randrange(1, 50, 2)
  my_list.append(num)

print(my_list)

# 3 - Generate 3 random numbers multiple of 7
for _ in range(3):
  rand_num = random.randint(1, 7)*5
  print(rand_num)

# 4 - let's generate a list with 4 sequential numbers. You hare t>

import random
# from random impot shuffle

#some_nums = [i for i in range(1, 7)]
#print (some_nums)
#random.shuffle(some_nums)
#print ("Randomized: in", some_nums)

# Convertir la cadena en una lista de números
#numeros = [int(numero.strip()) for numero in cadena_SIoSI.split(",")[1:]]

# Obtener 6 números aleatorios
#seis_numeros_aleatorios = random.sample(numeros, 6)

#print(seis_numeros_aleatorios)


print ("Bye, bye "+ nombre)
