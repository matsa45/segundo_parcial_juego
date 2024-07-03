import os

def parse_csv(nombre_archivo):
    lista_elementos = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding='utf-8') as archivo:
            primer_linea = archivo.readline()
            primer_linea = primer_linea.replace("\n", "")
            lista_claves = primer_linea.split(",")
            for linea in archivo:
                linea_aux = linea.replace("\n", "")
                lista_valores = linea_aux.split(",")
                diccionario_aux = {}
                for i in range(len(lista_claves)):
                    diccionario_aux[lista_claves[i]] = lista_valores[i]

                lista_elementos.append(diccionario_aux)

        return lista_elementos
    else:
        print("ARCHIVO NO ENCONTRADO")
        return None


lista_preguntas = parse_csv("preguntas.csv")


def actualizar_preguntas(nueva_pregunta):
    nombre_archivo = "preguntas.csv"
    lista_preguntas = parse_csv(nombre_archivo)

    if isinstance(nueva_pregunta, dict):
        lista_preguntas.append(nueva_pregunta)

        with open(nombre_archivo, "w", encoding='utf-8') as archivo:
            archivo.write("pregunta,respuesta_a,respuesta_b,respuesta_c,respuesta_correcta\n")
            for pregunta in lista_preguntas:
                linea = ",".join(pregunta.values()) + "\n"
                archivo.write(linea)
    else:
        print("ERROR: La nueva pregunta debe ser un diccionario.")

