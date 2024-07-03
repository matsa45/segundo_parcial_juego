import pygame
from constantes import *
from pygame import *

pygame.init()

fuente_menu = pygame.font.SysFont("Arial Narrow",30)

imagen_preguntados = image.load('preguntados_menu.png')
imagen_preguntados = transform.scale(imagen_preguntados,(420,120))



boton_jugar = {"superficie":pygame.Surface(TAMAÑO_BOTON),"rectangulo":pygame.Rect(0,0,0,0)}
boton_jugar['superficie'].fill(COLOR_AZUL)

boton_agregar_preguntas = {"superficie":pygame.Surface(TAMAÑO_BOTON),"rectangulo":pygame.Rect(0,0,0,0)}
boton_agregar_preguntas['superficie'].fill(COLOR_AZUL)

boton_salir = {"superficie":pygame.Surface(TAMAÑO_BOTON),"rectangulo":pygame.Rect(0,0,0,0)}
boton_salir['superficie'].fill(COLOR_AZUL)

boton_opciones = {"superficie":pygame.Surface(TAMAÑO_BOTON),"rectangulo":pygame.Rect(0,0,0,0)}
boton_opciones['superficie'].fill(COLOR_AZUL)

boton_puntuaciones = {"superficie":pygame.Surface(TAMAÑO_BOTON),"rectangulo":pygame.Rect(0,0,0,0)}
boton_puntuaciones['superficie'].fill(COLOR_AZUL)

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
        
def mostrar_menu(pantalla:pygame.Surface,eventos):
    retorno = "menu"
    
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:

                if boton_jugar["rectangulo"].collidepoint(evento.pos):
                    click_sonido.play()
                    retorno = "juego"
                elif boton_opciones["rectangulo"].collidepoint(evento.pos):
                    click_sonido.play()
                    retorno = "opciones"
                elif boton_puntuaciones["rectangulo"].collidepoint(evento.pos):
                    click_sonido.play()
                    retorno = "puntuaciones"
                elif boton_agregar_preguntas["rectangulo"].collidepoint(evento.pos):
                    click_sonido.play()
                    retorno = "agregar_preguntas"
                elif boton_salir["rectangulo"].collidepoint(evento.pos):
                    click_sonido.play()
                    retorno = "salir"
        elif evento.type == pygame.QUIT:
                retorno = "salir"
    
    pantalla.fill(COLOR_BLANCO)
            
    boton_jugar["rectangulo"] = pantalla.blit(boton_jugar["superficie"],(5,235))
    boton_opciones["rectangulo"] = pantalla.blit(boton_opciones["superficie"],(265,235))
    boton_puntuaciones["rectangulo"] = pantalla.blit(boton_puntuaciones["superficie"],(5,310))
    boton_salir["rectangulo"] = pantalla.blit(boton_salir["superficie"],(265,310))
    boton_agregar_preguntas["rectangulo"] = pantalla.blit(boton_agregar_preguntas["superficie"],(5,385))
    pantalla.blit(imagen_preguntados, (40,40))


    blit_text(boton_jugar['superficie'],"JUGAR",(20,20),fuente_menu,COLOR_BLANCO)
    blit_text(boton_opciones['superficie'],"OPCIONES",(20,20),fuente_menu,COLOR_BLANCO)
    blit_text(boton_puntuaciones['superficie'],"PUNTUACIONES",(20,20),fuente_menu,COLOR_BLANCO)
    blit_text(boton_salir['superficie'],"SALIR",(20,20),fuente_menu,COLOR_BLANCO)
    blit_text(boton_agregar_preguntas['superficie'],"AGREGAR PREGUNTAS",(20,20),fuente_menu,COLOR_BLANCO)
    
    
    return retorno