"""""
Nombre: Nicolás
Apellido: Doyhenart

Parcial 07/03
"""""
from peliculas import *

def titulo_duplicado(lista_peliculas: list[dict], titulo: str):
    for pelicula in lista_peliculas:
        if pelicula["Titulo"].lower() == titulo.lower():
            return False
    return True

def ingresar_peliculas(lista_peliculas: list[dict]) -> None:
    id = len(lista_peliculas) + 1
    while len(lista_peliculas) < 20:
        titulo = input("Ingrese el titulo de la pelicula: ").capitalize()
        while len(titulo) > 30 or not titulo.isalpha():
                print("ERROR")
                titulo = input("Ingrese una titulo válido: ").capitalize()
  
        genero = input("Ingrese el genero de la pelicula: ").capitalize()
        while genero not in ["Acción","Aventura","Animación","Biográfico","Comedia","Comedia romántica","Comedia dramática","Crimen","Documental","Drama","Fantasía","Histórico","Infantil","Musical","Misterio","Policíaco","Romance","Ciencia ficción","Suspenso","Terror","Western","Bélico","Deportivo","Noir","Experimental","Familiar","Superhéroes","Espionaje","Artes marciales","Fantástico","Catástrofe","Melodrama","Erótico","Cine independiente","Zombies","Vampiros","Cyberpunk","Steampunk","Distopía", "Utopía","Road movie","Docuficción","Mockumentary","Gótico","Slasher","Adolescente","Culto","Maravilloso"]:
            print("ERROR")
            genero = input("Ingrese un genero válido: ").capitalize()
        
        año_lanzamiento = int(input("Ingrese el año de lanzamiento: "))
        while año_lanzamiento.isdigit() or not 1888 <= int(año_lanzamiento) <= 2024:
            print("ERROR")
            año_lanzamiento = int(input("Ingrese una fecha válida: "))
        
        duracion = int(input("Ingrese la duración de la pelicula: "))
        while duracion <= 0:
            print("ERROR")
            duracion = int(input("Ingrese una duración válida: "))

        clasificacion = input("¿La pelicula ingresada es ATP? (si/no): ").lower()
        if clasificacion.lower() != 'si':
            clasificacion == False
        else:
            clasificacion == True

        pelicula = crear_pelicula(id, titulo, genero, año_lanzamiento, duracion, clasificacion)
        lista_peliculas.append(pelicula)
        id += 1
        
        continuar = input("¿Desea ingresar otra pelicula? (si/no): ")
        if continuar.lower() != 'si':
            break

def modificar_peliculas(lista_peliculas: list[dict]):
    titulo_pelicula = input("Ingrese el título de la película a modificar: ").capitalize()

    pelicula_existente = None
    for pelicula in lista_peliculas:
        if pelicula["Titulo"] == titulo_pelicula:
            pelicula_existente = pelicula
            break

    if not pelicula_existente:
        print("Película inexistente")
        return False

    modificaciones = []
    while True:
        print("¡Película existente!")
        opcion_modificar = input("""¿Qué desea modificar?\n1-Título de la película\n2-Género de la película\n3-Año de lanzamiento\n4-Duración\n5-Clasificación\n6-Ninguno de los anteriores\nElija una opción: """)

        match opcion_modificar:
            case "1":
                nuevo_titulo = input("Ingrese el nuevo título: ").capitalize()
                while len(nuevo_titulo) > 30 or not nuevo_titulo.isalpha():
                        print("ERROR")
                        nuevo_titulo = input("Ingrese un nombre válido: ").capitalize()
                pelicula_existente["Titulo"] = nuevo_titulo
                modificaciones.append("-Título modificado exitosamente")

                
            case "2":
                nuevo_genero = input("Ingrese el nuevo género: ").capitalize()
                while nuevo_genero not in ["Acción", "Aventura", "Animación", "Biográfico", "Comedia", "Comedia romántica", "Comedia dramática", "Crimen", "Documental", "Drama", "Fantasía", "Histórico", "Infantil", "Musical", "Misterio", "Policíaco", "Romance", "Ciencia ficción", "Suspenso", "Terror", "Western", "Bélico", "Deportivo", "Noir", "Experimental", "Familiar", "Superhéroes", "Espionaje", "Artes marciales", "Fantástico", "Catástrofe", "Melodrama", "Erótico", "Cine independiente", "Zombies", "Vampiros", "Cyberpunk", "Steampunk", "Distopía", "Utopía", "Road movie", "Docuficción", "Mockumentary", "Gótico", "Slasher", "Adolescente", "Culto", "Maravilloso"]:
                    print("ERROR")
                    nuevo_genero = input("Ingrese un género válido: ").capitalize()
                pelicula_existente["Genero"] = nuevo_genero
                modificaciones.append("-Género modificado exitosamente")

            case "3":
                nuevo_año_lanzamiento = input("Ingrese el nuevo año de lanzamiento: ")
                while nuevo_año_lanzamiento.isdigit() or not 1888 <= int(nuevo_año_lanzamiento) <= 2024:
                    print("ERROR")
                    nuevo_año_lanzamiento = input("Ingrese un año válido: ")
                pelicula_existente["Año lanzamiento"] = int(nuevo_año_lanzamiento)
                modificaciones.append("-Año de lanzamiento modificado exitosamente")

            case "4":
                nueva_duracion = int(input("Ingrese la duración de la pelicula: "))
                while nueva_duracion <= 0:
                    print("ERROR")
                    nueva_duracion = input("Ingrese una duración válida: ")
                pelicula_existente["Duracion"] = int(nueva_duracion)
                modificaciones.append("-Duración modificada exitosamente")

            case "5":
                nueva_clasificacion = input("¿La película ingresada es ATP? (si/no): ").lower()
                while nueva_clasificacion != ["si", "no"]:
                    print("ERROR")
                    nueva_clasificacion = input("Ingrese una respuesta válida (si/no): ").lower()
                pelicula_existente["Clasificacion"] = (nueva_clasificacion == "si")
                modificaciones.append("-Clasificación modificada exitosamente")

            case "6":
                break

        continuar = input("¿Desea modificar otro dato? (si/no): ").lower()
        if continuar != "si":
            break

    if modificaciones:
        print("Se realizaron las siguientes modificaciones:\n")
        for modificacion in modificaciones:
            print(modificacion)
    
    if not modificaciones:
        print("No se realizaron modificaciones.")

        return True