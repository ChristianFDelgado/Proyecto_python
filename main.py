from commons.utils import limpiar_pantalla
from commons.menus import menu_principal,menu_trainers,menu_campers,menu_matriculas,menu_aulas,menu_reportes,menu_administrador
from businnes.cammpers import crear_camper,listar_campers
from businnes.administracion import crear_rutas,listar_rutas,crear_notas,asignar_campers,listar_campers_aprobados
from businnes.trainers import crear_trainer,listar_trainers
from businnes.aulas import crear_aulas,listar_aulas
from businnes.matriculas import crear_matricula,listar_estudiantes_profesores_por_ruta
from businnes.notas import ingresar_notas,consultar_campers_en_riesgo_por_cedula,listar_campers_en_riesgo
from businnes.reporte import informe_aprobacion_modulos

#bootstrap


# funtions
def campers():
    limpiar_pantalla()
    op=menu_campers()
    if op==1:
       crear_camper()
       input("Clic cualquier teclas [continuar]: ")
    if op==2:
       listar_campers()
       input("Clic cualquier teclas [continuar]: ")
def trainers():
    limpiar_pantalla()    
    op=menu_trainers()
    if op==1:
       crear_trainer()
       input("Clic cualquier teclas [continuar]: ")
    if op==2:
       ingresar_notas()
       input("Clic cualquier teclas [continuar]: ")
def matriculas():
    limpiar_pantalla()    
    op=menu_matriculas()
    if op==1:
       crear_matricula()
       input("Clic cualquier teclas [continuar]: ")
def aulas():
    limpiar_pantalla()    
    op=menu_aulas()
    if op==1:
       crear_aulas()
       input("Clic cualquier teclas [continuar]: ")
    elif op==2:
       listar_aulas()
       input("Clic cualquier teclas [continuar]: ")
def reportes():
    limpiar_pantalla()    
    op=menu_reportes()
    if op==1:
       listar_campers()
       input("Clic cualquier teclas [continuar]: ")
    if op==2:
       listar_campers_aprobados()
       input("Clic cualquier teclas [continuar]: ")
    if op==3:
       listar_trainers()
       input("Clic cualquier teclas [continuar]: ")
    if op==4:
       listar_campers_en_riesgo()
       input("Clic cualquier teclas [continuar]: ")
    if op==5:
       ruta_busqueda = input("Ingrese la ruta que desea buscar: ")
       listar_estudiantes_profesores_por_ruta(ruta_busqueda)
       input("Clic cualquier teclas [continuar]: ")
    if op==6:
       informe_aprobacion_modulos()
       input("Clic cualquier teclas [continuar]: ")
def admministrador():
    limpiar_pantalla()    
    op=menu_administrador()
    if op==1:
        crear_rutas()
        input("Clic cualquier teclas [continuar]: ")
    if op==2:
        listar_rutas()
        input("Clic cualquier teclas [continuar]: ")
    if op==3:
        crear_notas()
        input("Clic cualquier teclas [continuar]: ")
    if op==4:
        asignar_campers()
        input("Clic cualquier teclas [continuar]: ")
    if op==5:
        consultar_campers_en_riesgo_por_cedula()
        input("Clic cualquier teclas [continuar]: ")

    

#start
while True: 
   limpiar_pantalla()
   op=menu_principal()
   if  op==1:
       campers()
   elif op==2:
       trainers()
   elif op==3:
       matriculas()
   elif op==4:
       aulas()
   elif op==5:
       reportes()
   elif op==6:
       admministrador()
   elif op==7:
       print("Saliendo")
       break
       