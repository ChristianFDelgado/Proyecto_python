import json
import os


def load_aulas_json():
    try:
      with open(os.path.join("data", "aulas.json"), 'r') as archivo_json:        
        lista_aulas = json.load(archivo_json)
        print("La lista de aulas ha sido guardada")
        return lista_aulas
    except Exception as e:
      print(f"Error al leer el archivo: {e}")

lista_aulas = load_aulas_json()

def crear_aulas():
    nombre = input("Ingrese el nombre del aula: ")

    

    aula = {
        'nombre': nombre,
    }

    lista_aulas.append(aula)
    print("Se creó el aula con éxito")
    guardar_json()




def guardar_json():
    try:
      with open(os.path.join("data", "aulas.json"), 'w') as archivo_json:
        json.dump(lista_aulas, archivo_json, indent=2)
        print("La lista de aulas ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
      


def listar_aulas():
    print("Listado de Aulas: ")
    for aula in lista_aulas:
        print(aula)
