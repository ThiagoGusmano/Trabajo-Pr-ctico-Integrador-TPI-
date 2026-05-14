#esta función unicamente imprime un menu en la consola
paises = []
def mostrar_menu():
    print("""
        -------Menu de Gestión de Datos de Países-------
        1- Agregar pais y continente
        2- Actualizar datos de pobleción y superficie
        3- Filtra países
        4- Ordenar países
        5- Mostrar estadíscas
        6- Salir
""")

def ingreso_de_dato():
    while True:
        nombre = input("Ingrese el nombre del país: ").strip().capitalize()
        if nombre == "" or nombre.isdigit():
            print("Error: ingreso valor invalido para país")
            return

        for pais in paises:
            if pais["nombre"] == nombre:
                print("Error: el país ya existe")
            return
        
        continente = input("Ingrese el continente: ").strip().capitalize()
        if continente == "" or continente.isdigit():
            print("Error:ingreso valor invalido para continente")
            return
        else:
            pais = {
                "nombre": nombre,
                "poblacion": 0,
                "superficie": 0,
                "continente": continente
            }
            paises.append(pais)
            print("País agregado correctamente")
            break

def actualizar_datos():
    pass