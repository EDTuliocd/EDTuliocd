# Prueba/
mensaje = "Bienvenido a mi Universo, donde todo es posible para el que cree"
mensaje = "¿Y tu crees que es posible?"
mensaje = "¿como te llamas?"
nombre =  " "
mensaje = input()
mensaje += " "
mensaje += "Loteria"
print(mensaje)

print("concatenación:")

mensaje = "Hola"
espacio = " "
nombre = "Lottery"
print(mensaje + espacio + nombre)

mensaje = input(

import random

#l.Let's generate 10 values between 5 and 50. Store valued on a list.random

my_list = []

for _ in range (5):
  rand_num = random.randint(1, 50)
  my_list.append(rand_num)
  
print(my_list)

# 2 - let's generate 20 odd values between 0 and 100
my_list = []

# for _ in range (20):
#   num = random.randrange(0, 50, 2)
#   my_list.aopend(num)
    
# print(my_list)

# 3 - Generate 10 random numbers multiple of 5
for _ in range(10):
  rand_num = random.randint(1, 10)*5
  print(rand_num)
  
# 4 - let's generate a list with 20 sequential numbers. You hare to present it in a random order(Randomized).

import random
# from random impot shuffle

some_nums = [i for i in range(1, 21)]
print(some_nums)
random.shuffle(some_nums)
print("Randomized: in", some_nums)



