He planteado el ejercicio con dos clases , Jugador y Partida.
Un jugador puede ser humano o una maquina, por eso defino el tipo.
Defino la clase Partida como una clase que implementa los turnos de adivinar (hecho en dos metodos) y el juego de la partida, el cual controla los turnos, indica el resultado y la posible reiteracion de las rondas.
En el caso en el que la maquina adivina, compruebo que si por un casual el jugador se equivoca o es obvio que se equivoca al dar la respuesta (dejar un rango vacio) esta no cuenta como intento y se genera otro numero aleatorio en el mismo rango. Cuando solo queda un elemento posible lo indico y lo cuento como intento. Si la respuesta del jugador esta fuera de las opciones, el intento de la  máquina no cuenta y se genera otro número aleatorio.
