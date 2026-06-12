import csv
import os

archivo_csv = "paises.csv"

def mostrar_menu():
    print("""
        \n
        -------Menu de Gestión de Datos de Países-------
        1- Agregar pais y continente
        2- Actualizar datos de pobleción y superficie
        3- Filtra países
        4- Ordenar países
        5- Mostrar estadíscas
        6- Salir
""")

def normalizar_texto(texto):
    texto = texto.lower().strip()
    reemplazos = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u",
    "ü": "u",
    "Á": "A",
    "É": "E",
    "Í": "I",
    "Ó": "O",
    "Ú": "U",
}
    for con_tilde, sin_tilde in reemplazos.items():
        texto = texto.replace(con_tilde, sin_tilde)
    return texto

def leer_entero(mensaje: str) -> int:
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: El número no puede ser negativo.")
            else:
                return valor
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

def leer_cadena(mensaje: str) -> str:
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor.title()
        print("Error: El campo no puede estar vacío.")

def lista_tiene_datos(paises:list):
    if not paises:
        print("\n" + "!"*40)
        print("Error: la lista de paises está vacia")
        print("Por favor, utilice la opción 1 antes de proceder con cualquier otra opción.") 
        print("!"*40)
        return False
    return True

def leer_continente():
    continentes= ["america", "europa", "asia", "africa", "oceania"]
    while True:
        print ("\n Seleccione un continente: ")
        for i, continente in enumerate(continentes, 1):
            print(f"{i}. {continente.capitalize()}")
        opcion = input("Ingrese el número del continente: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(continentes):
            return continentes[int(opcion) - 1]
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

def carga_datos():
    paises= []
    if not os.path.exists(archivo_csv):
        print(f"Archivo '{archivo_csv}' no encontrado. Se creará un nuevo archivo al agregar datos.")
        return paises
    try:
        with open(archivo_csv, mode='r', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                try:
                    paises.append({
                        "nombre": fila["nombre"],
                        "continente": fila["continente"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"])
                    })
                except ValueError:
                    print(f"Error al convertir datos de la fila: {fila}. Se omitirá esta fila.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return paises

def guardar_datos(paises:list):
    try:
        with open(archivo_csv, mode='w', encoding='utf-8', newline='') as archivo:
            campos = ["nombre", "continente", "poblacion", "superficie"]
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writeheader()
            writer.writerows(paises)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def agregar_pais(paises:list):
    nombre = leer_cadena("Ingrese el nombre del país: ")
    for p in paises:
        if normalizar_texto(p["nombre"]) == normalizar_texto(nombre):
            print("Error: El país ya existe en la lista.")
            return
    continente = leer_continente()
    poblacion = leer_entero("Ingrese la población del país: ")
    superficie = leer_entero("Ingrese la superficie del país (en km²): ")
    nuevo_pais = {
        "nombre": nombre,
        "continente": continente,
        "poblacion": poblacion,
        "superficie": superficie
    }
    paises.append(nuevo_pais)
    guardar_datos(paises)
    print(f"País '{nombre}' agregado exitosamente.")

def actualizar_datos(paises:list):
    if not lista_tiene_datos(paises):
        return
    nombre = leer_cadena("Ingrese el nombre del país a actualizar: ")
    for pais in paises:
        if normalizar_texto(pais["nombre"]) == normalizar_texto(nombre):
            print(f"Actualizando datos para {pais['nombre']}:")
            pais["poblacion"] = leer_entero("Ingrese la nueva población del país: ")
            pais["superficie"] = leer_entero("Ingrese la nueva superficie del país (en km²): ")
            guardar_datos(paises)
            print(f"Datos de '{pais['nombre']}' actualizados exitosamente.")
            return
    print("Error: País no encontrado en la lista.")

def imprimir_tabla(paises: list):
    print(f"\n{'-'*65}")
    print(f"{'NOMBRE':<20} | {'POBLACIÓN':<15} | {'SUPERFICIE':<12} | {'CONTINENTE'}")
    print(f"{'-'*65}")
    for p in paises:
        print(f"{p['nombre']:<20} | {p['poblacion']:<15} | {p['superficie']:<12} | {p['continente']}")
    print(f"{'-'*65}")
