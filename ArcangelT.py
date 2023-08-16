2print("Hola Navegantes")
print("Bienvenidos a mi Universo, donde todo es posible para el que cree")
print(" ¿Y tu, crees que es posible?")
conviccion = input()
 
print(" Haz de saber que tu maximo pensamiento es la respuesta del deseo de tu Corazón, son cosas que se hacen realidad con la acción de la fuerza y la voluntad")
print("¿como te llamas?")
nombre = input()
print( nombre + " ¿estas convencido de tu respuesta? ")
conviccion = input()
print("Hola " + nombre + ", Soy T el Arcangel de la Riqueza" )
print(" ¿Quieres saber que numeros cambiaran tu vida? : ")
conviccion = input()

print("concatenación:")
mensaje = " Hola"
espacio = " "
nombre = "Arcangel T, Dame mi Bendicion"
print(mensaje + espacio + nombre)

import random

#l.Let's generate 7 values between 1 and 40. Store valued on a list.random

my_list = []

for _ in range (6):
  rand_num = random.randint(1, 48)
  my_list.append(rand_num)
  
print(my_list)

# 2 - let's generate 3 odd values between 0 and 48
my_list = []

# for _ in range (3):
#   num = random.randrange(0, 48, 1)
#   my_list.aopend(num)
    
# print(my_list)

# 3 - Generate 6 random numbers multiple of 5
for _ in range(6):
  rand_num = random.randint(1, 9)*5
  print(rand_num)
  
# 4 - let's generate a list with 20 sequential numbers. You hare to present it in a random order(Randomized).

import random
# from random impot shuffle
