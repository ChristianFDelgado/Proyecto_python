import json
import os
from datetime import datetime

def obtener_disponibilidad():
    horas_disponibles = input(f"Ingrese el horario del curso:  (formato HH:MM, separadas por coma): ")
    horas_separadas = [hora.strip() for hora in horas_disponibles.split(",")]

    disponibilidad = {
        "lunes": horas_separadas,
        "martes": horas_separadas,
        "miercoles": horas_separadas,
        "jueves": horas_separadas,
        "viernes": horas_separadas,
    }

    return disponibilidad

def load_rutas_json():
    try:
      with open(os.path.join("data", "cursos.json"), 'r') as archivo_json:        
        lista_rutas = json.load(archivo_json)
        print("La lista de cursos ha sido guardada")
        return lista_rutas
    except Exception as e:
      print(f"Error al leer el archivo: {e}")
      
lista_rutas = load_rutas_json()

def listar_rutas():
    print("Listado de rutas: ")
    for rutas in lista_rutas:
        print(rutas)


def crear_rutas():
    
    print("Creacion de Rutas de Entrenamiento")
    nombreruta=input("Ingrese nombre de ruta principal: ")
    fechainicio=input("Ingrese fecha de inicio del programa (formato YYYY-MM-DD): ")
    fechafin=input("Ingrese fecha finalizacion del programa (formato YYYY-MM-DD): ")
    horario=obtener_disponibilidad()
    fundamentos=[]
    programacion_web=[]
    programacion_formal=[]
    bases_datos=[]
    backend=[]

    if (nombreruta == "Java") or (nombreruta == "NodeJS") or (nombreruta == "NetCore"):
        for i in range(3):
            nombre_fundamentos=input("Ingrese nombre de los fundamentos: ")
            fundamentos.append(nombre_fundamentos)
        for i in range(3):
            nombre_programacion_web=input("Ingrese nombre de temas de programacion web: ")
            programacion_web.append(nombre_programacion_web)
        for i in range(3):
            nombre_programacion_formal=input("Ingrese nombre de los temas de programacion formal: ")
            programacion_formal.append(nombre_programacion_formal)
        for i in range(2):
            nombre_base_datos=input("Ingrese nombre de las bases de datos ")
            bases_datos.append(nombre_base_datos)
        for i in range(3):
            nombre_backend=input("Ingrese nombre de los temas de backend: ")
            backend.append(nombre_backend)
    
        rutas = {
            'nombre_ruta': nombreruta,
            'fecha_inicio':fechainicio,
            'fecha_fin':fechafin,
            'horario':horario,
            'fundamentos': fundamentos,
            'programacion_web':programacion_web,
            'programacion_formal':programacion_formal,
            'bases_de_datos':bases_datos,
            'backend':backend
        }

        lista_rutas.append(rutas)
        print("Se creó la ruta con éxito")
        guardar_json()
    else:
       print("Ingrese nombre de ruta valido")


def guardar_json():
    try:
      with open(os.path.join("data", "cursos.json"), 'w') as archivo_json:
        json.dump(lista_rutas, archivo_json, indent=2)
        print("La lista de Rutas ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")

#Leer json campers
        
def load_campers_json():
    try:
      with open(os.path.join("data", "campers.json"), 'r') as archivo_json:        
        lista_campers = json.load(archivo_json)
        print("La lista de rutas ha sido guardada")
        return lista_campers
    except Exception as e:
      print(f"Error al leer el archivo: {e}")
      
lista_campers = load_campers_json()
lista_pruebas = []

#REGISTRAR NOTAS DE PRUEBA
def crear_notas():
    
    print("Registro de Notas de Prueba")
    cedula = input("Ingrese la cedula del camper a registrar las notas de sus pruebas: ")
    nota_final=0
    for estado in lista_campers:
        if (estado['cedula']==cedula) and (estado['estado'] == "Inscrito"):
            prueba_teorica = float(input(f"Ingrese la nota de la prueba teorica del camper {estado['nombre']}: "))
            prueba_practica = float(input(f"Ingrese la nota de la prueba practica del camper {estado['nombre']}: "))
            cedula=estado['cedula']
            nombre=estado['nombre']
            apellidos=estado['apellidos']
            nota_final = ((prueba_teorica+prueba_practica)/2)
        if nota_final >= 60:
           estado = "Aprobado"
        else:
           estado = "Reprobado"
           
    notas = {
        'cedula': cedula,
        'nombre': nombre,
        'apellidos':apellidos,
        'prueba_practica':prueba_practica,
        'prueba_teorica':prueba_teorica,
        'estado':estado
        }

    lista_pruebas.append(notas)
    print("Se creó la ruta con éxito")
    guardar_json_notas()

def guardar_json_notas():
    try:
      with open(os.path.join("data", "notas_prueba.json"), 'w') as archivo_json:
        json.dump(lista_pruebas, archivo_json, indent=2)
        print("La lista de Rutas ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")

#-------------------------------------------  ASIGNACION DE CAMPERS A RUTAS DE APRENDIZAJE ----------------------------------------------------
        
#Leer Json Notas Prueba
def load_notasprueba_json():
    try:
      with open(os.path.join("data", "notas_prueba.json"), 'r') as archivo_json:        
        lista_notas_prueba = json.load(archivo_json)
        print("La lista de notas ha sido guardada")
        return lista_notas_prueba
    except Exception as e:
      print(f"Error al leer el archivo: {e}")
lista_notas_prueba = load_notasprueba_json()
def load_asignaciones_json():
    try:
      with open(os.path.join("data", "asignaciones.json"), 'r') as archivo_json:        
        lista_asignaciones = json.load(archivo_json)
        print("La lista de asignaciones ha sido guardada")
        return lista_asignaciones
    except Exception as e:
      print(f"Error al leer el archivo: {e}")
lista_asignaciones = load_asignaciones_json()

#Asignar campers a ruta de aprendizaje

def asignar_campers():  
    print("Asigancion de Campers a Una Ruta de Aprendizaje")
    cedula = input("Ingrese la cedula del camper a registrar: ")
    nombre_ruta = input("Ingrese el nombre de la ruta a la que desea asignar el camper: ")
    contJava=0
    contNetcore=0
    contNodeJs=0
    for asignacion in lista_asignaciones:
       for  clave, valor in asignacion.items():
           if (clave=="ruta") and valor=="Java":
            contJava+=1
           elif (clave=="ruta") and valor=="NetCore":
            contNetcore+=1
           elif (clave=="ruta") and valor=="NodeJS":
            contNodeJs+=1

    for ruta in lista_rutas:
        if ((ruta['nombre_ruta']=="Java" and contJava < 33 and ruta['nombre_ruta']==nombre_ruta)):
            for estado in lista_notas_prueba:
                if (estado['cedula']==cedula):
                    if(estado['estado'] == "Aprobado"):
                        nombre = estado['nombre']
                        apellidos = estado['apellidos']
                        ruta = ruta['nombre_ruta']
                          
                        asignaciones = {
                            'cedula': cedula,
                            'nombre': nombre,
                            'apellidos':apellidos,
                            'ruta':ruta
                        }

                        lista_asignaciones.append(asignaciones)
                        print("Se creó la asignacion con éxito")
                        guardar_json_asignaciones()
                    else:
                       print(f"El estudiante {estado['nombre']} no aprobo")

        elif (ruta['nombre_ruta']=="NodeJS" and contNodeJs < 33 and ruta['nombre_ruta']==nombre_ruta):
           for estado in lista_notas_prueba:
                if (estado['cedula']==cedula):
                    if(estado['estado'] == "Aprobado"):
                        nombre = estado['nombre']
                        apellidos = estado['apellidos']
                        ruta = ruta['nombre_ruta']
                          
                        asignaciones = {
                            'cedula': cedula,
                            'nombre': nombre,
                            'apellidos':apellidos,
                            'ruta':ruta
                        }

                        lista_asignaciones.append(asignaciones)
                        print("Se creó la asignacion con éxito")
                        guardar_json_asignaciones()
                    else:
                       print(f"El estudiante {estado['nombre']} no aprobo")

        elif (ruta['nombre_ruta']=="NetCore" and contNetcore < 33 and ruta['nombre_ruta']==nombre_ruta):
           for estado in lista_notas_prueba:
                if (estado['cedula']==cedula):
                    if(estado['estado'] == "Aprobado"):
                        nombre = estado['nombre']
                        apellidos = estado['apellidos']
                        ruta = ruta['nombre_ruta']
                          
                        asignaciones = {
                            'cedula': cedula,
                            'nombre': nombre,
                            'apellidos':apellidos,
                            'ruta':ruta
                        }

                        lista_asignaciones.append(asignaciones)
                        print("Se creó la asignacion con éxito")
                        guardar_json_asignaciones()
                    else:
                       print(f"El estudiante {estado['nombre']} no aprobo")
        
        else:
           if (ruta['nombre_ruta']==nombre_ruta):
            print(f"El camper no se puede registrar en la ruta de aprendizaje {ruta['nombre_ruta']}")

def guardar_json_asignaciones():
    try:
      with open(os.path.join("data", "asignaciones.json"), 'w') as archivo_json:
        json.dump(lista_asignaciones, archivo_json, indent=2)
        print("La lista de Asignaciones ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
 #---------------------------------------------------------------------------------------------------------------------


def load_asignaciones_json():
    try:
      with open(os.path.join("data", "asignaciones.json"), 'r') as archivo_json:        
        lista_asignaciones = json.load(archivo_json)
        print("La lista de campers aprobados ha sido guardada")
        return lista_asignaciones
    except Exception as e:
      print(f"Error al leer el archivo: {e}")
      
lista_asignaciones = load_asignaciones_json()

def listar_campers_aprobados():
    print("Listado de campers Aprobados: ")
    for camper in lista_asignaciones:
        print(camper)