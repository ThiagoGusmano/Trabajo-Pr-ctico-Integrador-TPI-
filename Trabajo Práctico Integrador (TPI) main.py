from funciones import *
def menu():
    paises = carga_datos()
    
    while True:
        print("\n" + "="*30)
        print("  SISTEMA DE GESTIÓN DE PAÍSES  ")
        print("="*30)
        print("1. Agregar un país")
        print("2. Actualizar población y superficie")
        print("3. Buscar un país")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            agregar_pais(paises)
        elif opcion == '2':
            if lista_tiene_datos(paises):
                actualizar_datos(paises)
        elif opcion == '3':
            if lista_tiene_datos(paises):
                buscar_pais(paises)
        elif opcion == '4':
            if lista_tiene_datos(paises):
                filtrar_pais(paises)
        elif opcion == '5':
            if lista_tiene_datos(paises):
                ordenar_paises(paises)
        elif opcion == '6':
            if lista_tiene_datos(paises):
                mostrar_estadisticas(paises)
        elif opcion == '7':
            print("\nGuardando datos y saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("\nError: Opción inválida. Intente nuevamente eligiendo un número del 1 al 7.")

if __name__ == "__main__":
    menu()