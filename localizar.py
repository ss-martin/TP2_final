# Grupo: 18
# Integrante: Carlos Montero Morales, Tomás Papantos, Martín Saavedra Sanchez

from clase_estacion_tren import EstacionDeTren
import sys

#guardo nombre de archivo, lat y lng
nombreCSV = sys.argv[1]
lat =float(sys.argv[2])
lng = float(sys.argv[3])
#se abre el archivo solicitado
estacionesCSV  = open(nombreCSV, encoding='utf-8')
# Se saltea la primera línea porque es el encabezado del archivo (sin datos)
estacionesCSV.readline()
primero = True
for linea in estacionesCSV:
    linea = linea.split(";")
    if  linea[4]!='' and linea[5]!='':
        #guardo un nuevo registro, si ramal, linea o estacion tiene " las replaza
        new_est = EstacionDeTren(linea[3].replace('"',''), linea[1].replace('"',''), linea[2].replace('"',''), linea[4], linea[5])
        #se gurda la distancia de new_est a la latitud y longitud solicitada
        new_est_dist = new_est.distancia(lat,lng)
        #si es el primer registro que se lee se lo guarda como estacion cercana
        if  primero:
            est_cercana = new_est
            est_cercana_dist = new_est_dist
            primero = False
        #si la distancia de new_est es menor a la previamente guardada se remplaza  y se guarda la estacion cercana
        elif est_cercana_dist > new_est_dist:
            est_cercana_dist = new_est_dist
            est_cercana  = str(new_est)
#se imprime la estacion cercana al punto solicitado
print(est_cercana)

# Se cierra el archivo
estacionesCSV.close()
