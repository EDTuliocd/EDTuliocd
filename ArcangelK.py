# python/ArcangelK.py
print ("Hola Navegantes - Hello World - Hello Navigators")
print ("Bienvenidos a mi Universo, donde todo es posible para el que cree")
print (" ¿Y tu, crees que es posible?")
conviccion = input()

print (" Haz de saber que tus maximos pensamientos son la respuesta del deseo de tu Corazón, son cosas que se vuelven realidad al proclamarlas con la accion de la fuerza y la voluntad  ")
print ("¿como te llamas?")
nombre = input()
print ( nombre + " ¿estas convencido de tu respuesta? ")
conviccion = input()
print ("Hola " + nombre + ", Soy K el Arcangel de la Prosperidad" )
print (" ¿Deseas saber que numeros cambiaran tu vida? ")
conviccion = input()

print ("Arcangel K, Dame la Bendicion que mi padre celestial dueño del Oro y la Plata te ha dado para mi")
print ("...Deseo concedido")
import random

#l.Let's generate 6 values between 1 and 40. Store valued on a list.random

my_list = []

for _ in range (6):
  rand_num = random.randint(1, 40)
  my_list.append(rand_num)

print(my_list)

# 2 - let's generate 3 odd values between 0 and 40
my_list = []

for _ in range (3):
  num = random.randrange(0, 40, 2)
  my_list.append(num)

print(my_list)

# 3 - Generate 3 random numbers multiple of 5
for _ in range(3):
  rand_num = random.randint(1, 8)*5
  print(rand_num)

# 4 - let's generate a list with 20 sequential numbers. You hare to present it in a random order(Randomized).

import random
# from random impot shuffle

