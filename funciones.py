import csv
import os

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

def lista_tiene_datos():
    if len(paises) == 0:
        print("\n" + "!"*40)
        print("Error: la lista de paises está vacia")
        print("Por favor, utilice la opción 1 antes de proceder con cualquier otra opción.") 
        print("!"*40)
        return False
    return True