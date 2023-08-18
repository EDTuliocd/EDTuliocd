#python/ArcangelT
print ("Hello Navegantes")
print ("Bienvenidos a mi Universo, donde todo es posible para el que cree")
print (" ¿Y tu, crees que es posible?")
conviccion = input()
 
print (" Haz de saber que tu maximo pensamiento es la respuesta del deseo de tu Corazón, ")
print ("¿como te llamas?")
nombre = input()
print ( nombre + " ¿estas convencido de tu respuesta? ")
conviccion = input()
print ("Hola " + nombre + ", Soy T el Arcangel de la Riqueza" )
print (" ¿Dedeas saber que numeros cambiaran tu vida? : ")
conviccion = input()

nombre = "Arcangel T, Dame la Bendicion que mi Padre Celestial dueño del Oro y la Plata te ha dado para mi"
print ( nombre)
print ("...Deseo concedido")

import random

#l.Let's generate 6 values between 1 and 48. Store valued on a list.random

my_list = []

for _ in range (6):
  rand_num = random.randint(1, 48)
  my_list.append(rand_num)
  
print(my_list)

# 2 - let's generate 3 odd values between 1 and 48
my_list = []

for _ in range (3):
  num = random.randrange(0, 48, 1)
  my_list.append(num)
    
print(my_list)

# 3 - Generate 3 random numbers multiple of 5
for _ in range(3):
  rand_num = random.randint(1, 9)*5
  print(rand_num)
  
# 4 - let's generate a list with 20 sequential numbers. You hare to present it in a random order(Randomized).

import random
# from random impot shuffle
