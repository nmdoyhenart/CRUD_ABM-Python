"""""
Nombre: Nicolás
Apellido: Doyhenart

Parcial 11/06 Completo
"""""
from inputs import *
from peliculas import *

id = [1,2,3,4]
titulo = ["Inception","Coco","Superman","Cars"]
genero = ["Ciencia ficción","Animación","Superhéroes","Animación"]
año_lanzamiento = [2010,2017,1986,2000]
duracion = [148,109,175,117]
clasificacion = [False,True,True,True]
plataforma = ["Netflix","Disney+","HBO","Disney+"]

with open("Peliculas.csv", "w", encoding = "utf8") as archivo:
    for i in range (len(id)):
        registro = f"{id[i]},{titulo[i]},{genero[i]},{año_lanzamiento[i]},{duracion[i]},{clasificacion[i]},{plataforma[i]}\n"
        archivo.write(registro)

def leer_peliculas(lista_peliculas: list[dict]):
    """Lee las peliculas ya creadas anteriormente

    Args:
        lista_peliculas: list[dict]: Diccionario en el que se encuentran las películas
    """
    with open("Peliculas.csv","r", encoding = "utf8") as archivo:
        for linea in archivo:
            registro = linea.strip().split(",")
            nueva_lista = {
                "ID": int(registro[0]),
                "Titulo": registro[1],
                "Genero": registro[2],
                "Año lanzamiento": int(registro[3]),
                "Duracion": int(registro[4]),
                "Clasificacion": registro[5],
                "Plataforma": bool(registro[6])
            }

            lista_peliculas.append(nueva_lista)

def escribir_peliculas(lista_peliculas: list[dict]):
    """Escribe nuevas películas que ingresa el usuario

    Args:
        lista_peliculas: list[dict]: La lista a la cual se añaden los nuevos elementos
    """
    with open("Peliculas.csv", "w", encoding = "utf8") as archivo:   
        for pelicula in lista_peliculas:
            registro = f'{pelicula["ID"]},{pelicula["Titulo"]},{pelicula["Genero"]},{pelicula["Año lanzamiento"]},{pelicula["Duracion"]},{pelicula["Clasificacion"]},{pelicula["Plataforma"]}\n'
            archivo.write(registro)