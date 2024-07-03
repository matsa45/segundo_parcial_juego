import pygame
from parsear_preguntas import lista_preguntas
import random
import json
import opciones
from constantes import *
from pygame import *
from opciones import *

corazon_imagen = image.load('corazon.png')
corazon_imagen = transform.scale(corazon_imagen,(30,30))

corazon_vacio_imagen = image.load('corazon_vacio.png')
corazon_vacio_imagen = transform.scale(corazon_vacio_imagen,(30,30))



def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height
pygame.init()

carta_pregunta = {"superficie":pygame.Surface(TAMAÑO_PREGUNTA),"rectangulo":pygame.Rect((0,0,0,0))}
carta_pregunta['superficie'].fill(COLOR_BLANCO)

cartas_respuestas = [
    {"superficie":pygame.Surface(TAMAÑO_RESPUESTA),"rectangulo":pygame.Rect((0,0,0,0))},#R1 -> 0
    {"superficie":pygame.Surface(TAMAÑO_RESPUESTA),"rectangulo":pygame.Rect((0,0,0,0))},#R2 -> 1
    {"superficie":pygame.Surface(TAMAÑO_RESPUESTA),"rectangulo":pygame.Rect((0,0,0,0))},#R3 -> 2
    {"superficie":pygame.Surface(TAMAÑO_RESPUESTA),"rectangulo":pygame.Rect((0,0,0,0))} #R4 -> 3
]

for carta in cartas_respuestas:
    carta['superficie'].fill(COLOR_AZUL)



fuente_pregunta = pygame.font.SysFont("Arial Narrow",30)
fuente_respuesta = pygame.font.SysFont("Arial Narrow",20)
fuente_puntuacion = pygame.font.SysFont("Arial Narrow",25)
fuente_reloj = pygame.font.Font("DS-DIGIT.TTF", 30)

puntuacion = 0
random.shuffle(lista_preguntas)
indice_pregunta = 0


error_sonido = pygame.mixer.Sound(f"{RUTA_DE_ACCCESO}\VENTANAS\error.mp3")

correcto_sonido = pygame.mixer.Sound(f"{RUTA_DE_ACCCESO}\VENTANAS\correcto_sfx.mp3")


def guardar_puntuacion(puntuacion):
    puntuacion = str(puntuacion)
    with open("puntuacion.json", "w") as archivo:
        json.dump({"puntuacion": puntuacion}, archivo)

def cargar_puntuacion():
    with open("puntuacion.json", "r") as archivo:
        datos = json.load(archivo)
        return datos.get("puntuacion", 0)


import time


oportunidades = 3
contador_preguntas = 0
start_time = None


def mostrar_juego(pantalla:pygame.Surface,eventos):
    global start_time
    global timer
    global indice_pregunta
    global segundos_transcurridos
    global puntuacion 
    global oportunidades
    global contador_preguntas
    
    if start_time is None:
        start_time = time.time()

    tiempo_actual = time.time()
    segundos_transcurridos = int(tiempo_actual - start_time)

    retorno = "juego"
    pregunta = lista_preguntas[indice_pregunta]
    
    timer = int(opciones.timer - segundos_transcurridos)

    if timer <= 0 or oportunidades == 0 or contador_preguntas >= len(lista_preguntas):
        retorno = "terminado"


    if retorno != 'terminado' and retorno != 'salir':
        for evento in eventos:
            
            if evento.type == pygame.QUIT:
                retorno = "salir"
                    
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                
                    for i in range(len(cartas_respuestas)):
                    
                        if cartas_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                            if i == 0:
                                respuesta = 'a'
                            elif i == 1:
                                respuesta = 'b'
                            else:
                                respuesta = 'c'

                            if pregunta['respuesta_correcta'] == respuesta :
                                correcto_sonido.set_volume(opciones.volumen / 100)
                                correcto_sonido.play()

                                carta_pregunta['superficie'].fill((COLOR_BLANCO))
                                for carta in cartas_respuestas:
                                    carta['superficie'].fill(COLOR_AZUL)
                            
                                indice_pregunta+=1    

                                if indice_pregunta != len(lista_preguntas):
                                    pregunta = lista_preguntas[indice_pregunta]
                                else:
                                    indice_pregunta = 0
                                    random.shuffle(lista_preguntas)
                                    pregunta = lista_preguntas[indice_pregunta]
                            
                                puntuacion += 100
                        
                            elif pregunta['respuesta_correcta'] != respuesta:
                                error_sonido.set_volume(opciones.volumen / 100)
                                error_sonido.play()
                            
                                if puntuacion <= 0:
                                    puntuacion = 0
                                else:
                                    puntuacion -= 50
                            
                                carta_pregunta['superficie'].fill((COLOR_BLANCO))
                                for carta in cartas_respuestas:
                                    carta['superficie'].fill(COLOR_AZUL)
                            
                                indice_pregunta += 1    

                                oportunidades -= 1
                            
                                                    
                                if indice_pregunta != len(lista_preguntas):
                                    pregunta = lista_preguntas[indice_pregunta]
                                else:
                                    indice_pregunta = 0
                                    random.shuffle(lista_preguntas)
                                    pregunta = lista_preguntas[indice_pregunta]
                            

                            contador_preguntas += 1

                        
    else:
        return retorno
                      
                        


    
    cuadro_imagen = image.load('cuadro.png')
    cuadro_imagen = transform.scale(cuadro_imagen,(500,300))

    pantalla.fill(COLOR_BLANCO)

    pantalla.blit(carta_pregunta['superficie'],(80,50))
    pantalla.blit(cuadro_imagen, (10,-10))

    blit_text(carta_pregunta['superficie'],pregunta['pregunta'],(10,10),fuente_pregunta)
    



    cartas_respuestas[0]['rectangulo'] = pantalla.blit(cartas_respuestas[0]['superficie'],(125,215))
    blit_text(cartas_respuestas[0]['superficie'],pregunta['respuesta_a'],(10,10),fuente_respuesta,COLOR_BLANCO)
   
    cartas_respuestas[1]['rectangulo'] = pantalla.blit(cartas_respuestas[1]['superficie'],(125,285))
    blit_text(cartas_respuestas[1]['superficie'],pregunta['respuesta_b'],(10,10),fuente_respuesta,COLOR_BLANCO)
   
    cartas_respuestas[2]['rectangulo'] = pantalla.blit(cartas_respuestas[2]['superficie'],(125,355))
    blit_text(cartas_respuestas[2]['superficie'],pregunta['respuesta_c'],(10,10),fuente_respuesta,COLOR_BLANCO) 

    
    blit_text(pantalla,f"{puntuacion} puntos",(10,10),fuente_puntuacion,COLOR_NEGRO)


    if oportunidades == 3:
        pantalla.blit(corazon_imagen, (350 ,5))
        pantalla.blit(corazon_imagen, (385, 5))
        pantalla.blit(corazon_imagen, (420, 5))
    
    elif oportunidades == 2:
        pantalla.blit(corazon_imagen, (350, 5))
        pantalla.blit(corazon_imagen, (385, 5))
        pantalla.blit(corazon_vacio_imagen, (420, 5))
    elif oportunidades == 1:
        pantalla.blit(corazon_imagen, (350, 5))
        pantalla.blit(corazon_vacio_imagen, (385, 5))
        pantalla.blit(corazon_vacio_imagen, (420, 5))

    minutos = timer // 60
    segundos = timer % 60 
    blit_text(pantalla, f"{minutos:02}:{segundos:02}", (200, 10), fuente_reloj, COLOR_NEGRO)
  
    guardar_puntuacion(puntuacion)

    return retorno

