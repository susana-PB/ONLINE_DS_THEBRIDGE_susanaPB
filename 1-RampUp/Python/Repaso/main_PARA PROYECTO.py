



import random # Nos hace el import de las variables y las funciones
from variables import LISTA_PALABRAS, VIDAS # llama a variables
from funciones import ahorcado # llama a funciones

palabra_elegida = random.choice(LISTA_PALABRAS) # elije aleatoriamente entre la lista de palabras en variables
palabra_elegida = palabra_elegida.upper()

palabra_oculta = "_" * len(palabra_elegida) 
palabra_oculta = list(palabra_oculta)

print("Bienvenido al juego del ahorcado, disfruta bastante!")

ahorcado(vidas= VIDAS, palabra_elegida=palabra_elegida, palabra_oculta=palabra_oculta)
# ahorcado es una funcion que está definida en funciones
# 