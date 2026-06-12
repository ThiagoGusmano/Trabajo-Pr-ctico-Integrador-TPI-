from funciones import *
paises=carga_datos()
def main():
    while True:
        mostrar_menu()
        opciones = int(input("Ingrese la opción: "))

        try:
            match opciones:
                case 1:
                    agregar_pais(paises)
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    print("Gracias por usar el programa")
                    break
        except ValueError:
            print("Ingrese una opción valida")
if __name__ == "__main__":
    main()