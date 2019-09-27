import random

class Jugador:
    def __init__(self, nombre,tipo):
        self.nombre=nombre
        self.tipo=tipo
        self.intentos=0

def getRandom(a,b):
	return random.randrange(a,b)

class partida:
    
    def adivina_jugador(self,nombre,jugador):
        numero_a_adivinar=getRandom(1,100)
        numero_res=input("Bueno, {}, estoy pensando en un número entre 1 y 100. Intenta adivinarlo\n".format(nombre))
        jugador.intentos=1
        while (numero_a_adivinar!=int(numero_res)):
            jugador.intentos+=1
            if numero_a_adivinar<int(numero_res):
                numero_res=input("Mi número es menor\n")
            else:
                numero_res=input("Mi número es mayor\n")
        print("¡Buen trabajo, {0}! ¡Has adivinado mi número en {1} intentos! Es tu turno.\n".format(nombre,jugador.intentos))

    def adivina_maquina(self,maquina):
        min=1
        max=100
        numero_maq=getRandom(min,max)
        res_jugador='n'
        maquina.intentos=0
        while res_jugador!='Correcto':
            print("El numero que has pensado es {} \n".format(numero_maq))
            maquina.intentos+=1
            res_jugador=input("Mayor/Menor/Correcto? ")
            if res_jugador=='Mayor':
                if max!=numero_maq:
                    min=numero_maq+1
                else:
                    maquina.intentos-=1
            elif res_jugador=='Menor':
                if min!=numero_maq:
                    max=numero_maq-1
                else:
                    maquina.intentos-=1
            if (min!=max):
                numero_maq=getRandom(min,max)
            else:
                print("Solo queda un numero posible, el {} es tu numero.\n".format(min))
                maquina.intentos+=1
                break
        
    def jugar_partida(self):
        maquina=Jugador('CPU','Maquina')
        nombre_ju=input("¡Hola! ¿cómo te llamas?\n")
        jugador=Jugador(nombre_ju,'Humano')
        repetir='S'
        while (repetir=='S'):
            self.adivina_jugador(jugador.nombre,jugador)
            self.adivina_maquina(maquina)
            if jugador.intentos>maquina.intentos:
                resultado="Yo gano."
            elif jugador.intentos<maquina.intentos:
                resultado="Tu ganas."
            else:
                resultado="Hemos empatado."
            repetir=input("{0} He acertado en {1} intentos. Quieres seguir jugando? S/N ".format(resultado,maquina.intentos))

if __name__== '__main__':
    nueva_partida=partida()
    nueva_partida.jugar_partida()
