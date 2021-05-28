# Grupo: 18
# Integrante: Carlos Montero Morales, Tomás Papantos, Martín Saavedra Sanchez

from clase_estacion_tren import EstacionDeTren
import sys

#guardo nombre de archivo
nombreCSV = sys.argv[1]
#se abre el archivo solicitado
estacionesCSV  = open(nombreCSV, encoding='utf-8')
# Se saltea la primera línea porque es el encabezado del archivo (sin datos)
estacionesCSV.readline()

#se crea un diccionario para guardar los registros
dic_est = dict()
#en este for se recorren todas los registros del archivo
for linea in estacionesCSV:
    linea = linea.split(";")
    #guardo un nuevo registro, si ramal, linea o estacion tiene " las replaza,
    #los campos correspondientes a latitud y longitud, los cargamos con 0, al no ser requerido en el archivo final
    new_est = EstacionDeTren(linea[3].replace('"',''), linea[1].replace('"',''), linea[2].replace('"',''), 0, 0)
    #se colsulta si la linea de new_est ya existe como key en dic_est
    if new_est.linea() in dic_est:
        #se consulta si new_est existe en lista de las keys correspondintre a las lineas. VER COMENTARIOS AL FINAL
        if not( new_est in dic_est[new_est.linea()]):
            # se agrega nuevo registro
            dic_est[new_est.linea()].append(new_est)
    #si no existe  la linea de new_est como key en dic_est, se creo y se carga registro
    else:
        dic_est[new_est.linea()]=[new_est]


f = open ("estaciones_ordenadas.txt", "w")
#se recorre la lista dic_est.keys() (Lineas) de forma ordenada y se escriben los registros para cada key(linea) de dic_est, ordenadas
for x in sorted(dic_est.keys()):
    f.write(x+":"+ ';'.join([(str(list_sort)) for list_sort in sorted(dic_est[x])])+ "\n")

f.close ()
estacionesCSV.close()
#COMENTARIOS: si bien hacemos la verificacion de existencia de new_est en las listas del diccionario
#hemos visto que hay registros linea/ramal/estacion que estan repetidos pero con otros formatos
#por ejemplo Abbot ABBOT, en esos caso  se verán repetidas en "estaciones_ordenadas.txt".
#Sería un tema de estandarizacion de los registros a cargo del responsable de la base de datos
