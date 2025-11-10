'''
Trabajo Integrador Programación I
'''

import csv
import os # Biblioteca encargada con funcionalidades dependientes del sistema operativo.

NOMBRE_ARCHIVO = "datosDePaises.csv"

def obtenerPaises_csv():    # Lee el archivo csv, y crea un diccionario por cada fila, lo agrega a la lista de diccionarios y finalmente devuelve la lista de diccionarios con return. 
    '''
    Lee el archivo CSV y devuelve una lista de paises como diccionarios.
    Si el archivo no existe, lo crea con encabezado y devuelve una lista vacía.
  
    Returns:
        list[dict]: lista de paises con claves 'NOMBRE' (string), 'POBLACION' (int), 'SUPERFICIE' (int), 'CONTINENTE' (string).
    '''

    paises= []
  
    # Si el archivo NO EXISTE, SE CREA con encabezado vacío:
    if not os.path.exists(NOMBRE_ARCHIVO): 
        with open (NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo: 
            escritor = csv.DictWriter(archivo, fieldnames=["NOMBRE", "POBLACION", "SUPERFICIE", "CONTINENTE"]) 
            escritor.writeheader() 
            return paises
  
    # Lectura del archivo existente:
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:     
        lector = csv.DictReader(archivo)                                     
    
        # Convierte las cantidades a int al leer:
        for fila in lector:
            paises.append({"NOMBRE": fila["NOMBRE"], "POBLACION": int(fila["POBLACION"]), "SUPERFICIE": int(fila["SUPERFICIE"]), "CONTINENTE": fila["CONTINENTE"]}) 
    
    return paises



def agregarPais_csv(pais):
    '''
    Agrega un nuevo pais al archivo CSV.

    Args:
        pais (dict): diccionario con claves 'NOMBRE', 'POBLACION', 'SUPERFICIE', 'CONTINENTE'.
    '''
    # Modo append ("a") -> agrega sin borrar los datos existentes:
    with open(NOMBRE_ARCHIVO, "a", newline="", encoding="utf-8") as archivo: 
        escritor = csv.DictWriter(archivo, fieldnames=["NOMBRE", "POBLACION", "SUPERFICIE", "CONTINENTE"])
        escritor.writerow(pais)



def guardarTodosPaises_csv(paises):
    '''
    Guarda una lista completa de los paises en el archivo CSV, sobreescribiendo su contenido actual.
    
    Args:
        paises (list[dict]): lista de paises con claves "NOMBRE", "POBLACION", "SUPERFICIE", "CONTINENTE".
    '''
    # Modo ("w") -> sobreescribe todo el archivo:
    with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo: 
        escritor = csv.DictWriter(archivo, fieldnames=["NOMBRE", "POBLACION", "SUPERFICIE", "CONTINENTE"])
        escritor.writeheader()          # escribe el título 
        escritor.writerows(paises)  



def coincidencia_parcial(paises):
    '''
    Busca países que coincidan con las primeras tres letras del texto ingresado por el usuasio.
    Muestra los resultados y permite seleccionar uno para ver sus datos completos.

    Args:
        paises (list): lista de diccionarios con datos de paises extraído del archivo csv.

    Returns:
        None (Muestra la información por consola).
    '''
    print("\n_____Coincidencia Parcial____")

    if len(paises) == 0:
        print("\n ⚠️  No hay países cargados.\n Puede ingresarlos en la opción 1 del menú general.")
        return

    buscar_nombre = input("\nIngrese el nombre del país a buscar: ").strip().lower()
    
    filtrar_paises = []

    # Busca coincidencias con la primera, segunda y tercer letra del pais
    for pais in paises:
        for i in range (1,4):
            if pais["NOMBRE"][:i] ==  buscar_nombre[:i]:
                if pais not in filtrar_paises:
                    filtrar_paises.append(pais)
                break
  
    if not filtrar_paises:
        print("⚠️  No se encontraron países con esas letras.")
        return

    print("\nCOINDIDENCIAS ENCONTRADAS:")
    # Muestra las coincidencias encontradas
    for pais_encontrado in filtrar_paises:
        print(f"\n [{filtrar_paises.index(pais_encontrado) +1}]: {pais_encontrado["NOMBRE"]}")
      
    # Solicita al usuario una opción para avanzar
    while True: 
        index = input("\n 👉 Elija una opción del listado: ").strip()

        if index.isdigit() and 1 <= int(index) <= len(filtrar_paises):
            index = int(index) -1
            # Muestra la opción elegida
            print(f"\nSeleccionaste: 🌎 País: {filtrar_paises[index]['NOMBRE'].title()} | Población: {filtrar_paises[index]["POBLACION"]} | Superficie: {filtrar_paises[index]["SUPERFICIE"]} | Continente: {filtrar_paises[index]["CONTINENTE"]}\n")
            break

        else:
            print("⚠️  Opción inválida.")
            continue



def coincidencia_exacta(paises):
    '''
    Busca paises en base a la coincidencia exacta.
    
    Args:
        paises (list): lista de diccionarios con datos de paises extraído del archivo csv.

    Returns:
        None (Muestra la información por consola).
    '''
    print("\n_____Coincidencia Exacta_____")

    if len(paises) == 0:
        print("\n ⚠️ No hay países cargados.\n Puede ingresarlos en la opción 1 del menú general.")
        return
    
    buscar_nombre = input("Ingrese el nombre del país a buscar: ").strip().lower()

    while True:
        if not buscar_nombre: 
            buscar_nombre =  input("❌ Se agregó un espacio vacío, ingrese nuevamente el nombre: ").strip().lower()
            continue
        if not existe_pais(buscar_nombre):
            buscar_nombre = input("❌ No se encontró el país. Ingrese otro nombre o escriba 'salir' para terminar: ").strip().lower()
            
            # Permite salir de la opción
            if buscar_nombre == "salir":
                break
        else: 
            for pais in paises:
                if buscar_nombre.lower() == pais["NOMBRE"].lower():
                    print(f"\n 🌎 País: {pais['NOMBRE'].title()} | Población: {pais['POBLACION']} | Superficie: {pais['SUPERFICIE']} km² | Continente: {pais['CONTINENTE'].title()}")
            break




def filtrar_por_continente(paises):
    '''
    Filtra países por continente.
    '''
    print("\n--- FILTRAR POR CONTINENTE ---")
    
    paises = obtenerPaises_csv()
    
    #Validar si hay países cargados
    if not paises:
        print("⚠️  No hay países cargados.")
        return
    
    # Llama a la función validar_continente
    continente = validar_continente()
    
    # Filtra los países
    filtrar_paises = []
    for pais in paises:
        if pais["CONTINENTE"].lower() == continente.lower():
            filtrar_paises.append(pais)
    
    # Muestra los resultados
    if filtrar_paises:
        print(f"\n 🌎  Países del continente '{continente.upper()}': ")
        for pais in filtrar_paises:
            print(f"* {pais["NOMBRE"].title()} - Población: {pais["POBLACION"]} - Superficie: {pais["SUPERFICIE"]} km²")
    else:
        print(f"⚠️  No hay países del continente '{continente}'")
        
    
   
def filtrar_por_rango_poblacion(paises):
    '''
    Filtra países por rango de población
    '''
    print("\n--- FILTRAR POR RANGO DE POBLACIÓN ---")
    
    print("\nIngrese el rango de la población: ")
    
    # Validar el rango de la población mínima
    valor_min = input("Población mínima: ").strip()
    min_poblacion = validar_cantidad("Población mínima", valor_min)
    
    # Validar el rango de la población máxima
    valor_max = input("Población máxima: ").strip()
    max_poblacion = validar_cantidad("Población máxima", valor_max)
    
    # Validamos que el rango mínimo no sea mayor que el rango máximo de la población
    if min_poblacion > max_poblacion:
        print("❌ La población mínima no puede ser mayor que la población máxima")
        return
    
    #Filtrar los países
    filtrar_paises = []
    for pais in paises:
        if min_poblacion <= pais["POBLACION"] <= max_poblacion:
            filtrar_paises.append(pais)
    
    #Mostrar los resultados
    if filtrar_paises:
        print(f"\n✅ Países con población entre {min_poblacion} y {max_poblacion}: ")
        print(f" 🌎 Se encontraron {len(filtrar_paises)} país(es)\n")
        for pais in filtrar_paises:
            print(f"* {pais['NOMBRE'].title()} - Población: {pais['POBLACION']} - Superficie: {pais['SUPERFICIE']} km² - Continente: {pais['CONTINENTE'].title()}")
    else:
        print(f"⚠️ No se encontraron países con población entre {min_poblacion} y {max_poblacion}")


   
def filtrar_por_rango_superficie(paises):
    '''
    Filtra países por rango de superficie
    '''
    print("\n--- FILTRAR POR RANGO DE SUPERFICIE ---")

    print("\nIngrese el rango de la superficie (km²): ")
    
     # Valida el rango de la superficie mínima
    valor_min = input("Superficie mínima: ").strip()
    min_superficie = validar_cantidad('valor mínimo',valor_min)
    
    # Valida el rango de la superficie máxima
    valor_max = input("Superficie máxima: ").strip()
    max_superficie = validar_cantidad('valor máximo',valor_max)
    
    # Valida que el rango mínimo no sea mayor que el rango máximo de la superficie
    if min_superficie > max_superficie:
        print("❌ La superficie mínima no puede ser mayor que la superficie máxima")
        return
    
    # Filtr los países
    filtrar_paises = []
    for pais in paises:
        if min_superficie <= pais["SUPERFICIE"] <= max_superficie:
            filtrar_paises.append(pais)
    
    # Muestra los resultados
    if filtrar_paises:
        print(f"\n✅ [OK] Países con superficie entre {min_superficie} y {max_superficie}: ")
        print(f"🌎 Se encontraron {len(filtrar_paises)} país(es)")
        for pais in filtrar_paises:
            print(f" * {pais['NOMBRE'].title()} - Población: {pais['POBLACION']} - Superficie: {pais['SUPERFICIE']} km² - Continente: {pais['CONTINENTE'].title()}")
    else:
        print(f"⚠️  No se encontraron países con superficie entre {min_superficie} y {max_superficie}")


   

def ordenar_por_nombre(paises):
    '''
    Ordena la lista paises por nombre utilizando algoritmo Buble Sort y los muestra por consola.
    
    Args:
        paises (list): lista de diccionarios con datos de paises extraído del archivo csv.

    Returns:
        None (Muestra la información por consola).
    '''
    print("\n--- ORDENAR PAISES POR NOMBRE ---")

    # Orden de países según nombre (usando algoritmo Buble Sort)
    n = len(paises)
    # Recorre todos los elementos de la lista
    for i in range(n):
        # Se optimiza para no compaparar elementos ya ordenados al final
        # (n-i-1) porque los últimos 'i' elementos ya están en su lugar    
        for j in range(0, n-i-1):
            # Compara el nombre actual con el siguiente
            if paises[j]["NOMBRE"] > paises[j+1]["NOMBRE"]:
                # Si el nombre actual es lexicamente mayor, los intercambia
                paises[j], paises[j+1] = paises[j+1],paises[j]

    # Muestra el resultado 
    for pais in paises:
        print(f"\n 🌎 {pais['NOMBRE'].title()} | Población: {pais['POBLACION']} | Superficie: {pais['SUPERFICIE']} km² | {pais['CONTINENTE'].title()}")




def ordenar_por_poblacion(paises):
    '''
    Ordena la lista paises por población (ascendente) utilizando algoritmo Buble Sort y los muestra por consola.
    
    Args:
        paises (list): lista de diccionarios con datos de paises extraído del archivo csv.

    Returns:
        None (Muestra la información por consola).
    '''
    print("\n--- ORDENAR PAISES POR POBLACION (ASCENDENTE) ---")

    # Orden de países según población (usando algoritmo Buble Sort)
    n = len(paises)
    # Recorre todos los elementos de la lista
    for i in range(n):   
        for j in range(0, n-i-1):
            # Compara el nombre actual con el siguiente
            if paises[j]["POBLACION"] > paises[j+1]["POBLACION"]:
                # Si el nombre actual es lexicamente mayor, los intercambia
                paises[j], paises[j+1] = paises[j+1],paises[j]

    # Muestra el resultado 
    for pais in paises:
        print(f"\n 🌎 Población: {pais['POBLACION']} | {pais['NOMBRE'].title()} | Superficie: {pais['SUPERFICIE']} km² | {pais['CONTINENTE'].title()}")



def ordenar_superficie_ascendente(paises):
    '''
    Ordena la lista paises por superficie (orden Ascendente) utilizando algoritmo Buble Sort y los muestra por consola.
    
    Args:
        paises (list): lista de diccionarios con datos de paises extraído del archivo csv.

    Returns:
        None (Muestra la información por consola).
    '''
    print("\n--- ORDENAR PAISES POR SUPERFICIE (ORDEN ASCENDENTE) ---")

    n = len(paises)

    # Recorre todos los elementos de la lista
    for i in range(n):  
        for j in range(0, n-i-1):
            if paises[j]["SUPERFICIE"] > paises[j+1]["SUPERFICIE"]:
                paises[j], paises[j+1] = paises[j+1],paises[j]

    # Muestra el resultado 
    for pais in paises:
        print(f"\n 🌎 Superficie: {pais['SUPERFICIE']} km² | {pais['NOMBRE'].title()} | Población: {pais['POBLACION']} | {pais['CONTINENTE'].title()}")




def orden_superficie_descendente(paises):
    '''
    Ordena la lista paises por superficie (orden Descendente) utilizando algoritmo Buble Sort y los muestra por consola.
    
    Args:
        paises (list): lista de diccionarios con datos de paises extraído del archivo csv.

    Returns:
        None (Muestra la información por consola).
    '''
    print("\n--- ORDENAR PAISES POR SUPERFICIE (ORDEN DESCENDENTE) ---")

    n = len(paises)

    # Recorre todos los elementos de la lista
    for i in range(n):  
        for j in range(0, n-i-1):
            if paises[j]["SUPERFICIE"] < paises[j+1]["SUPERFICIE"]:
                paises[j], paises[j+1] = paises[j+1],paises[j]

    # Muestra el resultado 
    for pais in paises:
        print(f"\n 🌎 Superficie: {pais['SUPERFICIE']} km² | {pais['NOMBRE'].title()} | Población: {pais['POBLACION']} | {pais['CONTINENTE'].title()}")




def pais_mayor_menor_poblacion(paises):
    '''
    Ordena la lista de países según su población de menor a mayor, usando método de burbujeo.
    Y muestra por pantalla el país con mayor y menor población.
    
    Args:
        paises (list): lista de diccionarios con datos de paises extraído del archivo csv.
    '''
    n = len(paises)

    for i in range(n):
        for j in range(0, n-i-1):
            if paises[j]["POBLACION"] > paises[j+1]["POBLACION"]:
                paises[j], paises[j+1] = paises[j+1],paises[j]
    

    print("\n Pais con mayor población: ")
    print(f"🌎  {paises[n-1]['NOMBRE'].upper()} | Población: {paises[n-1]['POBLACION']} | | {paises[n-1]['SUPERFICIE']} km² | {paises[n-1]['CONTINENTE'].title()}")
    
    print("\n Pais con menor población: ")
    print(f"🌎  {paises[0]['NOMBRE'].upper()} | Población: {paises[0]['POBLACION']} | {paises[0]['SUPERFICIE']} km² | {paises[0]['CONTINENTE'].title()}")




def promedio (categoria, paises):
    '''
    Retorna en pantalla el promedio de la categoría seleccionada.
    '''
    n = len(paises)
    contador = 0

    for pais in paises:
        contador += pais[categoria.upper()]

    print(f"\n📊  El promedio de {categoria.lower()} es: {(contador/n):.2f}")




def paises_por_continente(paises):
    '''
    Muestra la cantidad de países por continente, según los datos acumulados en el archivo csv.
    Permite visualizar para cada continente los nombres todos los paises que le pertenecen, sus poblaciones y sus superficies.
    '''
    print("\n--- MOSTRAR PAÍSES POR CONTINENTE ---")

    # Crea un diccionario con key continente y el valor la lista de paises
    continentes = {}

    for pais in paises:
        continente = pais["CONTINENTE"].title()
        if continente not in continentes:
            continentes[continente] = []
        continentes[continente].append(pais)

    # Muestra el resultado
    for continente in continentes:
        lista_paises = continentes[continente]
        print(f"\n🌍 {continente} ( {len(lista_paises)} {"pais" if len(lista_paises) <= 1 else "paises" } )\n" + "-" * 45)
        for pais in lista_paises:
            print(f"• {pais["NOMBRE"].title()} | Población: {pais["POBLACION"]} | Superficie: {pais["SUPERFICIE"]} km²")
        print("-" * 45)

    print("\n✅ Se muestran los países correctamente.")




def existe_pais(nombre):
    '''
    Verifica si existe el país con el nombre indicado en el archivo.

    Args:
        nombre (str): nombre del pais a buscar
        
    Returns:
        bool: True si existe, False si no
    '''
    paises = obtenerPaises_csv() # Trae el listado de países

    # Recorre todos los países para buscar coincidencia por nombre
    for pais in paises:
        if pais["NOMBRE"].lower() == nombre.strip().lower():
            return True 

    return False # El país no existe en el listado



def validar_continente():
    '''
    Solicita un continente al usuario y valida que el texto 
    ingresado sea un continente válido dentro del array continentes.
    '''
    continentes = ["america", "europa", "asia", "africa", "oceania"]
    entrada = input(f"Ingrese el continente: ").strip().lower()
    while True:
        if not entrada in continentes:
           entrada = input("❌ Ingrese un continente válido: ").strip().lower()
        
        else:
            return entrada.lower()
        


def validar_cantidad(categoria, entrada):
    '''
    Valida que la entrada ingresada por el usuario sea un número entero positivo (<0).

    Args:
        categoria (str): nombre del parámetro que se evalúa (por ejemplo: "poblacion" o "superficie en km²").
        entrada (str): cantidad ingresada por el usuario.

    Returns:
        entrada (int): la cantidad validada y convertida a entero.

    '''
    while True:
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)
        
        entrada = input(f"\n ⚠️  Ingrese solo números enteros para {categoria}: ").strip()



def validar_pais():
    '''
    Solicita un nombre al usuario y valida que el texto 
    ingresado sea un pais válido dentro del array continentes.
    '''
    while True: 
        nombre = input("Ingrese nombre del país: ").strip().lower()

        # Validar que todas las palabras sean alfabéticas
        if not all(palabra.isalpha() for palabra in nombre.split()):
            print("\n ⚠️ El nombre solo puede contener letras (sin números ni símbolos).")
            continue

        if existe_pais(nombre):
            print("\n ⚠️  El país ya existe, ingrese otro.")
            nombre = input("Nombre del país: ")
            return nombre.lower()
    
        else:
            return nombre.lower()



def agregar_pais():
    '''
    Solicita al usuario los datos de un nuevo pais y lo agrega al archivo
    validando previamente que no exista y que los datos de población, superficie y continente sean válidos.
    '''
    obtenerPaises_csv() # Si no hay países cargados, inicializa el archivo csv

    print("\n-- AGREGAR UN PAIS --")

    nombre = validar_pais()

    entrada_poblacion = input("Ingrese la cantidad de poblacion: ").strip()
    poblacion = validar_cantidad("poblacion", entrada_poblacion )

    entrada_superficie = input("Ingrese la cantidad de superficie: ").strip()
    superficie = validar_cantidad("superficie", entrada_superficie )
    
    continente = validar_continente()
    
    agregarPais_csv({"NOMBRE": nombre, "POBLACION": poblacion, "SUPERFICIE": superficie, "CONTINENTE": continente  })

    print("✅ [OK] Se agregó correctamente")
   

    
def actualizar_pais():
    '''
    Solicita un nombre al usuario y si existe actualiza la superficie y la población del país 
    verificando que sean valores correctos y lo actualiza en el csv.
    '''
    print("\n--- ACTUALIZAR UN PAÍS ---")

    buscar_nombre = input("Ingrese el nombre del país a actualizar: ").strip()

    while True:
        if not existe_pais(buscar_nombre):
            buscar_nombre = input("⚠️  No se encuentra el país, ingrese otro: ")
        else: 
            break

    # Trae un array de paises: 
    paises = obtenerPaises_csv()

    for pais in paises: 
        if pais["NOMBRE"].lower() == buscar_nombre.lower():
            # Actualiza población:
            entrada_poblacion = input("Ingrese la cantidad de población a actualizar: ").strip()
            nueva_poblacion = validar_cantidad("población", entrada_poblacion)
            pais["POBLACION"] = nueva_poblacion
            print("✅ [OK] Población actualizada")
            
            # Actualiza la superficie: 
            entrada_superficie = input("Ingrese la superficie en km² a actualizar: ").strip()
            nueva_superficie = validar_cantidad("superficie en km²", entrada_superficie)
            pais["SUPERFICIE"] = nueva_superficie
            print("✅ [OK] Superficie actualizada")
    
    print("\n✅ [OK] País actualizado exitosamente.")

    guardarTodosPaises_csv(paises)



def buscar_pais():
    '''
    Busca un país por nombre, usando coincidencia parcial o exacta.

    '''
    print("\n--- BUSCAR PAÍS ---")
    # Guarda el array de países
    paises = obtenerPaises_csv()

    entrada = input(
    "\nSeleccione el tipo de búsqueda:\n"
    "  [1] Parcial - busca coincidencias parciales\n"
    "  [2] Exacta  - busca coincidencia completa\n"
    "Opción: ")

    while True:
        match entrada:
            case '1':
                # Búqueda con coincidencia parcial:
                coincidencia_parcial(paises)
                break

            case '2':
                # Búqueda con coincidencia exacta:
                coincidencia_exacta(paises)
                break

            case _:
                entrada = input("❌ Ingrese [1] Búsqueda Parcial, [2] Exacta o 'salir' para finalizar: ")

                # Permite salir de la opción
                if entrada == "salir":
                    break
                


def filtrar_paises():
    '''
    Filtra paises por continente, rango de población o rango de superficie.
    '''
    print("\n--- FILTRAR PAISES ---")
    paises = obtenerPaises_csv()

    # Valida si hay países cargados
    if not paises:
        print("⚠️  No hay países cargados.")
        return
    
    # Solicita input al usuario
    entrada = input(
    "\nSeleccione el tipo de filtro:\n"
    "  [1] Continente \n"
    "  [2] Rango Población \n"
    "  [3] Rango de Superficie \n"
    "Opción: ")

    while True:
        match entrada:
            case '1':
                # Ordena países según continente:
                filtrar_por_continente(paises)
                break

            case '2':
                # Ordena países según rango de población:
                filtrar_por_rango_poblacion(paises)
                break
            
            case '3':
                # Ordena países según rango de superficie: 
                filtrar_por_rango_superficie(paises)
                break

            case _:
                entrada = input("\n❌ Ingrese una de las opciones para ordenar: \n [1] Continente \n [2] Rango Población \n [3] Rango Superficie \n 'salir' para finalizar \n Opción: ")

                # Permite salir de la opción
                if entrada == "salir":
                    break
              


def ordenar_paises():
    '''
    Ordena paises por nombre, población o superficie (de manera ascendente o descendente)
    '''
    print("\n--- ORDENAR PAISES ---")
    paises = obtenerPaises_csv()

    # Valida si hay países cargados
    if not paises:
        print("⚠️  No hay países cargados.")
        return
    
    # Solicita input al usuario
    entrada = input(
    "\nSeleccione el tipo de ordenamiento:\n"
    "  [1] Nombre \n"
    "  [2] Población \n"
    "  [3] Superficie (orden ascendente) \n"
    "  [4] Superficie (orden descendente) \n"
    "Opción: ")

    while True:
        match entrada:
            case '1':
                # Ordena países por nombre:
                ordenar_por_nombre(paises)
                break

            case '2':
                # Ordena países según población:
                ordenar_por_poblacion(paises)
                break
            
            case '3':
                # Ordena países por superficie (Orden Adcendente):
                ordenar_superficie_ascendente(paises)
                break

            case '4':
                # Ordena países por superficie (Orden Descendente):
                orden_superficie_descendente(paises)
                break

            case _:
                entrada = input("\n❌ Ingrese una de las opciones para ordenar: \n [1] Nombre \n [2] Superficie \n [3] Poblacion Ascedente \n [4] Población Descendente \n 'salir' para finalizar \n Opción: ")

                # Permite salir de la opción
                if entrada == "salir":
                    break
              


def mostrar_estadisticas():
    '''
    Devuelve una serie de estadísticas que van desde mostrar el país con mayor y menor población, 
    el promedio de población, el promedio de superficie y cantidad de países por continente. 
    
    '''
    print("\n--- MOSTRAR ESTADÍSTICAS ---")
    paises = obtenerPaises_csv()

    # Valida si hay países cargados
    if not paises:
        print("⚠️  No hay países cargados.")
        return
    
    # Solicita input al usuario
    entrada = input(
    "\nSeleccione una opción:\n"
    "  [1] País con Mayor y Menor población \n"
    "  [2] Promedio de Población \n"
    "  [3] Promedio de Superficie \n"
    "  [4] Cantidad de países por continente \n"
    "Opción: ")

    while True:
        match entrada:
            case '1':
                # Muestra el país con mayor y menor población:
                pais_mayor_menor_poblacion(paises)
                break

            case '2':
                # Muestra el promedio de población:
                promedio("POBLACION", paises)
                break
            
            case '3':
                # Muestra el promedio de superficie:
                promedio("SUPERFICIE", paises)
                break

            case '4':
                # Muestra cuantos países hay por continente:
                paises_por_continente(paises)
                break

            case _:
                entrada = input("\n❌ Ingrese una de las opciones para ordenar: \n [1] País con Mayor y Menor Población \n [2] Promedio de Población \n [3] Promedio de Superficie \n [4] Cantidad de países por continente \n 'salir' para finalizar \n Opción: ")

                # Permite salir de la opción
                if entrada == "salir":
                    break
              






def mostrar_menu():
    '''
    Muestra el menú principal
    '''
    print("\n" + "="*50)
    print("       SISTEMA DE GESTIÓN DE DATOS DE PAÍSES")
    print("="*50)
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Salir")
    print("-"*50)

def main():
    
    print("\n¡Bienvenido al Sistema de Gestión de Datos de Países!")
    
    while True:
        mostrar_menu()    # Llamamos al menú de opciones 
        opcion = input("Seleccione una opción (1-9): ").strip()
        
        # Match/case para direccionar las opciones
        match opcion:
            case '1':
                agregar_pais()
            
            case '2':
                actualizar_pais()
        
            case '3':
                buscar_pais()
            
            case '4':
                filtrar_paises()
            
            case '5':
                ordenar_paises()
            
            case '6':
                mostrar_estadisticas()
                
            case '7':
                print("\n¡Gracias por usar el Sistema de Gestión de Datos de Países! ")
                print("Saliendo del programa... 👋 \n")
                break

            case _:
                print("❌ Opción inválida. Por favor, seleccione (1-9).")


# Punto de entrada principal
main()