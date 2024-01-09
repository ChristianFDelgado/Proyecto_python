import json
import os
from datetime import datetime

def obtener_disponibilidad():
    horas_disponibles = input(f"Ingrese las horas de disponibilidad:  (formato HH:MM, separadas por coma): ")
    horas_separadas = [hora.strip() for hora in horas_disponibles.split(",")]

    disponibilidad = {
        "lunes": horas_separadas,
        "martes": horas_separadas,
        "miercoles": horas_separadas,
        "jueves": horas_separadas,
        "viernes": horas_separadas,
    }

    return disponibilidad

def cargar_profesores_desde_archivo():
    try:
        with open(os.path.join("data", "profesores.json"), 'r') as archivo_json:
            lista_profesores = json.load(archivo_json)
            print("La lista de profesores ha sido cargada")
            return lista_profesores
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []

def cargar_cursos_desde_archivo():
    try:
        with open(os.path.join("data", "cursos.json"), 'r') as archivo_json:
            lista_cursos = json.load(archivo_json)
            print("La lista de cursos ha sido cargada")
            return lista_cursos
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []

def guardar_datos_en_archivo(nombre_archivo, datos):
    try:
        with open(os.path.join("data", nombre_archivo), 'w') as archivo_json:
            json.dump(datos, archivo_json, indent=2)
            print(f"Los datos han sido guardados en {nombre_archivo}")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe. Puede que aún no haya datos guardados.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {nombre_archivo}. El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido al guardar datos en {nombre_archivo}: {e}")

def crear_trainer():
    profesores_lista = cargar_profesores_desde_archivo()
    cursos_lista = cargar_cursos_desde_archivo()

    num_profesores = len(profesores_lista)
    if num_profesores == 0:
        num_profesores = int(input("Ingrese el número de profesores: "))

    for i in range(num_profesores):
        nombre_profesor = input(f"Ingrese el nombre del profesor {i + 1}/{num_profesores}: ")

        # Verificar si el profesor ya existe en la lista
        profesor_existente = next((profesor for profesor in profesores_lista if profesor["nombre"] == nombre_profesor), None)
        if profesor_existente:
            print(f"¡Error! El profesor {nombre_profesor} ya existe. Ingrese otro nombre.")
            continue  # Saltar a la siguiente iteración del bucle

        apellidos = input("Ingrese los apellidos del profesor: ")
        disponibilidad = obtener_disponibilidad()

        # Solicitar cursos para el profesor
        cursos_asignados = []
        while True:
            nombre_curso = input(f"Ingrese el nombre del curso para {nombre_profesor} (o 'fin' para terminar): ")
            if nombre_curso.lower() == 'fin':
                break

            # Verificar si el curso está disponible en al menos uno de los horarios del profesor
            curso_existente = next((curso for curso in cursos_lista if curso["nombre_ruta"] == nombre_curso), None)
            if not curso_existente:
                print(f"¡Error! El curso {nombre_curso} no existe. Ingrese un curso válido.")
                continue  # Volver a solicitar el nombre del curso

            horario_curso = curso_existente.get("horario", {})
            disponibilidad_profesor = set(hora for lista_horas in disponibilidad.values() for hora in lista_horas)
            
            if any(hora in disponibilidad_profesor for lista_horas in horario_curso.values() for hora in lista_horas):
                cursos_asignados.append({
                    "nombre_curso": nombre_curso,
                    "fecha_inicio": curso_existente["fecha_inicio"],
                    "fecha_fin": curso_existente["fecha_fin"],
                    "horario_curso": horario_curso
                })
            else:
                print(f"¡Error! El horario del curso {nombre_curso} no coincide con la disponibilidad del profesor.")
                continue  # Volver a solicitar el nombre del curso

        # Utilizar el nombre del profesor como clave en el diccionario
        nuevo_profesor = {
            "nombre": nombre_profesor,
            "apellidos": apellidos,
            "disponibilidad": disponibilidad,
            "cursos_asignados": cursos_asignados
        }
        profesores_lista.append(nuevo_profesor)

    # Guardar datos actualizados en el archivo JSON
    guardar_datos_en_archivo('profesores.json', profesores_lista)

def load_trainers_json():
    try:
      with open(os.path.join("data", "profesores.json"), 'r') as archivo_json:        
        lista_profesores = json.load(archivo_json)
        print("La lista de profesores ha sido guardada")
        return lista_profesores
    except Exception as e:
      print(f"Error al leer el archivo: {e}")
      
lista_profesores = load_trainers_json()

def listar_trainers():
    print("Listado de trainers que trabajan con Campus: ")
    print("\n")
    for trainer in lista_profesores:
        print(f"Trainer: {trainer['nombre']} {trainer['apellidos']} ")