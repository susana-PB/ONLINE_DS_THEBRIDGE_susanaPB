import time
import random

def ahorcado(vidas, palabra_elegida, palabra_oculta):

    while vidas > 0: # mientras haya vidas
        time.sleep(1)
        letra_usuario = input("Introduce una letra: ")
        letra_usuario = letra_usuario.upper()

        if letra_usuario in palabra_elegida:
            for i in range(len(palabra_elegida)):
                if palabra_elegida[i] == letra_usuario:
                    palabra_oculta[i] = letra_usuario
            
            if "_" not in palabra_oculta: # quedan todavia guines? si no quedan, has ganado
                print("Has ganado!")
                print(*palabra_oculta) # con el * imprime la lista y quita corchetes y comas
                break # si se cumple, salimos del bucle

            print("Has acertado!")
            print(*palabra_oculta)

        else:
            vidas -= 1 # si no has acertado y no has ganado, te quita una vida
            print("Has fallado!")
            print(f'Vidas:{vidas}')
            print(*palabra_oculta) # con el * imprime la lista y quita corchetes y comas


            if vidas == 0: # finalmente, si las vidas llegan a 0, pierde
                print("Has perdido :(")