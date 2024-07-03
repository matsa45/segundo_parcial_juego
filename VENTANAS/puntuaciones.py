import pygame 
from constantes import *
from parsear_puntuaciones import mejores_diez
from pygame import *

pygame.init()

fuente = pygame.font.SysFont("Arial Narrow",32)
fuente_boton = pygame.font.SysFont("Arial Narrow",23)
fuente_top = pygame.font.SysFont("Mongolian Baiti",28)

imagen_top_10 = image.load('top_10.png')
imagen_top_10 = transform.scale(imagen_top_10,(150,150))

boton_volver = {"superficie":pygame.Surface(TAMAÑO_BOTON_VOLVER),"rectangulo":pygame.Rect(0,0,0,0)}
boton_volver['superficie'].fill(COLOR_AZUL)

click_sonido = pygame.mixer.Sound(f"{RUTA_DE_ACCCESO}\VENTANAS\click.mp3")
click_sonido.set_volume(1)

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


def mostrar_puntuaciones(pantalla:pygame.Surface,eventos):
    global volumen

    retorno = "puntuaciones"
    
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_volver['rectangulo'].collidepoint(evento.pos):
                    click_sonido.play()
                    retorno = "menu"
        elif evento.type == pygame.QUIT:
            retorno = "salir"
            
    pantalla.fill(COLOR_DORADO)

    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'],(5,5))
    
    nombre_top_10 = ''
    fecha_top_10 = ''
    puntuacion_top_10 = ''
    top_10 = mejores_diez()
    
    for i in top_10:
        nombre = i['nombre']
        if len(nombre) > 10:
            nombre = nombre[:10] + '...'
        fecha = i['fecha']
        puntuacion = i['puntuacion']
        nombre_top_10 += f'{nombre}\n'
        fecha_top_10 += f'{fecha}\n'
        puntuacion_top_10 += f'{puntuacion}\n'
    

    blit_text(boton_volver['superficie'],"VOLVER",(10,10),fuente_boton,COLOR_BLANCO)
    blit_text(pantalla,f' \n{nombre_top_10}',(3,150),fuente_top,COLOR_NEGRO)
    blit_text(pantalla, f'\n{fecha_top_10}', (200, 150),fuente_top,COLOR_NEGRO) 
    blit_text(pantalla, f'\n{puntuacion_top_10}', (400, 150),fuente_top,COLOR_NEGRO)
    pantalla.blit(imagen_top_10, (180,0))

    return retorno
