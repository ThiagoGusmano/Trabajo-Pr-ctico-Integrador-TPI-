import csv
import os

archivo_csv = "paises.csv"

#funciones de normalización y validación :O

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

# manejo de archivos :P

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

#funciones full del sistema del tpi :D

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

def buscar_pais(paises:list):
    print("\n--- BUSCAR PAÍS ---")
    termino = leer_cadena("Ingrese el nombre a buscar (parcial o exacto): ")
    termino_norm = normalizar_texto(termino)

    resultados = [p for p in paises if termino_norm in normalizar_texto (p["nombre"])]

    if resultados:
        imprimir_tabla(resultados)
    else:
        print("no se encontraron coicidencias.")

def filtrar_pais(paises:list):
    print("\n--- FILTRAR PAÍSES ---")
    print("1. Por Continente")
    print("2. Por Rango de Población")
    print("3. Por Rango de Superficie")
    opcion = input("Elija una opción de filtro: ")

    resultados = []
    if opcion == "1":
        continente = leer_continente()
        resultados = [p for p in paises if normalizar_texto (p["continente"]) == normalizar_texto(continente)]
    elif opcion == "2":
        min_pob = leer_entero("Superficie mínima: ")
        max_pob = leer_entero("Superficie maxima: ")
        resultados = [p for p in paises if min_pob <= p['poblacion'] <= max_pob]
    elif opcion == "3":
        min_sup = leer_entero("Superficie mínima: ")
        max_sup = leer_entero("Superficie maxima: ")
        resultados = [p for p in paises if min_sup <= p['superficie'] <= max_sup]
    else:
        print("Opción invalida.")
        return
    
    if resultados:
        imprimir_tabla(resultados)
    else:
        print("No hay países que cumplan con los criterios. ")

def ordenar_paises(paises:list):
    print("\n--- ORDENAR PAÍSES ---")
    print("1. Por Nombre (Alfabético)")
    print("2. Por Población")
    print("3. Por Superficie")
    opcion = input("Elija un criterio: ")

    if opcion not in ['1', '2', '3']:
        print("Opción inválida.")
        return
    
    orden = input("¿Orden Ascendete (A) o Desendente (D)?: ").strip().upper()
    desendente = True if orden == "D" else False

    if opcion == "1":
        paises_ordenados = sorted(paises, key=lambda x: x["nombre"], reverse=desendente)
    if opcion == "2":
        paises_ordenados = sorted(paises, key=lambda x: x["poblacion"], reverse=desendente)
    if opcion == "3":
        paises_ordenados = sorted(paises, key=lambda x: x["superficie"], reverse=desendente)

    imprimir_tabla(paises_ordenados)

def mostrar_estadisticas(paises: list):
    print("\n--- ESTADÍSTICAS ---")

    pais_mayor_pob = max(paises, key=lambda x: x["poblacion"])
    pais_menor_pob = min(paises, key=lambda x: x["poblacion"])

    total_poblacion = sum (p["poblacion"] for p in paises)
    total_superficie = sum (p["superficie"] for p in paises)
    promedio_pob = total_poblacion / len(paises)
    promedio_sup = total_superficie / len(paises)

    conteo_continentes = {}
    for p in paises:
        cont = p["continente"]
        if cont in conteo_continentes:
            conteo_continentes[cont] += 1
        else:
            conteo_continentes[cont] = 1

    print(f"País con MAYOR población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']:,})")
    print(f"País con MENOR población: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']:,})")
    print(f"Promedio de población global: {promedio_pob:,.2f}")
    print(f"Promedio de superficie global: {promedio_sup:,.2f} km²")
    print("\nCantidad de países por continente:")
    for cont, cant in conteo_continentes.items():
        print(f" - {cont}: {cant}")

#la funcion imprimir tablas es mas para enbellecer el resultado de la funcion filtrar paises UwU

def imprimir_tabla(paises: list):
    print(f"\n{'-'*65}")
    print(f"{'NOMBRE':<20} | {'POBLACIÓN':<15} | {'SUPERFICIE':<12} | {'CONTINENTE'}")
    print(f"{'-'*65}")
    for p in paises:
        print(f"{p['nombre']:<20} | {p['poblacion']:<15} | {p['superficie']:<12} | {p['continente']}")
    print(f"{'-'*65}")
