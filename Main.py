from funciones import mostrar_menu, agregar_pais, actualizar_pais, buscar_pais, filtrar_paises, ordenar_paises, mostrar_estadisticas

'''
Trabajo Integrador Programación I
'''

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