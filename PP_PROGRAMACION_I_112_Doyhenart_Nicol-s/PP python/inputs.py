"""""
Nombre: Nicolás
Apellido: Doyhenart

Parcial 07/03
"""""

generos = ["Acción","Aventura","Animación","Biográfico","Comedia","Comedia romántica","Comedia dramática","Crimen","Documental","Drama","Fantasía","Histórico","Infantil","Musical","Misterio","Policíaco","Romance","Ciencia ficción","Suspenso","Terror","Western","Bélico","Deportivo","Noir","Experimental","Familiar","Superhéroes","Espionaje","Artes marciales","Fantástico","Catástrofe","Melodrama","Erótico","Cine independiente","Zombies","Vampiros","Cyberpunk","Steampunk","Distopía", "Utopía","Road movie","Docuficción","Mockumentary","Gótico","Slasher","Adolescente","Culto","Maravilloso"]

def titulo_duplicado(lista_peliculas: list[dict], titulo: str) -> bool:
    for pelicula in lista_peliculas:
        if pelicula["Titulo"] == titulo:
            return True  # Se encontró un título duplicado
    return False  # No se encontró un título duplicado

def ingresar_peliculas(lista_peliculas: list[dict]) -> None:
    while True:
        id = len(lista_peliculas) + 1
        titulo = input("Ingrese el título de la película: ").capitalize()
        
        # Verificar si el título ya está duplicado o si es demasiado largo
        while len(titulo) > 30 or titulo_duplicado(lista_peliculas, titulo):
            if len(titulo) > 30:
                print("El título es demasiado largo. Ingrese un título con menos de 30 caracteres.")
            elif titulo_duplicado(lista_peliculas, titulo):
                print("El título ya existe. Ingrese un título diferente.")
            titulo = input("Ingrese un título válido: ").capitalize()

        genero = input("Ingrese el género de la película: ").capitalize()
        while genero not in generos:
            print("ERROR")
            genero = input("Ingrese un género válido: ").capitalize()
        
        año_lanzamiento = int(input("Ingrese el año de lanzamiento: "))
        while año_lanzamiento < 1888 or año_lanzamiento > 2024:
            print("ERROR")
            año_lanzamiento = int(input("Ingrese una fecha válida: "))
        
        duracion = int(input("Ingrese la duración de la película en minutos: "))
        while duracion <= 0:
            print("ERROR")
            duracion = int(input("Ingrese una duración válida: "))

        clasificacion = input("¿La película ingresada es ATP? (si/no): ").lower()
        if clasificacion != 'si' and clasificacion != 'no':
            print("ERROR")
            clasificacion = input("Ingrese una respuesta válida (si/no): ").lower()
        clasificacion = clasificacion == 'si'

        nueva_pelicula = {
            "ID": id,
            "Titulo": titulo,
            "Genero": genero,
            "Año lanzamiento": año_lanzamiento,
            "Duracion": duracion,
            "Clasificacion": clasificacion
        }
        lista_peliculas.append(nueva_pelicula)

        continuar = input("¿Desea ingresar otra película? (si/no): ").lower()
        if continuar != 'si':
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
                nuevo_titulo = input("Ingrese el nuevo título de la película: ").capitalize()
        
                while len(nuevo_titulo) > 30 or (nuevo_titulo != titulo_pelicula and titulo_duplicado(lista_peliculas, nuevo_titulo)):
                    if len(nuevo_titulo) > 30:
                        print("El título es demasiado largo.")
                    elif nuevo_titulo != titulo_pelicula and titulo_duplicado(lista_peliculas, nuevo_titulo):
                        print("El título ya existe. Ingrese un título diferente.")
                    nuevo_titulo = input("Ingrese un título válido: ").capitalize()
                pelicula_existente["Titulo"] = nuevo_titulo
                modificaciones.append("-Título modificado exitosamente")
                
            case "2":
                nuevo_genero = input("Ingrese el nuevo género: ").capitalize()
                while nuevo_genero != generos:
                    print("ERROR")
                    nuevo_genero = input("Ingrese un género válido: ").capitalize()
                pelicula_existente["Genero"] = nuevo_genero
                modificaciones.append("-Género modificado exitosamente")

            case "3":
                nuevo_año_lanzamiento = input("Ingrese el nuevo año de lanzamiento: ")
                while not nuevo_año_lanzamiento.isdigit() or not 1888 <= int(nuevo_año_lanzamiento) <= 2024:
                    print("ERROR")
                    nuevo_año_lanzamiento = input("Ingrese un año válido: ")
                pelicula_existente["Año lanzamiento"] = int(nuevo_año_lanzamiento)
                modificaciones.append("-Año de lanzamiento modificado exitosamente")

            case "4":
                nueva_duracion = int(input("Ingrese la duración de la película en minutos: "))
                while nueva_duracion <= 0:
                    print("ERROR")
                    nueva_duracion = int(input("Ingrese una duración válida: "))
                pelicula_existente["Duracion"] = nueva_duracion
                modificaciones.append("-Duración modificada exitosamente")

            case "5":
                nueva_clasificacion = input("¿La película ingresada es ATP? (si/no): ").lower()
                while nueva_clasificacion not in ["si", "no"]:
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