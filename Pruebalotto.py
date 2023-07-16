#<!CODTYPE html>
#<html>
# Top-most EditorConfig file

# Esto es una prueba/
print("Hello World - Hello Navigators")
print("Bienvenido a mi Universo, donde todo es posible para el que cree")
print("¿Y tu crees que es posible?")
conviction = input()
print("Haz de saber que tus pensamientos son los deseos de tu corazón")
print( "¿como te llamas?")
nombre = input()
print("Hello " + nombre + " ¿Cual es tu maximo deseo?")
respuesta = input()
print("Crees que lo lograras")
respuesta = input()

print("Somos los Arcageles de la Abundancia -K, Prosperidad -GD y Riqueza -T")
print("¿Te gustaria Crear o jugar?")
respuesta = input()
print("Con cual de los Arcangeles te gustaria recibir tu Bendicion")
arcangel = input()
print("Hello " + nombre + ", Soy el Arcangel " + arcangel + ", Haz de saber que tu maxino anhelo se hace realidad")
print(nombre + " ¿Dedeseas recibirlo?")
respueta = input()
print("Arcangel " + arcangel + " dame la Bendion que el Padre de la Creación te ha dado para mí")

mensaje = input()

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

#</html>

