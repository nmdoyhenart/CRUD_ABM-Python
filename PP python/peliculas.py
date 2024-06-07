"""""
Nombre: Nicolás
Apellido: Doyhenart

Parcial 07/03
"""""

def crear_pelicula(id: int, titulo: str, genero: str, año_lanzamiento: int, duracion: int, clasificacion: bool):
    diccionario_empleado = {
        "ID": id,
        "Titulo": titulo,
        "Genero": genero,
        "Año lanzamiento": año_lanzamiento,
        "Duracion": duracion,
        "Clasificacion": clasificacion
    }

    return diccionario_empleado

def eliminar_pelicula(lista_peliculas: list[dict]):
    titulo_pelicula_eliminada = int(input("Ingrese el titulo de la pelicula a eliminar: "))
    pelicula_eliminada = None
    for pelicula in lista_peliculas:
        if pelicula["Titulo"] == titulo_pelicula_eliminada:
            print("Empleado encontrado y eliminado")
            pelicula_eliminada = pelicula

    if pelicula_eliminada != None:
        lista_peliculas.remove(pelicula_eliminada)

        return pelicula_eliminada

    else:
        print("Empleado inexistente")

def mostrar_pelicula(pelicula: list[dict]):
    print("***********************************************************************")
    encabezado = "     Título      Género       Año lanzamiento       Duración     Clasificación"
    print(encabezado)
    print(f"{pelicula['Titulo']:>10}{pelicula['Genero']:>12}{pelicula['Año lanzamiento']:>12}{pelicula['Duracion']:>12}{pelicula['Clasificacion']:>12}")
    print("***********************************************************************")

def mostrar_todas(lista_peliculas: list[dict]):
    for pelicula in lista_peliculas:
        mostrar_pelicula(pelicula)

def ordenar_lista_ascendente(lista_peliculas: list[dict], llave):
    n = len(lista_peliculas)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_peliculas[j][llave] > lista_peliculas[j+1][llave]:
                lista_peliculas[j], lista_peliculas[j+1] = lista_peliculas[j+1], lista_peliculas[j]

def ordenar_lista_descendente(lista_peliculas: list[dict], llave):
    n = len(lista_peliculas)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_peliculas[j][llave] < lista_peliculas[j+1][llave]:
                lista_peliculas[j], lista_peliculas[j+1] = lista_peliculas[j+1], lista_peliculas[j]

def ordenar_peliculas(lista_peliculas: list[dict]):
    while True:
            opcion = input("""¿Como desea ordenar los datos?\n1- Titulo\n2- Genero\n3- Año de lanzamiento\n4- Duración\nElija una opción: """)
            
            match opcion:
                    case "1":
                        opcion_asc_desc = input("Ingrese de que manera quiere ordenar\n1- Ascendente\n2- Descendente\n")
                        match opcion_asc_desc:
                            case "1":
                                ordenar_lista_ascendente(lista_peliculas, "Titulo")
                            case "2":
                                ordenar_lista_descendente(lista_peliculas, "Titulo")
                    case "2":
                        opcion_asc_desc = input("Ingrese de que manera quiere ordenar\n1- Ascendente\n2- Descendente\nElija una opción: ")
                        match opcion_asc_desc:
                            case "1":
                                ordenar_lista_ascendente(lista_peliculas, "Genero")
                            case "2":
                                ordenar_lista_descendente(lista_peliculas, "Genero")
                    case "3":
                        opcion_asc_desc = input("Ingrese de que manera quiere ordenar\n1- Ascendente\n2- Descendente")
                        match opcion_asc_desc:
                            case "1":
                                ordenar_lista_ascendente(lista_peliculas, "Año lanzamiento")
                            case "2":
                                ordenar_lista_descendente(lista_peliculas, "Año lanzamiento")
                    case "4":
                        opcion_asc_desc = input("Ingrese de que manera quiere ordenar\n1- Ascendente\n2- Descendente")
                        match opcion_asc_desc:
                            case "1":
                                ordenar_lista_ascendente(lista_peliculas, "Duracion")
                            case "2":
                                ordenar_lista_descendente(lista_peliculas, "Duracion")
            break

def buscar_por_titulo(lista_empleados: list):
    titulo_pelicula = input("Ingrese el título de la pelicula que desee: ")
    while True:
        for pelicula in lista_empleados:
            if pelicula["Titulo"] == titulo_pelicula:
                print("***********************************************************************")
                encabezado = "      Título       Género      Año de lanzamiento       Duración       ATP    "
                print(encabezado)
                print(f"{pelicula['Titulo']:>10}{pelicula['Genero']:>12}{pelicula['Año lanzamiento']:>12}{pelicula['Duracion']:>12}{pelicula['Clasificacion']:>12}")
                print("***********************************************************************")
                break
            else:
                print("Película inexistente.")
                break
        break

def calcular(lista_peliculas: list[dict]):
    while True:
        opcion = input("""¿Que desea calcular?\n1- Duración promedio de todas las peliculas\n2- Porcentaje de peliculas ATP\nElija una opción: """)

        match opcion:
            case "1":
                pass
            
            case "2":
                pass

def porcentaje(lista_empleados: list[dict]):
    while True:
        opcion = input("""¿Que desea calcular?\n1- Porcentaje por genero\n2- Porcentaje de películas ATP\nElija una opción: """)

        match opcion:
            case "1":
                pass

            case "2":
                pass