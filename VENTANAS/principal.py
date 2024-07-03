'''
-----------------------
nombres: Matías Adrian
apellido: Ramos
División 314
DNI: 46894213

-----------------------
nombres: Rodrigo Martín
apellido: Pettico
División 314
DNI: 34623153
-------------------
'''
from pygame import *
from constantes import *
from menu import *
from juego import *
from opciones import *
from terminado import *
from puntuaciones import *
from agregar_preguntas import *
from parsear_preguntas import *
import opciones
import juego
import pygame

pygame.init()
pantalla = pygame.display.set_mode(PANTALLA)
pygame.display.set_caption("Preguntados")
ventana_actual = 'menu'
corriendo = True
bandera_juego = True
bandera_puntuaciones  = True
bandera_terminado = True
bandera_menu = True
FPS = 60
clock = pygame.time.Clock()

while corriendo:
    clock.tick(FPS)
    
    if ventana_actual == 'menu':
        if bandera_menu:
            pygame.mixer.music.load(f"{RUTA_DE_ACCCESO}\VENTANAS\musica_menu.mp3") #Define musica de fondo mientras juego
            pygame.mixer.music.play(1)
           # pygame.mixer.music.set_volume(opciones.volumen / 100)
            bandera_menu = False

        ventana_actual = mostrar_menu(pantalla,pygame.event.get())
        bandera_puntuaciones  = True
        
    elif ventana_actual == 'opciones':
        ventana_actual = mostrar_opciones(pantalla,pygame.event.get())
        pygame.mixer.music.set_volume(opciones.volumen / 100)
    
    elif ventana_actual == 'juego':    
        if bandera_juego:
            pygame.mixer.music.load(f"{RUTA_DE_ACCCESO}\VENTANAS\musica_juego.mp3")
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(opciones.volumen / 100)
            bandera_juego = False
        
        
        ventana_actual = mostrar_juego(pantalla, pygame.event.get())

    elif ventana_actual == 'puntuaciones':
        if bandera_menu == False:
            pygame.mixer.music.stop()
            
        
        if bandera_puntuaciones:
            pygame.mixer.music.load(f"{RUTA_DE_ACCCESO}\VENTANAS\musica_top_10.mp3")
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(opciones.volumen / 100)
            
        bandera_puntuaciones  = False
        bandera_menu = True

        ventana_actual = mostrar_puntuaciones(pantalla,pygame.event.get())
    
    elif ventana_actual == 'agregar_preguntas':
        ventana_actual = agregar_preguntas(pantalla,pygame.event.get(),)

    

    elif ventana_actual == 'terminado':
        if bandera_juego == False:
            pygame.mixer.music.stop()
            bandera_juego = True
            pygame.mixer.music.load(f"{RUTA_DE_ACCCESO}\VENTANAS\musica_terminado.mp3")
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(opciones.volumen / 100)

        ventana_actual = mostrar_juego_terminado(pantalla,pygame.event.get(),juego.puntuacion)
    
    elif ventana_actual == 'salir':
        corriendo = False
            
    pygame.display.flip()

    if ventana_actual == 'juego' and juego.timer <= 0:
        ventana_actual = 'terminado'

pygame.quit()
