import json
import os

def cargar_datos_desde_archivo(archivo):
    try:
        with open(os.path.join("data", archivo), 'r') as archivo_json:
            datos = json.load(archivo_json)
            print(f"La lista de {archivo[:-5]} ha sido cargada")
            return datos
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
        return []
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {archivo}. El formato podría ser incorrecto.")
        return []
    except Exception as e:
        print(f"Error desconocido al cargar datos desde {archivo}: {e}")
        return []

def guardar_datos_en_archivo(archivo, datos, carpeta='data'):
    # Crear la carpeta si no existe
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    ruta_completa = os.path.join(carpeta, archivo)

    with open(ruta_completa, 'w') as archivo:
        json.dump(datos, archivo, indent=2)

def obtener_horario_disponible(profesor, ruta_curso):
    disponibilidad_profesor = profesor.get("disponibilidad", {})
    curso_asignado = next((curso for curso in profesor.get("cursos_asignados", []) if curso["nombre_curso"] == ruta_curso), None)

    if not curso_asignado:
        return None

    horario_curso = curso_asignado.get("horario_curso", {})
    
    for dia, horas_disponibles in disponibilidad_profesor.items():
        if all(hora in horas_disponibles for hora in horario_curso.get(dia, [])):
            return horario_curso

    return None


def crear_matricula():
    asignaciones_lista = cargar_datos_desde_archivo('asignaciones.json')
    profesores_lista = cargar_datos_desde_archivo('profesores.json')
    aulas_lista = cargar_datos_desde_archivo('aulas.json')

    if not asignaciones_lista or not profesores_lista or not aulas_lista:
        print("No se pueden asignar matrículas debido a datos faltantes.")
        return

    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    estudiante = next((est for est in asignaciones_lista if est.get("nombre") == nombre_estudiante), None)

    if not estudiante:
        print(f"No se encontró al estudiante {nombre_estudiante} en la lista de estudiantes aprobados.")
        return

    print(f"Matriculando al estudiante {nombre_estudiante}...")
    ruta_estudiante = estudiante.get("ruta", "")

    profesor_asignado = next((prof for prof in profesores_lista if any(curso["nombre_curso"] == ruta_estudiante for curso in prof.get("cursos_asignados", []))), None)

    if not profesor_asignado:
        print(f"No se encontró un profesor asignado para la ruta {ruta_estudiante}.")
        return

    horario_disponible = obtener_horario_disponible(profesor_asignado, ruta_estudiante)

    if not horario_disponible:
        print(f"No hay horario disponible para el curso {ruta_estudiante} con el profesor {profesor_asignado['nombre']}.")
        return

    aula_asignada = aulas_lista[0]  # Supongamos que asignamos la primera aula disponible, puedes modificar esto según tus criterios.

    matricula = {
        "cedula": estudiante.get("cedula", ""),
        "nombre_estudiante": nombre_estudiante,
        "profesor_asignado": profesor_asignado["nombre"],
        "curso": ruta_estudiante,
        "horario_curso": horario_disponible,
        "fecha_inicio": profesor_asignado["cursos_asignados"][0]["fecha_inicio"],
        "fecha_fin": profesor_asignado["cursos_asignados"][0]["fecha_fin"],
        "nombre_aula": aula_asignada["nombre"]
    }

    matriculas_lista = cargar_datos_desde_archivo('matriculas.json')
    matriculas_lista.append(matricula)
    guardar_datos_en_archivo('matriculas.json', matriculas_lista)

    print(f"Matrícula exitosa para el estudiante {nombre_estudiante}. ¡Bienvenido!")

def listar_estudiantes_profesores_por_ruta(ruta_buscada):
    # Cargar datos desde el archivo matriculas.json
    try:
        with open("data/matriculas.json", 'r') as archivo_matriculas:
            matriculas = json.load(archivo_matriculas)
    except FileNotFoundError:
        print("El archivo matriculas.json no existe.")
        return

    # Filtrar matriculas por la ruta buscada
    matriculas_ruta = [matricula for matricula in matriculas if matricula["curso"] == ruta_buscada]

    if not matriculas_ruta:
        print(f"No hay estudiantes matriculados en la ruta de entrenamiento '{ruta_buscada}'.")
        return

    # Imprimir información de estudiantes y profesores asociados a la ruta
    print(f"Estudiantes y Profesores asociados a la ruta '{ruta_buscada}':")
    for matricula in matriculas_ruta:
        print(f"\nCedula Estudiante: {matricula['cedula']}")
        print(f"Nombre Estudiante: {matricula['nombre_estudiante']}")
        print(f"Profesor Asignado: {matricula['profesor_asignado']}")
        print(f"Curso: {matricula['curso']}")
        print(f"Horario del Curso: {matricula['horario_curso']}")
        print(f"Fecha de Inicio: {matricula['fecha_inicio']}")
        print(f"Fecha de Fin: {matricula['fecha_fin']}")
        print(f"Nombre del Aula: {matricula['nombre_aula']}")
        print("-" * 40)
