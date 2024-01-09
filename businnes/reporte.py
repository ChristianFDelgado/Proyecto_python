import json
import os

def informe_aprobacion_modulos():
    def cargar_datos_desde_archivo(nombre_archivo):
        try:
            with open(os.path.join("data", nombre_archivo), 'r') as archivo_json:
                datos = json.load(archivo_json)
                #print(f"Los datos han sido cargados desde {nombre_archivo}")
                return datos
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe.")
            return []

    matriculas = cargar_datos_desde_archivo("matriculas.json")
    notas = cargar_datos_desde_archivo("notas.json")

    informe = {}# Creamos un diccionario para almacenar la información del informe

    
    for profesor in set(matricula["profesor_asignado"] for matricula in matriculas):
        informe[profesor] = {}
        for ruta in set(matricula["curso"] for matricula in matriculas):
            informe[profesor][ruta] = {modulo: {"Aprobados": 0, "Perdidos": 0} for modulo in list(set(modulo for nota in notas if nota["nombre_ruta"] == ruta for modulo in nota["notas"].keys()))}

    # Iteramos sobre las matrículas y notas
    for matricula in matriculas:
        cedula = matricula["cedula"]
        ruta = matricula["curso"]
        profesor = matricula["profesor_asignado"]

        # Verificamos si hay notas para esta cédula y ruta
        notas_estudiante = next((nota for nota in notas if nota["cedula"] == cedula and nota["nombre_ruta"] == ruta), None)

        # Si hay notas, actualizamos el informe
        if notas_estudiante:
            for modulo, estado in notas_estudiante["notas"].items():
                informe[profesor][ruta][modulo]["Aprobados"] += 1 if estado["estado"] == "Aprobado" else 0
                informe[profesor][ruta][modulo]["Perdidos"] += 1 if estado["estado"] != "Aprobado" else 0

    # Imprimimos el informe
    for profesor, rutas in informe.items():
        print(f"\nInforme para el profesor {profesor}:")
        for ruta, modulos in rutas.items():
            print(f"\nRuta: {ruta}")
            for modulo, estado in modulos.items():
                aprobados = estado["Aprobados"]
                perdidos = estado["Perdidos"]
                total = aprobados + perdidos
                print(f"{modulo}: Aprobados {aprobados}, Perdidos {perdidos}, Total {total}")


