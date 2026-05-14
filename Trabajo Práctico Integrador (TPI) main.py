from funciones import *
while True:
    mostrar_menu()
    opciones = input("Ingrese la opción: ")

    match opciones:
        case "1":
            ingreso_de_dato()
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            print("Gracias por usar el programa")
            break
        case _:
            print("Opcion invalida")
for pais in paises:
    print(pais)