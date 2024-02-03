#¡  /python/NumerosAk.py
#este es un recopilador de datos
print ("Hola Navegantes")
print ("Hello World - Hellow navigators")
print ("Bienvenidos a mi Universo, donde todo es posible para el que cree")
print (" ¿Y tu, crees que es posible?")
conviccion = input()


#print("El nombre de tu script es $0")

'''
Buscar numerosPA repetidos de Pozo Acumulado
Buscar nunerosCha repetidos de chau chamba
'''

'''
Encontrar los numeros repetidos de una lis
'''

#Pozo Acumulado
#Chau Chamba

print ("Sorteo 1527 29/07/2023")
numerosPA = [21, 6, 20, 58, 10, 18, 40, 17, 23]
numerosCha = [ 38, 2, 3, 6, 15, 19]

print ("Sorteo 1525 25/07/2023")
numerosPA = [33, 16, 9, 35, 19, 18]
numerosCha = [6, 4, 12, 26, 2, 29]

("Sorteo 1524 22/07/2023")
numerosPA = [2, 37, 36, 34, 40, 5]
numerosCha = [8, 6, 3, 33, 36, 35]

print ("Sorteo 1523 20/07/2023")
numerosPA = [28, 5, 23, 9, 18, 32]
numerosCha = [10, 40, 8, 16, 2, 1]

print ("Sorteo 1522 18/07/2023")
numerosPA = [23, 33, 31, 22, 40, 10]
numerosCha = [6, 5, 27, 33, 9, 3]

print ("Sorteo 1521 15/07/2023")
numerosPA = [23, 1, 10, 21, 5, 33]
numerosCha = [14, 22, 3, 38, 2, 32]

print ("Sorteo 1520 13/07/2023")
numerosPA = [32, 36, 34, 25, 23, 21]
numerosCha = [33, 36, 39, 32, 23, 2]

print ("Sorteo 1519 11/07/2023")
numerosPA = [38, 31, 10, 6, 13, 25]
numerosCha = [36, 18, 6, 25, 7, 4]

print ("Sorteo 1518 08/07/2023")
numerosPA = [30, 20, 9, 40, 5, 11]
numerosCha = [13, 40, 39, 36, 10, 26]

print ("Sorteo 18517 06/07/2023")
numerosPA = [24, 3, 34, 7, 15, 14]
numerosCha = [17, 2, 36, 25, 6, 13]

print ("Sorteo 1516 04/07/2023")
print ("Sorteo 1515 01/07/2023")
print ("Sorteo 1514 29/06/2023")
print ("Sorteo 1513 27/06/2023")


numeros = [   30, 28, 1, 31, 20, 6, 1, 28, 13, 5, 2, 17, 23, 6, 30, 18, 27, 1, 29, 13, 2, 28, 33, 7]
numerosChauCh = [  17, 37, 20, 32, 11, 2, 2, 39, 9, 32, 6, 28, 9, 20, 23, 28, 6, 21, 4, 7, 24, 8, 34, 35]




repetidos = []
archivo = []


# 1 Busquemos números repetidos entre 0 y 40
mi_lista = []

import time


# Forma no eficiente

t0 = time.time()

repetidos = []

#for i in range (len(numeros)):
   # for j in range (len(numeros)):
       # if i != j:
           # if numeros [1] = numeros [j] and numeros [i] not in repetidos:
               # repetidos.append(numeros[i])


# print (repetidos)

import random
import time
print (repetidos)
print (numeros)
print (numerosChauCh)
#
#
print ("Haz de saber que tus pensamientos son los maximos deseos de tu corazón, que al proclamarlas constantemente y ejercer la fuerza de la voluntad sobre ellos se hacen realidad")
print ( "¿como te llamas?")
nombre = input()
print ("Hello " + nombre + " ¿Cual es tu maximo deseo?")
respuesta = input()
print ("Crees que lo lograras")
respuesta = input ()
print (nombre + " Soy el Arcagel T encargado de darte las Riquezas que el padre de la creaciln tiene para ti")
print ("¿Te gustaria Crear o jugar?")
respuesta = input()
print ("Hello " + nombre + ", Soy el Arcangel K ,  Haz de saber que tus pensamientos son los maximos deseos de tu corazón, que al proclamarlas constantemente     que al proclamarlas constantemente y ejercer la fuerza de la voluntad sobre ellos se hacen realidad")
print (nombre + " ¿Dedeseas recibirlo?")
respueta = input()
print ("Arcangel K, dame la Bendicion que el Padre de la Creación te ha dado para mi")
mensaje = input()

print ("Bendicion Concedida")

import random
# l.Let's generate 7 values between 0 and 48. Store valued on a l>

my_list = []

for _ in range (6):
  rand_num = random.randint(1, 48)
  my_list.append(rand_num)

print(my_list)

# 2 - let's generate 3 odd values between 1 and 48
my_list = []

for _ in range (3):
   num = random.randrange(1, 48, 2)
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

print (repetidos)

t1 = time.time()

print (repetidos)
print (t1-t0)

# Forma eficiente

repetidos = []
archivo = []

t2 = time.time()

for n in numeros:
    if n not in archivo:
       archivo.append(n)

t3 = time.time()

print (repetidos)
print (t3-t2)
print (numerosAP)
print (numerosCha)


print ("Bye, bye"+ nombre)
