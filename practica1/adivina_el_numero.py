import random

class Jugador:
    def __init__(self, nombre):
        self.nombre=nombre

def getRandom(a,b):
	return random.randrange(a,b)

def adivina_jugador(nombre):
    intentos=1
    numero_a_adivinar=getRandom(1,100)
    numero_res=input("Bueno, {}, estoy pensando en un número entre 1 y 100. Intenta adivinarlo\n".format(nombre))
    while (numero_a_adivinar!=int(numero_res)):
        intentos+=1
        if numero_a_adivinar<int(numero_res):
            numero_res=input("Mi número es menor\n")
        else:
            numero_res=input("Mi número es mayor\n")
    print("¡Buen trabajo, {0}! ¡Has adivinado mi número en {1} intentos! Es tu turno.\n".format(nombre,intentos))
    return intentos

def adivina_maquina():
    intentos=0
    min=1
    max=100
    numero_maq=getRandom(min,max)
    res_jugador='n'
    while res_jugador!='Correcto':
        print("El numero que has pensado es {} \n".format(numero_maq))
        intentos+=1
        res_jugador=input("Mayor/Menor/Correcto? ")
        if res_jugador=='Mayor':
            min=numero_maq+1
        elif res_jugador=='Menor':  
            max=numero_maq-1
        if (min!=max):
            numero_maq=getRandom(min,max)
        else:
            numero_maq=min
    return intentos

if __name__== '__main__':
    nombre_ju=input("¡Hola! ¿cómo te llamas?\n")
    jugador=Jugador(nombre_ju)
    repetir='S'
    while (repetir=='S'):
        intentos_ju=adivina_jugador(jugador.nombre)
        intentos_ma=adivina_maquina()
        if intentos_ju>intentos_ma:
            resultado="Yo gano."
        elif intentos_ju<intentos_ma:
            resultado="Tu ganas."
        else:
            resultado="Hemos empatado."
        repetir=input("{0} He acertado en {1} intentos. Quieres seguir jugando? S/N ".format(resultado,intentos_ma))
