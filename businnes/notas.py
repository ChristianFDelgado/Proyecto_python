import json
import os

def cargar_notas_desde_archivo():
    try:
        with open(os.path.join("data", "notas.json"), 'r') as archivo_json:
            lista_notas = json.load(archivo_json)
            print("La lista de notas ha sido cargada")
            return lista_notas
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []

def guardar_notas_en_archivo(nombre_archivo, datos):
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

def calcular_nota_final(notas_modulo):
    peso_prueba_teorica = 0.3
    peso_prueba_practica = 0.6
    peso_quices = 0.1

    nota_teorica = notas_modulo.get("prueba_teorica", 0)
    nota_practica = notas_modulo.get("prueba_practica", 0)
    quices = notas_modulo.get("quices", 0)

    nota_final = (((nota_teorica * peso_prueba_teorica) + (nota_practica * peso_prueba_practica) + (quices * peso_quices)) / 5)
    return round(nota_final, 2)

def evaluar_estado_modulo(nota_modulo):
    return "Aprobado" if nota_modulo >= 60 else "En Riesgo" 

def ingresar_notas():
    notas = []

    cedula_ejemplo = input("Ingrese la cédula del estudiante: ")
    nombre_ruta = input("Ingrese el nombre de la ruta del estudiante: ")

    # Obtener la información de notas.json si ya existe
    try:
        notas = cargar_notas_desde_archivo()
    except FileNotFoundError:
        pass

    # Verificar si ya existen notas para el estudiante en la ruta dada
    estudiante_existente = next((est for est in notas if est["cedula"] == cedula_ejemplo and est["nombre_ruta"] == nombre_ruta), None)
    if estudiante_existente:
        print("¡Error! Notas ya ingresadas para este estudiante en la ruta especificada.")
        return

    # Solicitar las notas para cada módulo
    notas_estudiante = {"cedula": cedula_ejemplo, "nombre_ruta": nombre_ruta, "notas": {}}
    modulos = ["fundamentos", "programacion_web", "programacion_formal", "bases_de_datos", "backend"]

    for modulo in modulos:
        print(f"\nIngresar notas para el módulo: {modulo}")
        prueba_teorica = float(input("Ingrese la nota de la prueba teórica: "))
        prueba_practica = float(input("Ingrese la nota de la prueba práctica: "))
        quices = float(input("Ingrese la nota de los quices: "))
        nota_modulo = ((prueba_practica * 0.3) + (prueba_teorica * 0.6) + (quices * 0.1))

        notas_modulo = {"prueba_teorica": prueba_teorica, "prueba_practica": prueba_practica, "quices": quices, "nota_modulo": round(nota_modulo, 2)}
        estado_modulo = evaluar_estado_modulo(nota_modulo)

        notas_estudiante["notas"][modulo] = {"estado": estado_modulo, **notas_modulo}

    # Calcular la nota final del estudiante
    notas_estudiante["nota_final"] = round(sum(calcular_nota_final(notas_modulo) for notas_modulo in notas_estudiante["notas"].values()), 2)
    notas_estudiante["estado"] = evaluar_estado_modulo(notas_estudiante["nota_final"])

    # Agregar las notas del estudiante a la lista de notas
    notas.append(notas_estudiante)

    # Guardar datos actualizados en el archivo JSON
    guardar_notas_en_archivo("notas.json", notas)

def consultar_campers_en_riesgo_por_cedula():
    cedula_buscada = input("Ingrese la cédula del camper a buscar: ")

    try:
        notas = cargar_notas_desde_archivo()
    except FileNotFoundError:
        print("No hay datos de notas disponibles. Por favor, ingrese notas primero.")
        return

    campers_en_riesgo = []

    for estudiante in notas:
        cedula = estudiante["cedula"]
        nombre_ruta = estudiante["nombre_ruta"]
        estado_general = estudiante["estado"]
        notas_modulos = estudiante["notas"]

        for modulo, info_modulo in notas_modulos.items():
            estado_modulo = info_modulo["estado"]

            if estado_modulo == "En Riesgo" and cedula_buscada == cedula:
                camper_en_riesgo = {
                    "cedula": cedula,
                    "nombre_ruta": nombre_ruta,
                    "modulo": modulo,
                    "estado_modulo": estado_modulo
                }
                campers_en_riesgo.append(camper_en_riesgo)

    if not campers_en_riesgo:
        print(f"No hay campers en riesgo con la cédula {cedula_buscada}.")
    else:
        print(f"\nCampers en riesgo con la cédula {cedula_buscada}:")
        for camper in campers_en_riesgo:
            print(f"Cedula: {camper['cedula']}, Ruta: {camper['nombre_ruta']}, Módulo: {camper['modulo']}, Estado del Módulo: {camper['estado_modulo']}")

def cargar_datos_desde_archivo(archivo):
    try:
        with open(os.path.join("data", archivo), 'r') as archivo_json:
            datos = json.load(archivo_json)
            #print(f"La lista de {archivo} ha sido cargada")
            return datos
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe. Puede que aún no haya datos guardados.")
        return []
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo}. El formato podría ser incorrecto.")
        return []
    except Exception as e:
        print(f"Error desconocido al cargar datos desde {archivo}: {e}")
        return []

def listar_campers_en_riesgo():
    try:
        campers = cargar_datos_desde_archivo("campers.json")
        notas = cargar_datos_desde_archivo("notas.json")

        campers_en_riesgo = []

        for camper_notas in notas:
            cedula = camper_notas["cedula"]
            nombre_ruta = camper_notas["nombre_ruta"]

            # Buscar el camper por cédula en la lista de campers
            camper = next((c for c in campers if c["cedula"] == cedula), None)

            if camper:
                for modulo, notas_modulo in camper_notas["notas"].items():
                    if notas_modulo["estado"] == "En Riesgo":
                        campers_en_riesgo.append({
                            "cedula": cedula,
                            "nombre": camper["nombre"],
                            "apellidos": camper["apellidos"],
                            "nombre_ruta": nombre_ruta,
                            "modulo": modulo,
                            "nota_modulo": notas_modulo["nota_modulo"]
                        })

        if campers_en_riesgo:
            print("Campers en riesgo:")
            for camper in campers_en_riesgo:
                print(f"Cédula: {camper['cedula']}, Nombre: {camper['nombre']} {camper['apellidos']}, Ruta: {camper['nombre_ruta']}, Módulo: {camper['modulo']}, Nota: {camper['nota_modulo']}")
        else:
            print("No hay campers en riesgo.")

    except Exception as e:
        print(f"Error desconocido al listar campers en riesgo: {e}")
