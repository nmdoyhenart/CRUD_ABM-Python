"""""
Nombre: Nicolás
Apellido: Doyhenart

Parcial 07/03
"""""
from peliculas import *

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
        
        año_lanzamiento = int(input("Ingrese el año de lanzamiento: ")) # isdigit
        while año_lanzamiento <= 1888 or año_lanzamiento >=  2024:
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

        if len(lista_peliculas) >= 20:
            print("Se ha alcanzado el límite de empleados.")
            break
        
        continuar = input("¿Desea ingresar otra pelicula? (si/no): ")
        if continuar.lower() != 'si':
            break

def modificar_peliculas(lista_peliculas: list[dict]):
    titulo_pelicula = input("Ingrese el titulo de la pelicula a moficar: ")
    bandera_ingreso = False
    modificaciones = False

    while True:
        for pelicula in lista_peliculas:
            if pelicula["Titulo"] == titulo_pelicula:
                print("¡Pelicula existente!")
                bandera_ingreso = True
                opcion_modificar = input("""¿Que desea mofidicar?\n1-Titulo de la pelicula\n2-Genero de la pelicula\n3-Año de lanzamiento\n4-Duración\n5-Clasifiación\n6-Ninguno de los anteriores\nElija una opción: """)
                break
        
        match opcion_modificar:
            case "1":
                nuevo_titulo = input("Ingrese el nuevo titulo: ").capitalize()
                while len(nuevo_titulo) > 30 or not nuevo_titulo.isalpha():
                    print("ERROR")
                    nuevo_titulo = input("Ingrese un nombre válido: ").capitalize()
                pelicula["Titulo"] = nuevo_titulo
                modificaciones = True

            case "2":
                nuevo_genero = input("Ingrese el nuevo genero: ").capitalize()
                while nuevo_genero not in ["Acción","Aventura","Animación","Biográfico","Comedia","Comedia romántica","Comedia dramática","Crimen","Documental","Drama","Fantasía","Histórico","Infantil","Musical","Misterio","Policíaco","Romance","Ciencia ficción","Suspenso","Terror","Western","Bélico","Deportivo","Noir","Experimental","Familiar","Superhéroes","Espionaje","Artes marciales","Fantástico","Catástrofe","Melodrama","Erótico","Cine independiente","Zombies","Vampiros","Cyberpunk","Steampunk","Distopía", "Utopía","Road movie","Docuficción","Mockumentary","Gótico","Slasher","Adolescente","Culto","Maravilloso"]:
                    print("ERROR")
                nuevo_genero = input("Ingrese un genero válido: ").capitalize()
                pelicula["Genero"] = nuevo_genero
                modificaciones = True
                
            case "3":
                nuevo_año_lanzamiento = int(input("Ingrese el nuevo año de lanzamiento: ")) # isdigit
                while nuevo_año_lanzamiento <=  1888 or nuevo_año_lanzamiento >=  2024:
                    print("ERROR")
                    nuevo_año_lanzamiento = int(input("Ingrese un DNI válido: "))
                pelicula["Año lanzamiento"] = nuevo_año_lanzamiento
                modificaciones = True

            case "4":
                nueva_duracion = int(input("Ingrese la nueva duración: "))
                while nueva_duracion <= 0:
                    nueva_duracion = int(input("Ingrese un duración válida: "))
                pelicula["Duracion"] = nueva_duracion
                modificaciones = True
            
            case "5":
                nueva_clasificacion = bool(input("¿La pelicula ingresada es ATP? (si/no): ")).lower()
                if nueva_clasificacion.lower != 'si':
                    nueva_clasificacion == False
                else:
                    nueva_clasificacion == True
                pelicula["Clasificacion"] = nueva_clasificacion
                modificaciones = True

            case "6":
                if modificaciones:
                    print("Se realizaron modificaciones.")
                else:
                    print("No se realizaron modificaciones.")
                
                return modificaciones
        
        continuar = input("¿Desea modificar otro dato? (si/no): ")
        if continuar.lower() != 'si':
            break

    if not bandera_ingreso:
        print("Pelicula inexistente")