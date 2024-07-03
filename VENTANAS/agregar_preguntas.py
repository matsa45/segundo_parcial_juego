
import parsear_preguntas
import pygame
from pygame import *
from constantes import *

pygame.init()

fuente =  pygame.font.SysFont("Arial Narrow",40)
fuente_boton = pygame.font.SysFont("Arial Narrow",23)

abc_imagen = image.load('abc.png')
abc_imagen = transform.scale(abc_imagen,(110,70))

guardar_imagen = image.load('guardar.png')
guardar_imagen = transform.scale(guardar_imagen,(90,70))

cuadro_pregunta= {"superficie":pygame.Surface(CUADRO_AGREGAR_PREGUNTA),"rectangulo":pygame.Rect(0,0,0,0)}
cuadro_pregunta['superficie'].fill(COLOR_AZUL)

cuadro_respuesta_a = {"superficie":pygame.Surface(CUADRO_AGREGAR),"rectangulo":pygame.Rect(0,0,0,0)}
cuadro_respuesta_a['superficie'].fill(COLOR_AZUL)

cuadro_respuesta_b = {"superficie":pygame.Surface(CUADRO_AGREGAR),"rectangulo":pygame.Rect(0,0,0,0)}
cuadro_respuesta_b['superficie'].fill(COLOR_AZUL) 

cuadro_respuesta_c = {"superficie":pygame.Surface(CUADRO_AGREGAR),"rectangulo":pygame.Rect(0,0,0,0)}
cuadro_respuesta_c['superficie'].fill(COLOR_AZUL)

cuadro_respuesta_correcta = {"superficie":pygame.Surface(CUADRO_AGREGAR),"rectangulo":pygame.Rect(0,0,0,0)}
cuadro_respuesta_correcta['superficie'].fill(COLOR_AZUL)

boton_volver = {"superficie":pygame.Surface(TAMAÑO_BOTON_VOLVER),"rectangulo":pygame.Rect(0,0,0,0)}
boton_volver['superficie'].fill(COLOR_AZUL) 

cargar_respuestas = {"superficie":pygame.Surface(CUADRO_AGREGAR),"rectangulo":pygame.Rect(0,0,0,0)}
cargar_respuestas['superficie'].fill(COLOR_BLANCO) 

pregunta = ""
respuesta_a = ""
respuesta_b = ""
respuesta_c = ""
respuesta_correcta = ""
caja_activa = None


def guardar_lista_preguntas(pregunta, respuesta_a, respuesta_b, respuesta_c, respuesta_correcta):
    nueva_pregunta = {
        'pregunta': pregunta,
        'respuesta_a': respuesta_a,
        'respuesta_b': respuesta_b,
        'respuesta_c': respuesta_c,
        'respuesta_correcta': respuesta_correcta
    }
    return nueva_pregunta


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

def escribir_texto(eventos, texto, bandera_respuesta_correcta):
    for tecla in eventos:
        if tecla.type == pygame.KEYDOWN:
            if tecla.key == pygame.K_BACKSPACE and len(texto) > 0:
                texto = texto[:-1]
            elif tecla.unicode:
                letra_presionada = tecla.unicode

                if bandera_respuesta_correcta == False:
                    if letra_presionada.isalpha() or letra_presionada.isdigit() or letra_presionada in [' ', ',', '.', ';', ':', '-', '¿', '?']: 
                        texto += letra_presionada
                elif bandera_respuesta_correcta == True:
                    if letra_presionada.lower() in ['a', 'b', 'c'] and len(texto) == 0:
                        texto += letra_presionada.lower()
    
    return texto
def agregar_preguntas(pantalla:pygame.Surface,eventos,): 
    retorno = "agregar_preguntas"
    global pregunta
    global respuesta_a
    global respuesta_b
    global respuesta_c
    global respuesta_correcta
    global caja_activa
    bandera_cargar = False
    
    for evento in eventos:

        if evento.type == pygame.QUIT:
            retorno = "salir"
                
        
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_volver['rectangulo'].collidepoint(evento.pos):
                    retorno = "menu"
            if cuadro_pregunta['rectangulo'].collidepoint(evento.pos):
                caja_activa = "pregunta"
                
            elif cuadro_respuesta_a['rectangulo'].collidepoint(evento.pos):
                caja_activa = "respuesta_a"
                
            elif cuadro_respuesta_b['rectangulo'].collidepoint(evento.pos):
                caja_activa = "respuesta_b"
            
            elif boton_volver['rectangulo'].collidepoint(evento.pos):
                caja_activa = "volver"

            elif cuadro_respuesta_c['rectangulo'].collidepoint(evento.pos):
                caja_activa = "respuesta_c"
                
            elif cuadro_respuesta_correcta['rectangulo'].collidepoint(evento.pos):
                caja_activa = "respuesta_correcta"
            
            elif cargar_respuestas['rectangulo'].collidepoint(evento.pos):
                caja_activa = 'cargar_lista'
            
            
                    
                

    if caja_activa == "pregunta":
        bandera_respuesta_correcta = False
        pregunta = escribir_texto(eventos, pregunta, bandera_respuesta_correcta)
   
    elif caja_activa == "respuesta_a":
        bandera_respuesta_correcta = False
        respuesta_a = escribir_texto(eventos, respuesta_a, bandera_respuesta_correcta)
    
    elif caja_activa == "respuesta_b":
        bandera_respuesta_correcta = False
        respuesta_b = escribir_texto(eventos, respuesta_b, bandera_respuesta_correcta)
   
    elif caja_activa == "respuesta_c":
        bandera_respuesta_correcta = False
        respuesta_c = escribir_texto(eventos, respuesta_c, bandera_respuesta_correcta)
    
    elif caja_activa == 'respuesta_correcta':
          bandera_respuesta_correcta = True
          respuesta_correcta = escribir_texto(eventos,respuesta_correcta, bandera_respuesta_correcta)

    elif caja_activa == "cargar_lista":
        if pregunta != '' and respuesta_a != '' and respuesta_b != '' and respuesta_c != '' and respuesta_correcta != '':
            nueva_lista = guardar_lista_preguntas(pregunta,respuesta_a, respuesta_b, respuesta_c, respuesta_correcta)
            bandera_cargar = True
        else: bandera_cargar = False
            
    if bandera_cargar:
        from parsear_preguntas import actualizar_preguntas
        actualizar_preguntas(nueva_lista)
        retorno = 'salir'
        return retorno
    
    pantalla.fill(COLOR_BLANCO)
    
    cuadro_pregunta['rectangulo'] = pantalla.blit(cuadro_pregunta['superficie'], (220, 10))
    blit_text(pantalla, f" INGRESAR\nPREGUNTA", (50, 10), fuente, COLOR_NEGRO)
    cuadro_pregunta['superficie'].fill(COLOR_AZUL)
    blit_text(cuadro_pregunta['superficie'], pregunta, (10, 10), fuente, COLOR_BLANCO)

    cuadro_respuesta_a['rectangulo'] = pantalla.blit(cuadro_respuesta_a['superficie'], (220, 160))
    blit_text(pantalla, f"      INGRESAR\nRESPUESTA A", (13, 160), fuente, COLOR_NEGRO)
    cuadro_respuesta_a['superficie'].fill(COLOR_AZUL)
    blit_text(cuadro_respuesta_a['superficie'], respuesta_a, (10, 10), fuente, COLOR_BLANCO)

    cuadro_respuesta_b['rectangulo'] = pantalla.blit(cuadro_respuesta_b['superficie'], (220, 220))
    blit_text(pantalla, f"      INGRESAR\nRESPUESTA B", (13, 220), fuente, COLOR_NEGRO)
    cuadro_respuesta_b['superficie'].fill(COLOR_AZUL)
    blit_text(cuadro_respuesta_b['superficie'], respuesta_b, (10, 10), fuente, COLOR_BLANCO)
    
    cuadro_respuesta_c['rectangulo'] = pantalla.blit(cuadro_respuesta_c['superficie'], (220, 280))
    blit_text(pantalla, f"      INGRESAR\nRESPUESTA C", (13, 280), fuente, COLOR_NEGRO)
    cuadro_respuesta_c['superficie'].fill(COLOR_AZUL)
    blit_text(cuadro_respuesta_c['superficie'], respuesta_c, (10, 10), fuente, COLOR_BLANCO)

    cuadro_respuesta_correcta['rectangulo'] = pantalla.blit(cuadro_respuesta_correcta['superficie'], (220, 340))
    blit_text(pantalla, f"     RESPUESTA\n       CORRECTA", (1, 340), fuente, COLOR_NEGRO)
    cuadro_respuesta_correcta['superficie'].fill(COLOR_AZUL)
    blit_text(cuadro_respuesta_correcta['superficie'], respuesta_correcta, (10, 10), fuente, COLOR_BLANCO)

    cargar_respuestas['rectangulo'] = pantalla.blit(cargar_respuestas['superficie'], (400,420))
    cargar_respuestas['superficie'].fill(COLOR_BLANCO)

    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'], (0,460))
    boton_volver['superficie'].fill(COLOR_AZUL)
    blit_text(boton_volver['superficie'],"VOLVER",(10,10),fuente_boton,COLOR_BLANCO)
    
    pantalla.blit(abc_imagen, (290,400))

    pantalla.blit(guardar_imagen, (400,420))


    return retorno

