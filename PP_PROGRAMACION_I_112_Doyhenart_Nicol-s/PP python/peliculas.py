"""""
Nombre: Nicolás
Apellido: Doyhenart

Parcial 07/03
"""""
def eliminar_pelicula(lista_peliculas: list[dict]):
    """Comprueba si el título existe y lo elimina de la lista.

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
    """
    titulo_pelicula_eliminada = input("Ingrese el titulo de la pelicula a eliminar: ").capitalize()
    pelicula_eliminada = None
    for pelicula in lista_peliculas:
        if pelicula["Titulo"] == titulo_pelicula_eliminada:
            print("Pelicula encontrada y elimnada")
            pelicula_eliminada = pelicula

    if pelicula_eliminada != None:
        lista_peliculas.remove(pelicula_eliminada)

        return pelicula_eliminada

    else:
        print("Película fuera del catalogo.")

def mostrar_pelicula(pelicula: list[dict]):
    """Muestra la información de una pelicula

    Args:
        pelicula: list[dict]: Diccionario que contiene la información de una película.
    """
    if pelicula["Clasificacion"]:
        auxiliar = "Si"
    else:
        auxiliar = "No"
    print("*******************************************************************************************")
    encabezado = f"{'Título':<20}{'Género':<20}{'Año lanzamiento':<20}{'Duración':<10}{'ATP':<5}{'Plataforma':<15}"
    print(encabezado)
    print(f"{pelicula['Titulo']:<20}{pelicula['Genero']:<20}{pelicula['Año lanzamiento']:<20}{pelicula['Duracion']:<10}{auxiliar:<5}{pelicula['Plataforma']:<15}")
    print("*******************************************************************************************")
        
def mostrar_todas(lista_peliculas: list[dict]):
    """Muestra todas las películas en la lista

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
    """
    for pelicula in lista_peliculas:
        mostrar_pelicula(pelicula)

def mostrar_genero(lista_peliculas: list[dict]):
    """Muestra las películas de la lista y le solicita al usuario que ingrese el género que quiere ver.

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
    """
    genero = input("Ingrese el género que busca: ").capitalize()
    encontrado = False
    for pelicula in lista_peliculas:
        if pelicula["Genero"] == genero:
            mostrar_pelicula(pelicula)
            encontrado = True

    if not encontrado:
        print("Película fuera del catalogo.")

def mostrar_lanzamiento(lista_peliculas: list[dict]):
    """Muestra las películas de la lista y le solicita al usuario que ingrese el año de lanzamiento que quiera ver.

    Args:
        lista_pelicula: list[dict]: Diccionario que contiene la información de las películas.
    """
    año_lanzamiento = int(input("Ingrese el año de lanzamiento: "))
    encontrado = False
    for pelicula in lista_peliculas:
        if pelicula["Año lanzamiento"] == año_lanzamiento:
            mostrar_pelicula(pelicula)
            encontrado = True

    if not encontrado:
        print("Película fuera del catalogo.")

def mostrar_atp(lista_peliculas: list[dict]):
    """Muestra todas las películas ATP en la lista.

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
    """
    encontrado = False
    for pelicula in lista_peliculas:
       if pelicula["Clasificacion"] == True:
            mostrar_pelicula(pelicula)
            encontrado = True

    if not encontrado:
        print("Todas las pelocilas del catalogo son NO ATP.")

def mostrar_no_atp(lista_peliculas: list[dict]):
    """Muestra todas las películas NO ATP en la lista.

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
    """
    encontrado = False
    for pelicula in lista_peliculas:
        if pelicula["Clasificacion"] == False:
            mostrar_pelicula(pelicula)
            encontrado = True

    if not encontrado:
        print("Todas las peliculas del catalogo son ATP")

def mostrar_plataforma(lista_peliculas: list[dict]):
    plataforma = input("Ingrese la plataforma que busca: ").capitalize()
    encontrado = False
    for pelicula in lista_peliculas:
        if pelicula["Plataforma"] == plataforma:
            mostrar_pelicula(pelicula)
            encontrado = True

    if not encontrado:
        print("Plataforma no disponible en catalogo.")

def muestreo_peliculas(lista_peliculas: list[dict]):
    """Menu de muestreo y aplicación de funciones anteriores.

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
    """
    for pelicula in lista_peliculas:
        opciones = input("""¿Como desea ver nuestro catalogo?\n1- Todas las películas disponibles\n2- Género especifico\n3- Año de lanzamiento especifico\n4- Películas ATP\n5- Películas NO ATP\n6- Plataforma especifica\nElija una opción: """)

        match opciones:
            case "1":
                mostrar_todas(lista_peliculas)
            case "2":
                mostrar_genero(lista_peliculas)
            case "3":
                mostrar_lanzamiento(lista_peliculas)
            case "4":
                mostrar_atp(lista_peliculas)
            case "5":
                mostrar_no_atp(lista_peliculas)
            case "6":
                mostrar_plataforma(lista_peliculas)
            case  _:
                print("Valor inexistente, ingrese una opción valida")
        break

def ordenar_lista_ascendente(lista_peliculas: list[dict], llave: str):
    """Función que ordena de manera ascendente con un burbujeo

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
        llave: str: Utilizada como auxiliar para el correcto funcionamiento del ordenamiento
    """
    n = len(lista_peliculas)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_peliculas[j][llave] > lista_peliculas[j+1][llave]:
                lista_peliculas[j], lista_peliculas[j+1] = lista_peliculas[j+1], lista_peliculas[j]

def ordenar_lista_descendente(lista_peliculas: list[dict], llave: str):
    """Función que ordena de manera descendente con un burbujeo

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
        llave: str: Utilizada como auxliar para el correcto funcionamiento del ordenamiento
    """
    n = len(lista_peliculas)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_peliculas[j][llave] < lista_peliculas[j+1][llave]:
                lista_peliculas[j], lista_peliculas[j+1] = lista_peliculas[j+1], lista_peliculas[j]

def ordenar_peliculas(lista_peliculas: list[dict]):
    """Menu de ordenamiento que aplica las funciones de burbujeo.

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
    """    
    while True:
            opcion = input("""¿Como desea ordenar los datos?\n1- Titulo\n2- Genero\n3- Año de lanzamiento\n4- Duración\nElija una opción: """)
            
            match opcion:
                    case "1":
                        opcion_asc_desc = input("Ingrese de que manera quiere ordenar\n1- Ascendente\n2- Descendente\nElija una opción: ")
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
                        opcion_asc_desc = input("Ingrese de que manera quiere ordenar\n1- Ascendente\n2- Descendente\nElija una opción: ")
                        match opcion_asc_desc:
                            case "1":
                                ordenar_lista_ascendente(lista_peliculas, "Año lanzamiento")
                            case "2":
                                ordenar_lista_descendente(lista_peliculas, "Año lanzamiento")
                    case "4":
                        opcion_asc_desc = input("Ingrese de que manera quiere ordenar\n1- Ascendente\n2- Descendente\nElija una opción: ")
                        match opcion_asc_desc:
                            case "1":
                                ordenar_lista_ascendente(lista_peliculas, "Duracion")
                            case "2":
                                ordenar_lista_descendente(lista_peliculas, "Duracion")
                    case  _:
                        print("Valor inexistente, ingrese una opción valida")                                
            break

def buscar_por_titulo(lista_peliculas: list[dict]):
    """Busca la coincidencia en "Titulo" para mostrar la película solicita.

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
    """
    titulo_pelicula = input("Ingrese el título de la pelicula que desee: ").capitalize()
    pelicula_encontrada = False

    for pelicula in lista_peliculas:
        if pelicula["Titulo"] == titulo_pelicula:
            pelicula_encontrada = True
            if pelicula["Clasificacion"]:
                auxiliar = "Si"
            else:
                auxiliar = "No"
            print("***********************************************************************")
            encabezado = f"{'Título':<20}{'Género':<20}{'Año de lanzamiento':<20}{'Duración':<10}{'ATP':<5}"
            print(encabezado)
            print(f"{pelicula['Titulo']:<20}{pelicula['Genero']:<20}{pelicula['Año lanzamiento']:<20}{pelicula['Duracion']:<10}{auxiliar:<5}")
            print("***********************************************************************")
        
    if not pelicula_encontrada:
            print("Película fuera del catalogo.")

def años_peliculas(lista_peliculas: list[dict], año_inicio: int, año_fin: int):
    """Averigua cuantas peliculas fueron lanzadas entre los años ingresados por el usuario.

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
        año_inicio: int: Valor numerico que representa el inicio de la busqueda.
        año_fin: int: Valor numerico que representa el fin de la busqueda.
    """
    contador = 0

    for pelicula in lista_peliculas:
        lanzamiento = pelicula["Año lanzamiento"]
        if año_inicio <= lanzamiento <= año_fin:
            contador += 1

    return contador

def calcular(lista_peliculas: list[dict]):
    """Menu que calcula el promedio de todas las peliculas de la lista y utiliza la funcion años_peliculas

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
    """
    while True:
        opcion = input("""¿Que desea calcular?\n1- Duración promedio de todas las peliculas\n2- Cantidad de peliculas lanzadas en cada año\nElija una opción: """)

        match opcion:
            case "1":
                auxiliar = 0
                for pelicula in range(len(lista_peliculas)):
                    auxiliar += lista_peliculas[pelicula]["Duracion"]
                
                auxiliar_promedio = auxiliar / len(lista_peliculas)
                print(f"La duracion promedio de todas las películas es: {auxiliar_promedio}")

            case "2":
                año_inicio = int(input("Ingrese el año de inicio a comparar (Ej; 2005): "))
                año_fin = int(input("Ingrese el año de finalización a comparar (Ej; 2024): "))

                resultado = años_peliculas(lista_peliculas, año_inicio, año_fin)
                print(f"La cantidad de películas, en nuestro catálogo, entre {año_inicio} y {año_fin} son: {resultado}")
            
            case  _:
                print("Valor inexistente, ingrese una opción valida")
        break

def calcular_porcentaje_por_genero(lista_peliculas: list[dict]):
    """Calcula el porcentaje de películas de cada género.

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
    """
    conteo_generos = {}
    total_peliculas = len(lista_peliculas)

    for pelicula in lista_peliculas:
        genero = pelicula["Genero"]
        if genero in conteo_generos:
            conteo_generos[genero] += 1
        else:
            conteo_generos[genero] = 1

    porcentaje_generos = {}

    for genero in conteo_generos:
        porcentaje_generos[genero] = (conteo_generos[genero] / total_peliculas) * 100

    print("El porcentaje de películas por género es:")
    for genero in porcentaje_generos:
        print(f"{genero}: {porcentaje_generos[genero]:.2f}%")

def porcentaje(lista_peliculas: list[dict]):
    """Menu que aplica la funcion calcular_porcentaje_por_genero y el porcentaje de las películas ATP

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
    """
    while True:
        opcion = input("""¿Que desea calcular?\n1- Porcentaje por genero\n2- Porcentaje de películas ATP\nElija una opción: """)

        match opcion:
            case "1":
                calcular_porcentaje_por_genero(lista_peliculas)

            case "2":
                auxiliar = 0
                for pelicula in lista_peliculas:
                    if lista_peliculas[pelicula]["Clasificacion"] == ["Clasificacion"]:
                        auxiliar += 1

                auxiliar_porcentaje = (auxiliar / len(lista_peliculas)) * 100
                print(f"El {auxiliar_porcentaje}% de películas son ATP.")
                                
            case  _:
                print("Valor inexistente, ingrese una opción valida")               
        break