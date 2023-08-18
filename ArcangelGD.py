#python/ArcangelGD.py
print ("Hola Navegantes,  Hellow Navigators")
print ("Bienvenidos a mi Universo, donde todo es posible para el que cree")
print (" ¿Y tu, crees que es posible?")
conviccion = input()

print (" Haz de saber que tus maximos pensamientos son los deseos de tu Corazon, son cosas que al proclamarlas se vuelvem realidad al usar la fuerza de la accion y la voluntad")
print ("¿como te llamas?")
nombre = input()
print ( nombre + " ¿estas convencido de tu respuesta? ")
conviccion = input()
print ("Hola " + nombre + ", Soy GD el Arcangel de la Abundancia")
print (" ¿Deseas saber que numeros cambiaran tu vida? : ")
conviccion = input()
mensaje = " Hola"
nombre = " Arcangel GD, Dame la Bendicion que mi padre Celestial dueño del Oro y laPlata, te ha dado para mi"
print (nombre)
print ("... Deseo concedido")

import random

# l.Let's generate 5 random values ​​between 1 and 35 and store them in a list.
my_list = []

for _ in range (5):
  rand_num = random.randint(1, 35)
  my_list.append(rand_num)

print(my_list)

# 2 - let's generate 3 odd values between 1 and 35
my_list = []

for _ in range (3):
  num = random.randrange(0, 35, 1)
  my_list.append(num)
    
print(my_list)

# 3 - Generate 3 random numbers multiple of 5
for _ in range(3):
  rand_num = random.randint(1, 7)*5
  print(rand_num)
  
# 4 - let's generate a list with 20 sequential numbers. You hare to present it in a random order(Randomized).

import random
# from random impot shuffle


# print(my_list)


