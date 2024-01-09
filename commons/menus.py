from commons.utils import validar_opcion

def menu_principal():
    print("----------- Menú Principal-----------")
    print("1. Campers")
    print("2. Trainers")
    print("3. Matriculas")
    print("4. Aulas")
    print("5. Reportes")
    print("6. Administrador")
    print("7. Salir")       
    op=validar_opcion("Opcion: ",1,7)
    return op

def menu_campers():
    print("----------- Menú Campers-----------")
    print("1. Crear campers")
    print("2. listar campers")
    print("3. Modificar campers")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op
    
    
def menu_trainers():
    print("----------- Menú Trainers-----------")
    print("1. Crear trainer")
    print("2. Evaluaciones")
    print("3. Salir")
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_matriculas():
    print("----------- Menú Matriculas-----------")
    print("1. Registro de matriculas")
    print("2. Buscar Matriculas")
    print("3. Salir")
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_aulas():
    print("----------- Menú Aulas-----------")
    print("1. Crear Aulas")
    print("2. Listar Aulas")
    print("3. Salir")
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_reportes():
    print("----------- Menú Reportes-----------")
    print("1. Listar campers estado inscripto")
    print("2. Listar campers aprobaron examen")
    print("3. Listar trainers trabajando en campus")
    print("4. Listar los estudiantes que cuentan con bajo rendimiento.")
    print("5. Listar los campers y entrenador que se encuentren asociados a una ruta de entrenamiento.")
    print("6. Mostrar cuantos campers perdieron y aprobaron cada uno de los modulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.")
    print("7. Salir")
    op=validar_opcion("Opcion: ",1,7)
    return op

def menu_administrador():
    print("----------- Menú Administrador-----------")
    print("1. Crear Rutas de Entrenamiento")
    print("2. Listar Rutas de Entrenamiento")
    print("3. Registrar notas de prueba")
    print("4. Asignar Campers a Ruta de Aprendizaje")
    print("5. Consultar Campers en riesgo")
    print("6. Salir")
    op=validar_opcion("Opcion: ",1,6)
    return op