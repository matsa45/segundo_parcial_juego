import pygame 
from constantes import *
from pygame import *
pygame.init()

imagen_menos_volumen = image.load('volumen.png')
imagen_menos_volumen = transform.scale(imagen_menos_volumen,(60,60))

imagen_mas_volumen = image.load('mas_volumen.png')
imagen_mas_volumen = transform.scale(imagen_mas_volumen,(60,60))


fuente_boton = pygame.font.SysFont("Arial Narrow",23)
fuente_volumen =  pygame.font.SysFont("Arial Narrow",50)
fuente = pygame.font.SysFont("Arial Narrow",50)

boton_timer_1 = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}
boton_timer_1['superficie'].fill(COLOR_BLANCO) 

boton_timer_5 = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}
boton_timer_5['superficie'].fill(COLOR_BLANCO)

boton_timer_menos_1 = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}
boton_timer_menos_1['superficie'].fill(COLOR_BLANCO) 

boton_timer_menos_5 = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}
boton_timer_menos_5['superficie'].fill(COLOR_BLANCO) 


boton_suma = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}
boton_suma['superficie'].fill(COLOR_BLANCO)

boton_resta = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}
boton_resta['superficie'].fill(COLOR_BLANCO)

boton_volver = {"superficie":pygame.Surface(TAMAÑO_BOTON_VOLVER),"rectangulo":pygame.Rect(0,0,0,0)}
boton_volver['superficie'].fill(COLOR_AZUL) 

volumen = 100
timer = 120

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


def mostrar_opciones(pantalla:pygame.Surface,eventos,):
    global volumen
    global timer
    retorno = "opciones"
    
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_suma['rectangulo'].collidepoint(evento.pos):
                    if volumen < 96: 
                        volumen += 5
                        click_sonido.play()
                        click_sonido.set_volume(volumen / 100)

                elif boton_resta['rectangulo'].collidepoint(evento.pos):
                    if volumen > 0: 
                        volumen -= 5
                        click_sonido.play()
                        click_sonido.set_volume(volumen / 100)
                
                elif boton_timer_1['rectangulo'].collidepoint(evento.pos):
                    timer += 1
                elif boton_timer_5['rectangulo'].collidepoint(evento.pos):
                    timer += 5
                elif boton_timer_menos_1['rectangulo'].collidepoint(evento.pos):
                    if timer > 1:
                        timer -= 1
                elif boton_timer_menos_5['rectangulo'].collidepoint(evento.pos):
                    if timer > 5:
                        timer -= 5
                
                elif boton_volver['rectangulo'].collidepoint(evento.pos):
                    retorno = "menu"
                    click_sonido.play()
                    click_sonido.set_volume(volumen / 100)
                
        elif evento.type == pygame.QUIT:
            retorno = "salir"
            
    pantalla.fill(COLOR_BLANCO)
    
    boton_resta['rectangulo'] = pantalla.blit(boton_resta['superficie'],(20,200))
    boton_suma['rectangulo'] = pantalla.blit(boton_suma['superficie'],(420,200))
    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'],(5,5))
    boton_timer_5['rectangulo'] = pantalla.blit(boton_timer_5['superficie'],(420,350))
    boton_timer_1['rectangulo'] = pantalla.blit(boton_timer_1['superficie'],(350,350))
    boton_timer_menos_5['rectangulo'] = pantalla.blit(boton_timer_menos_5['superficie'],(20,350))
    boton_timer_menos_1['rectangulo'] = pantalla.blit(boton_timer_menos_1['superficie'],(90,350))

    blit_text(pantalla,f"{volumen}%",(210,220),fuente_volumen,COLOR_NEGRO)
    blit_text(pantalla,f"{timer}s",(210,360),fuente_volumen,COLOR_NEGRO)
    blit_text(boton_volver['superficie'],"VOLVER",(10,10),fuente_boton,COLOR_BLANCO)
    blit_text(pantalla,'VOLUMEN',(30,100),fuente,COLOR_NEGRO)
    blit_text(pantalla,'+5s',(420,360),fuente,COLOR_NEGRO)
    blit_text(pantalla,'+1s',(350,360),fuente,COLOR_NEGRO)
    blit_text(pantalla,'-5s',(20,360),fuente,COLOR_NEGRO)
    blit_text(pantalla,'-1s',(90,360),fuente,COLOR_NEGRO)


    pantalla.blit(imagen_menos_volumen,(20,200))
    pantalla.blit(imagen_mas_volumen,(420,200))  
    
    return retorno
