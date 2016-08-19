#!/usr/bin/python
# -*- coding: utf-8 -*-
### Autor Cesar Chirinos
### Fecha 19 Agosto 2016
### publicado en https://stickybitshell.wordpress.com
 
import random
 
# Programa que emula el sorteo del Kino, no pretendo introducirlos en juegos de azar solo que no he visto nada sobre esto en internet y hace tiempo lo busque y es una de las cosas pendientes que tengo
 
kino_jugado = [1, 3, 4, 5, 6, 10, 11, 13, 15, 17, 18, 19, 20, 21, 23]
kino_jugado2 = [1, 2, 3, 4, 6, 8, 9, 12, 13, 15, 17, 19, 20, 24,25]
lista_de25 = []
sorteo = 1
 
 
#while kino_jugado2 !=  lista_de25: # Iteramos 10 Veces
while sorteo < 21: # Iteramos 10 Veces
 
    num_metidos = 0
    lista25 = range (1 , 25)  # Creamos la lista del 1 a 15, recuerda que range no agrega el ultimo indice
 
    for i in range(1 , 10): # Iteramos 10 Veces
 
 
        lista_de25 = lista25  # Cambiamos el nombre de la lista por si algun error
 
        cuanots_hay = len( lista_de25 ) # contamos cuantos elementos hay, recuerda que la lista varia y pierde un elemenrto por ciclo y no queremos ese horrible error de fuera de rango
     
        x = random.randrange(cuanots_hay) # Buscams un numero Aleatorio
     
        sacar_numero = lista_de25.pop(x) # Pasamos el numero aleatorio y lo sacamos del Sorteo
       

### Esto es lo nuevo, iteramos sobre uno de los 2 kinos el jugado o el ganador y asi verificamos cuantos aciertos tenemos
    for h in lista_de25: # Iteramos sobre el ganador
       
  
        if h in kino_jugado2:
	      num_metidos += 1
	      
    
### Aqui la asalida importante
    print "en el sorteo",  sorteo , "Has metido" ,      num_metidos

### Ahora verificamos cuantos metimos contandolos a el ojo, por eso escribo codigos imagina hacer esto 1 millon de veces :S
    print "Tu jugaste:",  kino_jugado2 , "y el ganador es",  lista_de25 
    sorteo += 1
    
    if kino_jugado2 == lista_de25:
            print "En el sorteo:",  sorteo , ", Has metido" ,      num_metidos
            print "Tu jugaste:",  kino_jugado2 , "y el ganador es",  lista_de25 

 
# Utilizamos pop pero podiamos usar del, te invito a hacerlo😀, utilice pop para luego crear otra lista con los numeros
# que vayamos sacando y sacar los 15 como en efecto lo hacen naturalmente
