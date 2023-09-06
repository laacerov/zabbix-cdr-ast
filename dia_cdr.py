# -*- coding: utf-8 -*-

import csv
from datetime import datetime

# Ruta al archivo CSV de CDR
archivo_csv = '/var/log/asterisk/cdr-csv/Master.csv'

# Obtener la fecha actual en el formato deseado (YYYY-MM-DD)
fecha_actual = datetime.now().strftime('%Y-%m-%d')

# Inicializar el total de consumo en segundos
consumo_total_dia = 0

# Abrir el archivo CSV en modo lectura
with open(archivo_csv, mode='r') as archivo:
    # Crear un lector CSV para el archivo
    reader = csv.reader(archivo, delimiter=',', quotechar='"')

    # Leer las filas del archivo y calcular el consumo del día
    for fila in reader:
        fecha_inicio = fila[9]  # Obtener la fecha de inicio del registro

        # Verificar si la fecha de inicio es la del día actual
        if fecha_inicio.startswith(fecha_actual):
            # Sumar el billsec al total de consumo del día en segundos
            consumo_total_dia += int(fila[13])

# Calcular el consumo total del día en minutos y segundos
minutos, segundos = divmod(consumo_total_dia, 60)

print("Consumo total del día {} : {} minutos y {} segundos".format(fecha_actual, minutos, segundos))
