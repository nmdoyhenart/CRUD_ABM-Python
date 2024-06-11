"""""
Nombre: Nicolás
Apellido: Doyhenart

Parcial 07/03
"""""
from os import system
from peliculas import *
from inputs import *
from archivos import *

def elegir_opcion():
    """Menu del programa

    Args: -
    """
    opcion = input("""Menu CINE\n1- Ingresar una nueva película\n2- Modificar película\n3- Eliminar película\n4- Mostrar películas\n5- Ordenar películas\n6- Buscar película por titulo\n7- Calcular duración y cantidad de películas\n8- Calcular porcentajes\n9- Salir del programa\nElije una opción: """)
    
    return opcion

lista_peliculas = []
bandera_ingreso = False

system("cls")

leer_peliculas(lista_peliculas)

while True:
    opcion = elegir_opcion()
    match opcion:
        case "1":
            bandera_ingreso = True
            ingresar_peliculas(lista_peliculas)        
        case "2":
            if bandera_ingreso == False:
                print("Ingrese, al menos, una película para utilizar el menu.")
            else:
                modificar_peliculas(lista_peliculas)
        case "3":
            if bandera_ingreso == False:
                print("Ingrese, al menos, una película para utilizar el menu.")  
            else:          
                eliminar_pelicula(lista_peliculas)
        case "4":
            system("cls")
            if bandera_ingreso == False:
                print("Ingrese, al menos, una película para utilizar el menu.")
            else:            
                muestreo_peliculas(lista_peliculas)
        case "5":
            if bandera_ingreso == False:
                print("Ingrese, al menos, una película para utilizar el menu.")
            else:           
                ordenar_peliculas(lista_peliculas)
        case "6":
            if bandera_ingreso == False:
                print("Ingrese, al menos, una película para utilizar el menu.")
            else:          
                buscar_por_titulo(lista_peliculas)
        case "7":
            if bandera_ingreso == False:
                print("Ingrese, al menos, una película para utilizar el menu.")
            else:           
                calcular(lista_peliculas)
        case "8":
            if bandera_ingreso == False:
                print("Ingrese, al menos, una película para utilizar el menu.") 
            else:           
                porcentaje(lista_peliculas)
        case "9":
            escribir_peliculas(lista_peliculas)
            print("Gracias por utilizar el programa CINE")
            break
        case  _:
            print("Valor inexistente, ingrese una opción valida")

    system("pause")
    system("cls")