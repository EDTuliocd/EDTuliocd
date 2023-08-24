#¡  /Python/NumerosAT.p
# Este es un recopilador de datos
print ("Hola Navegantes")
print ("Hello World - Hellow navigators")
print ("Bienvenidos a mi Universo, donde todo es posible para el que cree")
print (" ¿Y tu, crees que es posible?")
conviccion = input ()

# print("El nombre de tu script es $0")

'''
Buscar numeros repetidos de numeros
Buscar numeros repetidos de numerosBoliyapa
Buscar nuneros repetidos de numerosSíoSí
'''

print ("Sorteo 1010 - 09/08/2023")
print ("Sorteo 1009 - 06/08/2023")
print ("Sorteo 1008 - 02/08/2023")
print ("Sorteo 1007 - 30/07/2023")
print ("Sorteo 1006 - 26/07/2023")
print ("Sorteo 1005 - 23/07/2023")
print ("Sorteo 1004 - 19/07/2023")
print ("Sorteo 1003 - 16/07/2023")
print ("Sorteo 1002 - 12/07/2023")
print ("Sorteo 1001 - 09/07/2023")
print ("Sorteo 1000 - 05/07/2023")
print ("Sorteo 999 - 02/07/2023")
print ("Sorteo 998 - 28/06/2023")
print ("Sorteo 997 - 25/06/2023")
print ("Sorteo 996 - 21/06/2023")
print ("Sorteo 995 - 18/06/2023")
print ("Sorteo 994 - 14/06/2023")
#
#
numeros = [32, 42, 23, 2, 24, 27, 47, 25, 39, 35, 27, 6, 42, 38, 5, 33, 16, 12, 40, 21, 39, 13, 17, 26, 24, 15, 39, 15, 38, 31, 9, 26, 43, 6, 38, 35, 23, 9, 31, 32, 48, 24, 44, 33, 25, 1, 13, 20, 42, 27, 23, 26, 38, 29, 21, 6, 11, 34, 28, 11, 1, 24, 5, 12, 43, 20, 10, 13, 22, 35, 43, 34, 14, 7, 38, 19, 26, 23, 25, 2, 11, 26, 1, 38, 13, 42, 30, 29, 13, 27, 21, 25, 11, 27, 2, 22, 9, 18, 41]

numerosBoliyapa = [25, 9, 4, 30, 22, 34, 10, 2, 41, 45, 30, 31, 20, 3, 43, 40, 14]

numerosSíoSí = [45, 34, 9, 34, 30, 26, 32, 11, 29, 8, 13, 48, 7, 29, 30, 33, 16, 4, 47, 17, 10, 24, 10, 15, 44, 5, 42, 39, 44, 9, 32, 7, 19, 21, 40, 37, 14, 39, 29, 13, 26] 

repetidos = []
archivo = []


for i in range(len (numeros)) :
    for j in range(len(numeros)) :
        if i != j:
            if numeros[1] == numeros [j] and numeros [i] not in repetidos:
                repetidos.append(numeros[i])
#   for n in numeros:
#    if n not in archivo:
#         archivo.append(n)
#    else:
#         repetidos.append(n)

# for i in range(len(numeros)):
#   for j in range(len(numeros)):
#       if i != j:
#          if numeros(i) == numeros[j] and numeros[i] not in repe>
#             repetidos. append(numeros[i])

# print (repetidos)

import random
import time
print (repetidos)
print (numerosBoliyapa)
print (numerosSíoSí)
#
#
print ("Haz de saber que tus pensamientos son los maximos deseos de tu corazón")
print ( "¿como te llamas?")
nombre = input()
print ("Hello " + nombre + " ¿Cual es tu maximo deseo?")
respuesta = input()
print ("Crees que lo lograras")
print ("Somos los Arcageles de la Abundancia -K, Prosperidad -GD y Riqueza -T")
print ("¿Te gustaria Crear o jugar?")
respuesta = input()
print ("Con cual de los Arcangeles te gustaria recibir tu Bendicion")
arcangel = input()
print ("Hello " + nombre + ", Soy el Arcangel " + arcangel + ", Haz de saber que tu maxino anhelo se hace realidad")
print (nombre + " ¿Dedeseas recibirlo?")
respueta = input()
print ("Arcangel " + arcangel + " dame la Bendicion que el Padre la Creación te ha dado para mí")

mensaje = input()

print ("Concedido")

import random
# l.Let's generate 6 values between 1 and 48. Store valued on a list.random

my_list = []

for _ in range (6):
  rand_num = random.randint(1, 48)
  my_list.append(rand_num)

print(my_list)

# 2 - let's generate 3 odd values between 1 and 48
my_list = []

for _ in range (3):
  num = random.randrange(0, 48, 2)
  my_list.append(num)

print(my_list)

# 3 - Generate 3 random numbers multiple of 7
for _ in range(3):
  rand_num = random.randint(1, 7)*5
  print(rand_num)

# 4 - let's generate a list with 4 sequential numbers. You hare t>

import random
# from random impot shuffle

some_nums = [i for i in range(1, 48)]
print (some_nums)
random.shuffle(some_nums)
print ("Randomized: in", some_nums)


