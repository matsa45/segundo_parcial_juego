import pygame
from constantes import *
from parsear_puntuaciones import *
from juego import guardar_puntuacion
from datetime import datetime

juego_terminado_imagen = pygame.image.load('game_over.png')
juego_terminado_imagen = pygame.transform.scale(juego_terminado_imagen, (250, 250))

pygame.init()

fuente = pygame.font.SysFont("Arial Narrow", 40)
fuente_arcade = pygame.font.Font("fuente_arcade.ttf", 30)
fuente_nombre = pygame.font.Font("fuente_arcade.ttf", 35)

cuadro = {"superficie": pygame.Surface(CUADRO_NOMBRE), "rectangulo": pygame.Rect(0, 0, 0, 0)}
cuadro['superficie'].fill(COLOR_NEGRO)
nombre = ""


UPDATE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(UPDATE_EVENT, 100)

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

def mostrar_juego_terminado(pantalla: pygame.Surface, eventos, puntaje):
    retorno = "terminado"
    
    global nombre
    for evento in eventos:
        if evento.type == pygame.KEYDOWN:
            bloc_mayus = pygame.key.get_mods() and pygame.KMOD_CAPS
            letra_presionada = pygame.key.name(evento.key)
                        
            if letra_presionada == 'backspace' and len(nombre) > 0:
                nombre = nombre[:-1]  # Elimino el último
                cuadro['superficie'].fill(COLOR_NEGRO)  # limpio la superficie de su texto anterior

            if letra_presionada == 'space' and len(nombre) > 0:
                nombre += " "
            
            if letra_presionada.isalpha() and letra_presionada != '' and len(letra_presionada) == 1 and len(nombre) < 10:
                nombre += letra_presionada.upper()
            
            

            if letra_presionada == 'return' and len(nombre) > 0:
                retorno = "salir"
                fecha = datetime.now()
                puntuacion = cargar_puntuacion()
                partidas_json(nombre, fecha, puntuacion)    

        elif evento.type == pygame.QUIT:
            retorno = "salir"

        elif evento.type == UPDATE_EVENT:
            pantalla.fill(COLOR_NEGRO)
            cuadro['rectangulo'] = pantalla.blit(cuadro['superficie'], (180, 310))
            blit_text(pantalla, f"INGRESAR\n   NOMBRE", (15, 300), fuente_arcade, COLOR_BLANCO)
            blit_text(cuadro['superficie'], nombre, (10, 0), fuente_nombre, COLOR_BLANCO)
            blit_text(pantalla, f"Usted obtuvo: {puntaje} puntos", (50, 170), fuente_arcade, COLOR_BLANCO)
            pantalla.blit(juego_terminado_imagen, (120, -50))

    return retorno