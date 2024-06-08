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
    if pelicula["Clasificacion"]:
        auxiliar = "Si"
    else:
        auxiliar = "No"
    print("***********************************************************************")
    encabezado = f"{'Título':<20}{'Género':<20}{'Año lanzamiento':<20}{'Duración':<10}{'ATP':<5}"
    print(encabezado)
    print(f"{pelicula['Titulo']:<20}{pelicula['Genero']:<20}{pelicula['Año lanzamiento']:<20}{pelicula['Duracion']:<10}{auxiliar:<5}")
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
    titulo_pelicula = input("Ingrese el título de la película que desee: ").capitalize()
    encontrada = False

    for pelicula in lista_empleados:
        if pelicula["Titulo"].lower() == titulo_pelicula.lower():
            encontrada = True
            if (pelicula["Clasificacion"]):
                auxiliar = "Si"
            else:
                auxiliar = "No"
            print("***********************************************************************")
            encabezado = f"{'Título':<20}{'Género':<20}{'Año de lanzamiento':<20}{'Duración':<10}{'ATP':<5}"
            print(encabezado)
            print(f"{pelicula['Titulo']:<20}{pelicula['Genero']:<20}{pelicula['Año lanzamiento']:<20}{pelicula['Duracion']:<10}{auxiliar:<5}")
            print("***********************************************************************")
            break
        
        else:
            print("Película inexistente.")
            break

def calcular(lista_peliculas: list[dict]):
    while True:
        opcion = input("""¿Que desea calcular?\n1- Duración promedio de todas las peliculas\n2- Cantidad de peliculas lanzadas en cada año desde 2005 hasta 2024\nElija una opción: """)

        match opcion:
            case "1":
                auxiliar = 0
                for pelicula in range(len(lista_peliculas)):
                    auxiliar += lista_peliculas[pelicula]["Duracion"]
                
                auxiliar_promedio = auxiliar / len(lista_peliculas)
                print(f"La duracion promedio de todas las películas es: {auxiliar_promedio}")

            case "2":
                pass
        break

def porcentaje(lista_peliculas: list[dict]):
    while True:
        opcion = input("""¿Que desea calcular?\n1- Porcentaje por genero\n2- Porcentaje de películas ATP\nElija una opción: """)

        match opcion:
            case "1":
                pass
            
            case "2":
                auxiliar = 0
                for pelicula in range(len(lista_peliculas)):
                    auxiliar += lista_peliculas[pelicula]["Clasificacion"]

                auxiliar_porcentaje = (auxiliar / len(lista_peliculas)) * 100
                print(f"EL {auxiliar_porcentaje}% de películas son ATP.")
        break