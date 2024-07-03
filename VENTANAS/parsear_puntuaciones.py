import csv
from datetime import datetime
from juego import *
from terminado import *



def partidas_json(nombre_final:str, fecha, puntuacion:int):
    
    nueva_puntuacion = {'nombre': nombre_final, 'fecha': fecha.strftime('%d/%m/%Y'), 'puntuacion': puntuacion}

    try:
        with open('partidas.json', mode='r', encoding='utf-8') as file:
            puntuaciones = json.load(file)
    
    except json.JSONDecodeError:
        puntuaciones = []

    
    if not isinstance(puntuaciones, list):
        puntuaciones = []


    puntuaciones.append(nueva_puntuacion)
    
    with open('partidas.json', mode='w', encoding='utf-8') as file:
        json.dump(puntuaciones, file, ensure_ascii=False, indent=4)

    return puntuaciones

def mejores_diez():
    try:
        with open('partidas.json', mode='r', encoding='utf-8') as file:
            puntuaciones = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        puntuaciones = []

    if not isinstance(puntuaciones, list):
        puntuaciones = []

    n = len(puntuaciones)
    for i in range(n):
        for j in range(0, n-i-1):
            if int(puntuaciones[j]['puntuacion']) < int(puntuaciones[j+1]['puntuacion']):
                puntuaciones[j], puntuaciones[j+1] = puntuaciones[j+1], puntuaciones[j]

    mejores_diez = puntuaciones[:10]

    return mejores_diez