"""""
Nombre: Nicolás
Apellido: Doyhenart

Parcial 07/03
"""""
from os import system
from peliculas import *
from inputs import *

def elegir_opcion():
    opcion = input("""Menu CINE\n1- Ingresar una nueva película\n2- Modificar película\n3- Eliminar película\n4- Mostrar películas\n5- Ordenar películas\n6- Buscar película por titulo\n7- Calcular duración y cantidad de películas\n8- Calcular porcentajes\n9- Salir del programa\nElije una opción: """)

    return opcion

lista_peliculas = [
    {"Titulo": "Inception","Genero": "Ciencia ficción","Año lanzamiento": 2010,"Duracion": 148,"Clasificacion": False},
    {"Titulo": "Coco","Genero": "Animación","Año lanzamiento": 2017,"Duracion": 109,"Clasificacion": True},
    {"Titulo": "Superman","Genero": "Superhéroes","Año lanzamiento": 1986,"Duracion": 175,"Clasificacion": True},
    {"Titulo": "Cars","Genero": "Animación","Año lanzamiento": 2000,"Duracion": 117,"Clasificacion": True}
    ]

system("cls")

while True:
    opcion = elegir_opcion()
    match opcion:
        case "1":
            ingresar_peliculas(lista_peliculas)
        case "2":
            modificar_peliculas(lista_peliculas)
        case "3":
            eliminar_pelicula(lista_peliculas)
        case "4":
            system("cls")
            muestreo_peliculas(lista_peliculas)
        case "5":
            ordenar_peliculas(lista_peliculas)
        case "6":
            buscar_por_titulo(lista_peliculas)
        case "7":
            calcular(lista_peliculas)
        case "8":
            porcentaje(lista_peliculas)
        case "9":
            print("Gracias por elegir el programa CINE")
            break

    system("pause")
    system("cls")