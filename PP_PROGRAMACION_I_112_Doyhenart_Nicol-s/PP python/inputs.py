"""""
Nombre: Nicolás
Apellido: Doyhenart

Parcial 07/03
"""""
generos = ["Acción","Aventura","Animación","Biográfico","Comedia","Comedia romántica","Comedia dramática","Crimen","Documental","Drama","Fantasía","Histórico","Infantil","Musical","Misterio","Policíaco","Romance","Ciencia ficción","Suspenso","Terror","Western","Bélico","Deportivo","Noir","Experimental","Familiar","Superhéroes","Espionaje","Artes marciales","Fantástico","Catástrofe","Melodrama","Erótico","Cine independiente","Zombies","Vampiros","Cyberpunk","Steampunk","Distopía", "Utopía","Road movie","Docuficción","Mockumentary","Gótico","Slasher","Adolescente","Culto","Maravilloso"]

plataformas = ["Netflix","Star+","Hbo","Disney+","Crunchyroll","Paramount+","Hulu","Amazon"]

def titulo_duplicado(lista_peliculas: list[dict], titulo: str) -> bool:
    """Identifica si hay un título duplicado.

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
        titulo: str:

    Returns: -> bool; para hacer la comprobación.
    """
    for pelicula in lista_peliculas:
        if pelicula["Titulo"] == titulo:
            return True  
    return False 

def ingresar_peliculas(lista_peliculas: list[dict]) -> None:
    """Valida el ingreso de nuevas películas y las agrega a la lista.
    
    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.

    Returns: -> None; si no se ingresa nada.
    """  
    while True:
        id = len(lista_peliculas) + 1
        titulo = input("Ingrese el título de la película: ").capitalize().strip()
        
        while not titulo or len(titulo) > 30 or titulo_duplicado(lista_peliculas, titulo):
            if not titulo or titulo.isspace():
                print("No puede ingresar un titulo en blanco.")
            elif len(titulo) > 30:
                print("El título es demasiado largo. Ingrese un título con menos de 30 caracteres.")
            elif titulo_duplicado(lista_peliculas, titulo):
                print("El título ya existe. Ingrese un título diferente.")
            titulo = input("Ingrese un título válido: ").capitalize().strip()
       
        genero = input("Ingrese el género de la película: ").capitalize().strip()
        while genero not in generos or genero.isspace():
            print("ERROR")
            genero = input("Ingrese un género válido: ").capitalize().strip()
        
        año_lanzamiento = int(input("Ingrese el año de lanzamiento: "))
        while not año_lanzamiento or not 1888 <= año_lanzamiento <= 2024:
            print("ERROR")
            año_lanzamiento = int(input("Ingrese una fecha válida: "))
        
        duracion = int(input("Ingrese la duración de la película en minutos: "))
        while duracion <= 0:
            print("ERROR")
            duracion = int(input("Ingrese una duración válida: "))

        clasificacion = input("¿La película ingresada es ATP? (si/no): ").lower().strip()
        while clasificacion != 'si' and clasificacion != 'no' or clasificacion.isspace():
            print("ERROR")
            clasificacion = input("Ingrese una respuesta válida (si/no): ").lower().strip()
        clasificacion = clasificacion == 'si'

        plataforma = input("Ingrese la plataforma en la que se encuentra la película: ").capitalize().strip()

        while not plataforma or len(plataforma) > 20 or plataforma not in plataformas:
            if not plataforma:
                print("No puede ingresar un espacio en blanco.")
            elif plataforma not in plataformas:
                print("Ingrese una plataforma existente.")
            
            plataforma = input("Ingrese la plataforma en la que se encuentra la película: ").capitalize().strip()
            # plataforma = input("Ingrese una plataforma válida: ").capitalize().strip()
                
            # continuar = input("¿Desea ingresar otra plataforma? (si/no): ").lower().strip()
            # if not continuar:
            #     print("ERROR")
            # elif continuar != 'si':
            #     break

        nueva_pelicula = {
            "ID": id,
            "Titulo": titulo,
            "Genero": genero,
            "Año lanzamiento": año_lanzamiento,
            "Duracion": duracion,
            "Clasificacion": clasificacion,
            "Plataforma": plataforma            
        }
        lista_peliculas.append(nueva_pelicula)

        continuar = input("¿Desea ingresar otra película? (si/no): ").lower().strip()
        if not continuar or continuar.isspace():
            print("ERROR")
        elif continuar != 'si':
            break

def modificar_peliculas(lista_peliculas: list[dict]):
    """Permite modificar la información de una película existente en la lista.

    Args:
        lista_peliculas (list[dict]): Diccionario con información de las películas.
    """
    titulo_pelicula = input("Ingrese el título de la película a modificar: ").capitalize().strip()

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
        opcion_modificar = input("""¿Qué desea modificar?\n1- Título de la película\n2- Género de la película\n3- Año de lanzamiento\n4- Duración\n5- Clasificación\n6- Plataforma\n7- Ninguno de los anteriores\nElija una opción: """)

        match opcion_modificar:
            case "1":
                while True:
                    nuevo_titulo = input("Ingrese el nuevo título de la película: ").capitalize().strip()
                    if not nuevo_titulo or nuevo_titulo.isspace():
                        print("No puede ingresar un título en blanco.")
                    elif len(nuevo_titulo) > 30:
                        print("El título es demasiado largo. Ingrese un título con menos de 30 caracteres.")
                    elif titulo_duplicado(lista_peliculas, nuevo_titulo):
                        print("El título ya existe. Ingrese un título diferente.")
                    else:
                        pelicula_existente["Titulo"] = nuevo_titulo
                        modificaciones.append("-Títuloe")
                        break
                
            case "2":
                nuevo_genero = input("Ingrese el nuevo género: ").capitalize().strip()
                while nuevo_genero not in generos or nuevo_genero.isspace():
                    print("ERROR")
                    nuevo_genero = input("Ingrese un género válido: ").capitalize().strip()
                pelicula_existente["Genero"] = nuevo_genero
                modificaciones.append("-Género")

            case "3":
                nuevo_año_lanzamiento = int(input("Ingrese el nuevo año de lanzamiento: "))
                while not nuevo_año_lanzamiento.isdigit() or not 1888 <= nuevo_año_lanzamiento <= 2024:
                    print("ERROR")
                    nuevo_año_lanzamiento = input("Ingrese un año válido: ")
                pelicula_existente["Año lanzamiento"] = int(nuevo_año_lanzamiento)
                modificaciones.append("-Año de lanzamiento")

            case "4":
                nueva_duracion = int(input("Ingrese la nueva duración de la película en minutos: "))
                while nueva_duracion <= 0:
                    print("ERROR")
                    nueva_duracion = int(input("Ingrese una duración válida: "))
                pelicula_existente["Duracion"] = nueva_duracion
                modificaciones.append("-Duración")

            case "5":
                nueva_clasificacion = input("¿La nueva película ingresada es ATP? (si/no): ").lower().strip()
                while nueva_clasificacion not in ["si", "no"] or nueva_clasificacion.isspace():
                    print("ERROR")
                    nueva_clasificacion = input("Ingrese una respuesta válida (si/no): ").lower().strip()
                pelicula_existente["Clasificacion"] = (nueva_clasificacion == "si")
                modificaciones.append("-Clasificación")

            case "6":
                nueva_plataforma = input("Ingrese la nueva plataforma en la que se encuentra la película: ").capitalize().strip()
                while not nueva_plataforma or len(nueva_plataforma) > 20 or nueva_plataforma not in plataformas:
                    if not nueva_plataforma:
                        print("No puede ingresar un espacio en blanco.")
                    elif nueva_plataforma not in plataformas:
                        print("Ingrese una plataforma existente.")
                        nueva_plataforma = input("Ingrese la plataforma en la que se encuentra la película: ").capitalize().strip()
                    pelicula_existente["Plataforma"] = nueva_plataforma
                    modificaciones.append("-Plataforma")
            case  "7":
                break
            
            case  _:
                print("Valor inexistente, ingrese una opción valida")
            
        continuar = input("¿Desea modificar otro dato? (si/no): ").lower().strip()
        if not continuar or continuar.isspace():
            print("ERROR")
        elif continuar != 'si':
            break
        
    if modificaciones:
        print("\nSe realizaron las siguientes modificaciones:\n")
        for modificacion in modificaciones:
            print(modificacion)
    elif not modificaciones:
        print("No se realizaron modificaciones.")