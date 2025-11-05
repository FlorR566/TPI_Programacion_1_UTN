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
  
    # Si el archivo NO existe, se crea crea con encabezado vacío:
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
    continentes = ["america", "europa", "asia", "africa", "oceania", "antartida"]
    entrada = input(f"Ingrese el continente: ").strip().lower()
    while True:
        if not entrada in continentes:
           entrada = input("❌ [ERROR] Ingrese un continente válido: ").strip()
        
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
        
        entrada = input(f"\n ⚠️ [ERROR]: ingrese solo números enteros para la {categoria}: ").strip()





def validar_pais():
    '''
    Solicita un continente al usuario y valida que el texto 
    ingresado sea un continente válido dentro del array continentes.
    '''
    while True: 
        nombre = input("Ingrese nombre del país: ")
        
        if not nombre: 
            print("⚠️ [ADVERTENCIA] Se ingresó un nombre vacío.")
            nombre = input("Ingrese nombre del país: ")
            return

        if existe_pais(nombre):
            print("⚠️ [ADVERTENCIA] El país ya existe, ingrese otro.")
            nombre = input("Nombre del país: ")
            return
    
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

    entrada_poblacion = input("Ingrese la poblacion: ").strip()
    poblacion = validar_cantidad("poblacion", entrada_poblacion )

    entrada_superficie = input("Ingrese la superficie: ").strip()
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
            buscar_nombre = input("⚠️ [ADVERTENCIA] No se encuentra el país, ingrese otro: ")
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
    Busca un país por nombre, usando coincidencia parcial o exacta
    '''
    print("\n--- BUSCAR PAÍS ---")

    buscar_nombre = input("Ingrese el nombre del país a buscar: ").strip()

    while True:
        if not existe_pais(buscar_nombre):
            buscar_nombre = input("⚠️ [ADVERTENCIA] No se encuentra el país, ingrese otro: ")
        else: 
            paises = obtenerPaises_csv()
            for pais in paises:
                if buscar_nombre.lower() == pais["NOMBRE"].lower():
                    print(f"\n País: {pais['NOMBRE'].title()} | Población: {pais['POBLACION']} | Superficie: {pais['SUPERFICIE']} km² | Continente: {pais['CONTINENTE'].title()}")
            break


def filtrar_por_continente():
    """
    Filtra países por continente
    """
    print("\n--- FILTRAR POR CONTINENTE ---")
    
    paises = obtenerPaises_csv()
    
    #Validar que hay países cargados
    if not paises:
        print("⚠️ [ADVERTENCIA] No hay países cargados.")
        return
    
    #Llamamos a la función validar_continente que ya teníamos
    continente = validar_continente()
    
    #Filtrar los países
    filtrar_paises = []
    for pais in paises:
        if pais["CONTINENTE"].lower() == continente.lower():
            filtrar_paises.append(pais)
    
    #Mostrar los resultados
    if filtrar_paises:
        print(f"\n Países del continente '{continente}': ")
        for pais in filtrar_paises:
            print(f"{pais["NOMBRE"]} - Población: {pais["POBLACION"]} - Superficie: {pais["SUPERFICIE"]} km²")
    else:
        print(f"⚠️ [ADVERTENCIA] No hay países del continente '{continente}'")
        


       
def filtrar_por_rango_poblacion():
    """
    Filtra países por rango de población
    """
    print("\n--- FILTRAR POR RANGO DE POBLACIÓN ---")
    
    paises = obtenerPaises_csv()
    
    #Validar que hay países cargados
    if not paises:
        print("⚠️ [ADVERTENCIA] No hay países cargados.")
        return
    
    print("Ingrese el rango de la población: ")
    
    #Validar el rango de la población mínima
    valor_min = input("Población mínima: ").strip()
    min_poblacion = validar_cantidad("Población mínima", valor_min)
    
    #Validar el rango de la población máxima
    valor_max = input("Población máxima: ").strip()
    max_poblacion = validar_cantidad("Población máxima", valor_max)
    
    #Validamos que el rango mínimo no sea mayor que el rango máximo de la población
    if min_poblacion > max_poblacion:
        print("❌ [ERROR] La población mínima no puede ser mayor que la población máxima")
        return
    
    #Filtrar los países
    filtrar_paises = []
    for pais in paises:
        if min_poblacion <= pais["POBLACION"] <= max_poblacion:
            filtrar_paises.append(pais)
    
    #Mostrar los resultados
    if filtrar_paises:
        print(f"\n✅ [OK] Países con población entre {min_poblacion} y {max_poblacion}: ")
        print(f"Se encontraron {len(filtrar_paises)} país(es)")
        for pais in filtrar_paises:
            print(f"{pais['NOMBRE']} - Población: {pais['POBLACION']} - Superficie: {pais['SUPERFICIE']} km² - Continente: {pais['CONTINENTE']}")
    else:
        print(f"⚠️ [ADVERTENCIA] No se encontraron países con población entre {min_poblacion} y {max_poblacion}")
    
    
   
   
def filtrar_por_rango_superficie():
    """
    Filtra países por rango de superficie
    """
    print("\n--- FILTRAR POR RANGO DE SUPERFICIE ---")
    
    paises = obtenerPaises_csv()
    
    #Validar que hay países cargados
    if not paises:
        print("⚠️ [ADVERTENCIA] No hay países cargados.")
        return
    
    print("Ingrese el rango de la superficie (km²): ")
    
     #Validar el rango de la superficie mínima
    valor_min = input("Superficie mínima: ").strip()
    min_superficie = validar_cantidad(f"Superficie mínima {valor_min} km²")
    
    #Validar el rango de la superficie máxima
    valor_max = input("Superficie máxima: ").strip()
    max_superficie = validar_cantidad(f"Superficie máxima {valor_max} km²")
    
    #Validamos que el rango mínimo no sea mayor que el rango máximo de la superficie
    if min_superficie > max_superficie:
        print("❌ [ERROR] La superficie mínima no puede ser mayor que la superficie máxima")
        return
    
    #Filtrar los países
    filtrar_paises = []
    for pais in paises:
        if min_superficie <= pais["SUPERFICIE"] <= max_superficie:
            filtrar_paises.append(pais)
    
    #Mostrar los resultados
    if filtrar_paises:
        print(f"\n✅ [OK] Países con superficie entre {min_superficie} y {max_superficie}: ")
        print(f"Se encontraron {len(filtrar_paises)} país(es)")
        for pais in filtrar_paises:
            print(f"{pais['NOMBRE']} - Población: {pais['POBLACION']} - Superficie: {pais['SUPERFICIE']} km² - Continente: {pais['CONTINENTE']}")
    else:
        print(f"⚠️ [ADVERTENCIA] No se encontraron países con superficie entre {min_superficie} y {max_superficie}")
        
        
        

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
    print("4. Filtrar países por continente")
    print("5. Filtrar países por rango de población")
    print("6. Filtrar países por rango de superficie")
    print("7. Ordenar países")
    print("8. Mostrar estadísticas")
    print("9. Salir")
    print("-"*50)

def main():
    
    print("¡Bienvenido al Sistema de Gestión de Datos de Países!")
   
    
    while True:
        mostrar_menu()
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
                filtrar_por_continente()

            
            case '5':
                filtrar_por_rango_poblacion()
            
            case '6':
                filtrar_por_rango_superficie()
            
            # case '7':
            #     ordenar_paises(paises)
            #     pass
            
            # case '8':
            #    valor =  mostrar_estadisticas(paises)
            #    pass
            
            case '9':
                print("\n¡Gracias por usar el Sistema de Gestión de Datos de Países! ")
                print("Saliendo del programa... 👋 \n")
                break
            
            case _:
                print("❌ [ERROR] Opción inválida. Por favor, seleccione (1-9).")


# Punto de entrada principal
main()